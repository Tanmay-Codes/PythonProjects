import yfinance as yf
import pandas as pd
import os


def analyze_stock(symbol):
    # Download the historical data for the symbol
    data = yf.download(symbol, period="3y")

    # Calculate the 20-day simple moving average (SMA)
    data['SMA'] = data['Close'].rolling(window=20).mean()

    # Calculate the 50-day SMA
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    # Calculate the 200-day SMA
    data['SMA200'] = data['Close'].rolling(window=200).mean()

    # Define the entry and exit points based on the SMA crossovers
    if  data['SMA'][-1] < data['SMA50'][-1]:
        entry_point = data['Close'][-1]
        exit_point = data['SMA50'][-1]

        # Calculate the stop loss as 1% below the entry point
        stop_loss = entry_point * 0.99

        # Simulate buying and selling the stock over the past year
        bought = False
        wins = 0
        losses = 0
        profit_loss = 0
        backtest = []
        buy_price = 0
        stop_loss_price = 0
        for i in range(len(data)):
            if not bought and data['SMA'][i] < data['SMA50'][i]:
                bought = True
                buy_price = data['Close'][i]
                stop_loss_price = buy_price * 0.99
                buy_date = data.index[i]
            elif bought and (data['SMA'][i] > data['SMA50'][i] or data['Close'][i] == stop_loss_price) :
                bought = False
                sell_price = data['Close'][i]
                sell_date = data.index[i]
                if sell_price > buy_price:
                    wins += 1
                    profit_loss += sell_price - buy_price
                    backtest.append([symbol, buy_date, buy_price, sell_date, sell_price, stop_loss, wins, losses, profit_loss])

                else:
                    losses += 1
                    profit_loss += sell_price - buy_price
                    backtest.append([symbol, buy_date, buy_price, sell_date, sell_price, stop_loss, wins, losses, profit_loss])

        dfbacktest = pd.DataFrame(backtest,
                                  columns=["Symbol","entry date", "Entry Point", "exit date", "Exit Point", "Stop Loss", "Wins", "Losses", "Profit/loss"])

        # Define the name of the CSV file
        filename = 'trades.csv'
        # Check if the CSV file already exists
        if os.path.exists(filename):
            # If the CSV file already exists, append the data to it
            dfbacktest.to_csv(filename, mode='a', header=False, index=False)
        else:
            # If the CSV file does not exist, create it and write the data to it
            dfbacktest.to_csv(filename, mode='w', header=True, index=False)
        # Return the entry and exit points, stop loss, wins, and losses
        return entry_point, exit_point, stop_loss, wins, losses
    else:
        # Return None for the entry and exit points, stop loss, and 0 wins and losses
        return None, None, None, 0, 0


# Define a list of symbols to analyze
data = pd.read_csv("data.csv")
symbols = list(data["SYMBOL"])
# Create an empty list to hold the results
results = []
# Loop over the symbols and add the results to the list
for symbol in symbols:
    entry_point, exit_point, stop_loss, wins, losses = analyze_stock(symbol + ".NS")
    if entry_point and exit_point:
        results.append([symbol, entry_point, exit_point, stop_loss, wins, losses])

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=["Symbol", "Entry Point", "Exit Point", "stop loss", "Wins", "Losses"])
df.to_csv('entryExitpoints.csv', index=False)
# Print the DataFrame
print(df)

