import circleprob as cp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

VALUE = 500
RED = [1, 0, 0, 1]
BLUE = [0, 0, 1, 1]

fig = plt.figure(figsize = (12, 12))

axs = fig.subplots(3, 1, sharex = 'col')

# Create square plots
# Both types of line
axs[0].set_aspect('equal')
axs[0].axis([-1.3, 1.3, -1.3, 1.3])

# Chords longer than radius
axs[1].set_aspect('equal')
axs[1].axis([-1.3, 1.3, -1.3, 1.3])

# Chords shorter than radius
axs[2].set_aspect('equal')
# axs[2].set_xlim((-1.3, 1.3))
# axs[2].set_ylim((-1.3, 1.3))
axs[2].axis([-1.3, 1.3, -1.3, 1.3])

# Add circle with radius 1 centered at origin
disk1 = plt.Circle((0, 0), 1, color='blue', fill=False)
axs[0].add_artist(disk1)

disk2 = plt.Circle((0, 0), 1, color='blue', fill=False)
axs[1].add_artist(disk2)

disk3 = plt.Circle((0, 0), 1, color='blue', fill=False)
axs[2].add_artist(disk3)

# Initialize list of line endpoints and colors
lines = []
colorlist = []
shortlines = []
longlines = []

# Create circle chords
for _ in range(VALUE):
    # Pick points and add to collection
    point1 = cp.pick_point_on_circle()
    point2 = cp.pick_point_on_circle()
    lines.append([point1, point2])

    # Calculate distance and determine color
    distance = cp.calc_distance(point1, point2)
    if (distance >= 1):
        colorlist.append(BLUE)
        longlines.append([point1, point2])
    else:
        colorlist.append(RED)
        shortlines.append([point1, point2])

# Add line collections to matplotlib to plot
lc = mc.LineCollection(lines, colors=colorlist, linewidths=0.5)
axs[0].add_collection(lc)
longlc = mc.LineCollection(longlines, colors = BLUE, linewidths = 0.5)
axs[1].add_collection(longlc)
shortlc = mc.LineCollection(shortlines, colors = RED, linewidths = 0.5)
axs[2].add_collection(shortlc)

fig.tight_layout()
plt.show()