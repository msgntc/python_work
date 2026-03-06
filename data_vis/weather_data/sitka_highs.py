from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('data_vis/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# extract high temperatures
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)
print(highs)

# plot the high temperatures
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(highs, color='blue')

# format plot
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(label_size=16)
