import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


co_area = ['San Diego', 'San Fran', 'Los Angeles', 'Sacramento', 'San Jose']
co_cases = (.271, .354, 1.22, .098, .11)
clt = ['blue', 'blue', 'red', 'blue']
plt.bar(co_area, co_cases, color = clt, edgecolor = 'black')
plt.xlabel('City')
plt.ylabel('Covid Cases (in Millions)')



plt.show()
