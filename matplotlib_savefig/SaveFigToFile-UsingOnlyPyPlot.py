#https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x**2

plt.plot(x, y)
fig = plt.gcf()
fig.savefig('fig1_OnlyPyPlot.pdf')
plt.show()
fig.savefig('fig2_OnlyPyPlot.pdf')


