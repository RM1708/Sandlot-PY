#https://stackoverflow.com/questions/21875356/saving-a-figure-after-invoking-pyplot-show-results-in-an-empty-file
import matplotlib

import matplotlib.pyplot as plt


fig, ax = plt.subplots()

ax.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11]) 
#ax.xlabel('Months')
#ax.ylabel('Books Read')


fig.savefig("books_read-BeforeShow-Recommended.png")

plt.show()

fig.savefig('books_read-AferShow-Recommended.png')

