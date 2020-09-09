# LiDAR Data
This code reads .bin file (specially obtained from LiDAR), stores that to a .csv file, and plots the output in a point-cloud format.
It is tested with the raw data available at [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php).
For practice, [synced+rectified data] [calibration] [tracklets] from "2011_09_26_drive_0002" may be downloaded.

# Parsing Tracklets
A script, originally developed by [Alex Staravoitau](https://github.com/navoshta), is used to parse the tracklets, called parseTrackletXML.py .
