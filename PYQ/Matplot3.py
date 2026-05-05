import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('Weather_data.csv')

# Convert date column to datetime (important for plotting)
df['date'] = pd.to_datetime(df['date'])

# 1. Line plot (Temperature vs Date)
plt.figure()
plt.plot(df['date'], df['temperature'])
plt.title("Temperature vs Date")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Scatter plot (Humidity vs Date)
plt.figure()
plt.scatter(df['date'], df['humidity'])
plt.title("Humidity vs Date")
plt.xlabel("Date")
plt.ylabel("Humidity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()