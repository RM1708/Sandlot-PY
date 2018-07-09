import matplotlib

import matplotlib.pyplot as plt


plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11]) 
plt.xlabel('Months')
plt.ylabel('Books Read')

fig = plt.gcf()

fig.savefig("books_read-BeforeShow_UsingOnlyPyPlot.png")

plt.show()

fig.savefig('books_read-AferShow_UsingOnlyPyPlot.png')

