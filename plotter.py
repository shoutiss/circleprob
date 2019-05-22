import circleprob as cp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

VALUE = 200
RED = [1, 0, 0, 1]
BLUE = [0, 0, 1, 1]
DIM = 3

fig = plt.figure(figsize = (12, 12))

axs = fig.subplots(DIM, DIM)

# Create square plots
for i in range(DIM):
    for j in range(DIM):
        axs[i, j].set_aspect('equal')
        axs[i, j].axis([-1.3, 1.3, -1.3, 1.3])

        # Add circle with radius 1 centered at origin
        disk1 = plt.Circle((0, 0), 1, color='blue', fill=False)
        axs[i, j].add_artist(disk1)

# Label plots with method
axs[0, 0].set_title("Method 1 - Pick 2 Endpoints")
axs[0, 1].set_title("Method 2 - Random point is center")
axs[0, 2].set_title("Method 3 - Random radius point is center")

# Initialize list of line endpoints and colors
lines = []
colorlist = []
shortlines = []
longlines = []

# Create circle chords with method 1
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
axs[0, 0].add_collection(lc)
longlc = mc.LineCollection(longlines, colors = BLUE, linewidths = 0.5)
axs[1, 0].add_collection(longlc)
shortlc = mc.LineCollection(shortlines, colors = RED, linewidths = 0.5)
axs[2, 0].add_collection(shortlc)



lines = []
colorlist = []
shortlines = []
longlines = []

# Method 2
# Create circle chords
for _ in range(VALUE):
    # Pick points and add to collection
    center = cp.pick_point_in_circle()
    point1 = cp.find_endpoint(center, 1)
    point2 = cp.find_endpoint(center, -1)
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
axs[0, 1].add_collection(lc)
longlc = mc.LineCollection(longlines, colors = BLUE, linewidths = 0.5)
axs[1, 1].add_collection(longlc)
shortlc = mc.LineCollection(shortlines, colors = RED, linewidths = 0.5)
axs[2, 1].add_collection(shortlc)

# Method 3
lines = []
colorlist = []
shortlines = []
longlines = []

# Method 2
# Create circle chords
for _ in range(VALUE):
    # Pick points and add to collection
    center = cp.pick_radius_point()
    point1 = cp.find_endpoint(center, 1)
    point2 = cp.find_endpoint(center, -1)
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
axs[0, 2].add_collection(lc)
longlc = mc.LineCollection(longlines, colors = BLUE, linewidths = 0.5)
axs[1, 2].add_collection(longlc)
shortlc = mc.LineCollection(shortlines, colors = RED, linewidths = 0.5)
axs[2, 2].add_collection(shortlc)

fig.tight_layout()
fig.savefig("test.png")
plt.show()