
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\sanja\\Downloads\\ncr_ride_bookings (1).csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Group by month (sum of booking values per month)
monthly = df.resample("M", on="Date")["Booking Value"].sum()

# Plot monthly bar chart
plt.figure(figsize=(10,7))
bars = plt.bar(monthly.index.strftime("%b"), monthly.values)

plt.xlabel("Month")
plt.ylabel("Total Booking Value")
plt.title("Monthly Booking Value")

# Adding labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10,f"{yval:.0f}", ha="center", va="bottom")

plt.tight_layout()
plt.show()