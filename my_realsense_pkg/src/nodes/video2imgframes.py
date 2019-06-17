#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# required to convert ROS image to OpenCV image

"""
This code subscribes to the color image from the camera stream and continuously shows in a window
"""

frame_num = 0

def callback(data):
    # Show images
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv2.imwrite("frame-" + str(frame_num) + ".png", cv_image)
    frame_num += 1

def listener():
    rospy.Subscriber("/camera/color/image_raw", Image, callback)
    # rospy.Subscriber("/camera/depth/image_rect_raw", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_image_writer", anonymous=True)
    listener()
