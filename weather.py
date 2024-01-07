# Follow the instructions for coding a weather app
# Ryan Dennis

from statistics import mean
# I used https://www.geeksforgeeks.org/python-statistics-mean-function/
# to find the information to import the mean function

# Nested list
daily_values = [
    [62, 42, 0.48],
    [64, 48, 0.53],
    [79, 47, 0.46],
    [52, 24, 0.44],
    [46, 28, 0.4],
    [50, 28, 0.6],
    [58, 32, 0.58],
    [66, 37, 0.5],
    [71, 43, 0.48],
    [77, 46, 0.43],
    [78, 48, 0.41],
    [78, 47, 0.39],
    [76, 48, 0.39],
    [79, 49, 0.38],
    [77, 50, 0.4]
]

# Initialize value for daily_values list
value = 0

# For loop to separate nested list into separate lists using list comprehension
for value in daily_values:
    daily_high = [value[0] for value in daily_values]
    daily_low = [value[1] for value in daily_values]
    daily_humidity = [value[2] for value in daily_values]

# I used https://www.geeksforgeeks.org/python-split-nested-list-into-two-lists/
# for an example of unpacking a nested list using list comprehension.

# Calculate averages
avg_high = mean(daily_high)
avg_low = mean(daily_low)
avg_humidity = mean(daily_humidity)

# Calculate min and max of lows and highs
min_high = min(daily_high)
max_high = max(daily_high)
min_low = min(daily_low)
max_low = max(daily_low)

# Calculate number of days for the forecast.
num_days = len(daily_values)

print(f"Weather forecast for the next {num_days} days: The average high will be {avg_high:.0f} and the average low will be {avg_low:.0f}. \
The highest temperature will be {max_high:.0f}. The lowest temperature will be {min_low:.0f}. The average humidity will be {avg_humidity:.2f}.")

# I used https://stackoverflow.com/questions/4172448/is-it-possible-to-break-a-long-line-to-multiple-lines-in-python#:~:text=The%20preferred%20way%20of%20wrapping,indent%20the%20continued%20line%20appropriately.
# as a reference to find that \ can be used to break up a long line of code
# into multiple lines to make it easier to read
