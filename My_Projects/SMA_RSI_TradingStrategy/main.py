import pandas as pd
import numpy as np
import yfinance as yf



def MACD_RSI_strategy(symbol):
    # Download historical data for required symbol
    df = yf.download(symbol, start="2021-01-01", end="2022-01-01")
    df.dropna(inplace=True)

    # Calculate MACD and RSI indicators
    def MACD(df, fast=12, slow=26, signal=9):
        """
        function to calculate MACD
        """
        df["MA_Fast"] = df["Adj Close"].ewm(span=fast, min_periods=fast).mean()
        df["MA_Slow"] = df["Adj Close"].ewm(span=slow, min_periods=slow).mean()
        df["MACD"] = df["MA_Fast"] - df["MA_Slow"]
        df["Signal"] = df["MACD"].ewm(span=signal, min_periods=signal).mean()
        return df

    def RSI(df, n=14):
        """
        function to calculate RSI
        """
        delta = df["Adj Close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(n).mean()
        avg_loss = loss.rolling(n).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        df["RSI"] = rsi
        return df

    MACD(df)
    RSI(df)

    # Strategy
    df['Signal'] = np.where((df['MACD'] > df['Signal']) & (df['RSI'] < 30), 1, np.nan)
    df['Signal'] = np.where((df['MACD'] < df['Signal']) & (df['RSI'] > 70), 0, df['Signal'])

    # Create a new dataframe to store signals and positions
    signals = pd.DataFrame(index=df.index)
    signals['Signal'] = df['Signal']
    signals['Price'] = df['Adj Close']
    signals.dropna(inplace=True)

    # Backtesting
    position = None
    entry_price = None
    stop_loss = None
    exit_price = None
    wins = 0
    losses = 0

    for i in range(len(signals)):
        if position is None:
            if signals['Signal'].iloc[i] == 'Buy':
                position = 'Long'
                entry_price = signals['Price'].iloc[i]
                stop_loss = entry_price - 0.05 * entry_price
        elif position == 'Long':
            if signals['Signal'].iloc[i] == 'Sell':
                position = None
                exit_price = signals['Price'].iloc[i]
                if exit_price > entry_price:
                    wins += 1
                else:
                    losses += 1

        if position == 'Long' and signals['Price'].iloc[i] < float(stop_loss):
            position = None
            exit_price = stop_loss
            losses += 1

    return entry_price, exit_price, stop_loss, wins, losses


# Define a list of symbols to analyze
data = pd.read_csv("data.csv")
symbols = list(data["SYMBOL"])

results = []

for symbol in symbols:
    entry_point, exit_point, stop_loss, wins, losses = MACD_RSI_strategy(symbol + ".NS")
    if entry_point and exit_point:
        results.append([symbol, entry_point, exit_point, stop_loss, wins, losses])

# Create a DataFrame from the results
df = pd.DataFrame(results, columns=["Symbol", "Entry Point", "Exit Point", "Stop Loss", "Wins", "Losses"])

print(df)
