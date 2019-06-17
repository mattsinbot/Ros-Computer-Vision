#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# required to convert ROS image to OpenCV image

"""
This code subscribes depth data from RealSense camera which is aligned to the color image coordinate frmae.
"""
def callback(data):
	bridge = CvBridge()
	cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
	# print(cv_image.shape)
	cv2.imshow('RealSense', cv_image)
	cv2.waitKey(1)
	
def listener():
    rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_subscriber", anonymous=True)
    listener()
