import plotly.express as px

from die import Die

# create a D6
die = Die()

# make some rolls, and store resoults in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyse the results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the resoults
title = " Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
