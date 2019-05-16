import pygal
from die import Die

# Create a D6
die_1 = Die()
die_2 = Die(10)

number_rolls = 50000

# Make some rolls and store results in a list
rolls = []
for i in range(number_rolls):
    roll = die_1.roll() + die_2.roll()
    rolls.append(roll)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    ct = rolls.count(value)
    frequencies.append(ct)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D" + str(die_1.num_sides) + " and one D" + str(die_2.num_sides) + " " + str(number_rolls) + " times"
# hist.x_labels = ['2', '3', '4', '5', '6', '7']
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6D10', frequencies)
hist.render_to_file('die_visual.svg')
