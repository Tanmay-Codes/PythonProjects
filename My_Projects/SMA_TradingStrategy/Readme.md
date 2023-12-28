# SMA Trading Strategy Stock Filter with Backtest


## What This program does ?

- Inputs : CSV data in form of stocks that can be downloaded from the NSE website.
- Calculations : The program will apply the SMA strategy on the stocks and based on that strategy, also run the back test and keep tracks of the wins and looses of that stock as of a result of simulating the trades in the previous 3 Year, The stop loss is kept at 1% and the entry point and exit points are based on SMA50 [Simple Moving Average 50].
- Outputs: The ouputs are in the form of the two diffeent files. Primary file entryExitpoints.csv is created with the potential entry points and number of wins and losses based on the backtest, and the other file trades.csv is created as a detailed recored of all the simulated trades made by the program.

Example files are given in this repository, Open the files data.csv, it was the input file accepted by the program, and the output files are trades.csv and entryExitpoints.csv respectively.


The Simple Moving Average (SMA) trading strategy is a popular technical analysis approach used by traders and investors to identify trends and potential entry or exit points in the financial markets. The SMA is a commonly used indicator that smoothens price data to create a single flowing line, making it easier to identify the direction of the trend. Here's a basic overview of how the SMA trading strategy works:

1. **Calculation of SMA:**
   - Choose a specific time period (e.g., 50 days, 200 days) for which you want to calculate the SMA.
   - Add up the closing prices for the chosen period.
   - Divide the sum by the number of periods.

   The resulting value is the SMA, which is plotted on a price chart over time.

2. **Identification of Trends:**
   - When the current price is above the SMA, it suggests an uptrend.
   - When the current price is below the SMA, it suggests a downtrend.

3. **Entry Signals:**
   - **Golden Cross (Bullish Signal):** This occurs when a short-term SMA (e.g., 50-day) crosses above a long-term SMA (e.g., 200-day). It is considered a bullish signal and may indicate the start of an uptrend.
   - **Death Cross (Bearish Signal):** This happens when a short-term SMA crosses below a long-term SMA. It is considered a bearish signal and may indicate the start of a downtrend.

4. **Exit Signals:**
   - Traders may use crossovers in the opposite direction as exit signals. For example, if you are in a long position and the short-term SMA crosses below the long-term SMA, it could signal a potential trend reversal, prompting you to exit the trade.

5. **Risk Management:**
   - Traders often combine SMA crossovers with other technical indicators or tools to confirm signals and manage risks effectively.
   - It's essential to consider the overall market conditions, potential support and resistance levels, and other relevant factors when making trading decisions.

6. **Limitations:**
   - SMA reacts more slowly to price changes compared to other moving averages, such as Exponential Moving Averages (EMAs).
   - It may produce false signals during ranging or choppy market conditions.

Remember that no trading strategy guarantees success, and it's important to use risk management techniques, including setting stop-loss orders and having a clear understanding of the market conditions. Additionally, traders often customize SMA strategies based on their preferences and the specific assets they are trading.
