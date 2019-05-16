import csv

from matplotlib import pyplot as plt
# from datetime import datetime
from datetime import datetime as dt

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

# Get high temp from file
with open(filename) as f:
    reader = csv.reader(f)
    # header_row = next(reader)
    # print(header_row)

    # for row in reader:
    #     print(row)

    # row = next(reader)
    # while row:
    #     print(row)
    #     try:
    #         row = next(reader)
    #     except StopIteration:
    #         break

    # header_row = next(reader)
    # for index, column in enumerate(header_row):
        # print(f'{index:2d} ==> {column.strip()}')

    dates, highs, lows = [], [], []
    header_row = next(reader)
    for row in reader:
        try:
            current_date = dt.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        except ValueError:
            print(current_date, 'missing data')
            continue

# Plot temp in chart
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor=(0.5, 0.5, 0.8), alpha=0.2)

# Format plot
# plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.title("Daily high & low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('')
fig.autofmt_xdate()
plt.ylabel('Temp in F', fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
