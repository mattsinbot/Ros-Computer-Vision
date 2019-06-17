# To execute detect_color.py please see below
$ python detect_color.py --image <PATH>/test.png

# To run the contour detection please see below
# Terminal 1:
$ roslaunch realsense2_camera rs_camera.launch

# Optional: launch the following if you need RGBD information from the camera
$ roslaunch realsense2_camera rs_rgbd.launch

# Terminal 2:
$ python image_subscriber.py
