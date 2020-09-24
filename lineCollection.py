import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]

lc = LineCollection(lines, colors=['r', 'g', 'b'])
fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax1.add_collection(lc)
ax1.autoscale()
ax1.set_title('Current')

# Doesn't seem to do anything
for l in ax1.lines:
    l.set_marker('o')

ax2 = fig.add_subplot(1, 2, 2)
ax2.plot([0, 1,5], [1, 1,5], 'ro-')
ax2.plot([2, 3], [3, 3], 'go-')
ax2.plot([1, 1], [2, 3], 'bo-')
ax2.set_title('Goal')

plt.show()