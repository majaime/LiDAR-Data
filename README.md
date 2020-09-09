# LiDAR Data
This code reads .bin file (specially obtained from LiDAR), stores that to a .csv file, and plots the output in a point-cloud format.
It is tested with the raw data available at [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php).
For practice, [synced+rectified data] [calibration] [tracklets] from "2011_09_26_drive_0002" may be downloaded. Files need to be organized in the following manner:
path/to/directory
│   
└───2011_09_26
|   |   calib_cam_to_cam.txt
|   |   calib_imu_to_velo.txt
|   |   calib_velo_to_cam.txt
|   |
│   └───2011_09_26_drive_0001_sync
|   |   |   tracklet_labels.xml
|   |   |
│   |   └───image_00
|   |   |   |   data 
|   |   |   |   timestamps.txt
│   |   └───image_01
|   |   |   |   data
|   |   |   |   timestamps.txt
│   |   └───image_02
│   |   └───image_03
|   |   └───oxts
|   |   |   |   data
|   |   |   |   dataformat.txt
|   |   |   |   timestamps.txt
|   |   └───velodyne_points
|   |   |   |  data
|   |   |   |  timestamps.txt 
|   |   |   |  timestamps_end.txt
|   |   |   |  timestamps_start.txt
|   |
|   └───2011_09_26_drive_0002_sync
|   |   |   ...


