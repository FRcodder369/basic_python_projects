import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

flips = [random.randrange(1, 3) for _ in range(10_000)]
values, frequencies = np.unique(flips, return_counts=True)
values = ['heads', 'tails']

title = f'Flling a Coin for {len(flips)} times'

sns.set_style('darkgrid')

axes = sns.barplot(x=values, y=frequencies)

axes.set_title(title)

axes.set_xlabel('Coin Side')
axes.set_ylabel('Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(flips):.3%}'
    axes.text(text_x, text_y, text, ha='center', va='bottom')

plt.show()