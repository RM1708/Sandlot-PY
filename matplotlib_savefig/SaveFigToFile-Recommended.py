#https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig('fig1.pdf')
plt.show()
fig.savefig('fig2.pdf')
