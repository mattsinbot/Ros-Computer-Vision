#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from cv_bridge import CvBridge, CvBridgeError
from struct import *
# required to convert ROS image to OpenCV image

"""
1. This code subscribes point colud data that is aligned to the color frame coordinate system and prints values of each pointcloud data points.
2. At first run "roslaunch realsense2_camera rs_rgbd.launch" in another terminal
3. To understand how X, Y, Z values have been extracted read my question in ROS answers
"""

def callback_ptclud(ptcloud_data):
	print(ptcloud_data.fields)
	print(ptcloud_data.point_step)
	print(ptcloud_data.row_step)
	row_idx, col_idx = 400, 200
	index = (row_idx*ptcloud_data.row_step) + (col_idx*ptcloud_data.point_step)
	(X, Y, Z) = unpack_from('fff', ptcloud_data.data, offset=index)
	(rgb) = unpack_from('fff', ptcloud_data.data, offset=index+16)
	print(X, Y, Z)
	print(rgb)
	
	# assert isinstance(ptcloud_data, PointCloud2)
	# gen = point_cloud2.read_points(ptcloud_data)
	# print type(gen)
	# count = 0
	# for p in gen:
	# 	print(p)
	# 	count += 1
	# print(count)
	# print(type(ptcloud_data))
	# print(ptcloud_data.header)
	# print(ptcloud_data.height)
	# print(ptcloud_data.width)
	# print(ptcloud_data.fields)
	# print(ptcloud_data.data[0:10])
	# print("-----------------")

def listener():
    # rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, callback)
    rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback_ptclud)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_subscriber", anonymous=True)
    listener()
