#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# required to convert ROS image to OpenCV image

def callback(data):
    # Show images
    bridge = CvBridge()
    # cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', cv_image)
    cv2.waitKey(1)
    
def listener():
    rospy.Subscriber("/camera/color/image_raw", Image, callback)
    # rospy.Subscriber("/camera/depth/image_rect_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_subscriber", anonymous=True)
    listener()
