# This code reads .bin file (specially obtained from LIDAR),
# stores that to a.csv file, and plots the output in a point-cloud format.
import matplotlib.pyplot as plt
import numpy as np
import csv

# Reading data #
inputPath = '/home/mohammadamin/Desktop/2011_09_26/2011_09_26_drive_0002_sync/velodyne_points/data/0000000000.bin'
outputPath = '/home/mohammadamin/Desktop/2011_09_26/2011_09_26_drive_0002_sync/velodyne_points/data/0000000000.csv'

num = np.fromfile(inputPath, dtype='float32', count=-1, sep='', offset=0)
new = np.asarray(num).reshape(-1, 4)

# Storing the encrypted (.bin) file in (.csv) file
for i in range(0, len(new)): # len(new)
    print(new[i])
    with open(outputPath, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new[i])

# Plotting the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = num[0::4]
Y = num[1::4]
Z = num[2::4]
W = num[3::4]

pointSize = 0.01 * (1 // 1)  # 0.01*(1//0.02)
ax.scatter(X, Y, Z, s=pointSize, c=W)
ax.set_title("Point Cloud Data Visualization")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

