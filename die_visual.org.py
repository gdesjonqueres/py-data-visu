import pygal
from die import Die

# Create a D6
die = Die()

# Make some rolls and store results in a list
rolls = []
for i in range(1000):
    rolls.append(die.roll())

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    ct = rolls.count(value)
    frequencies.append(ct)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
