# LiDAR Data
This code reads .bin file (specially obtained from LiDAR), stores that to a .csv file, and plots the output in a point-cloud format.
It is tested with the raw data available at [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php).
For practice, [synced+rectified data] [calibration] [tracklets] from "2011_09_26_drive_0002" may be downloaded. In order to run the code, changes to the input path, base directory etc. should be made accordingly.

# Parsing Tracklets
A script, called parseTrackletXML.py and originally developed by Christian Herdtweck, is used to parse the tracklets.
Tracklets can be directly encrypted based on their labels using another script, called velodyne.py and devloped by [Anthony](https://github.com/anthonyn2121).
