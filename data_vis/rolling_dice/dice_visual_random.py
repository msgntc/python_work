import plotly.express as px
from random import randint

from die import Die

# create two D6 dice
die_1 = Die(randint(1, 10))
die_2 = Die(randint(5, 50))

# make some rolls, and store resoults in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the resoults
title = " Results of Rolling a D6 and a D10  50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# further costomize the chart
fig.update_layout(xaxis_dtick=1)

fig.show()
