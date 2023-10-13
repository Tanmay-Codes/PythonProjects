import datetime
from nsepy import get_history
import pandas as pd

sbin = get_history(symbol='SBIN',
                   start=datetime.date.today() - datetime.timedelta(days=1),
                   end=datetime.date.today())

df = pd.DataFrame(sbin)
print(df)
df.to_csv('out.csv')
difference = df["Close"][1] - df["Prev Close"][1]
percentage = round((abs(difference)/df["Prev Close"][1])*100)
direction = None
if difference > 0:
    direction = f"up by {percentage}%"
else:
    direction = f"down by {percentage}%"

print(direction)