#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# required to convert ROS image to OpenCV image

"""
This code detects closed contours in the view and draws a bounding box around the contour with maximum area.
"""

def callback(data):
    # print("type of data: {}".format(type(data)))
    # rospy.loginfo("Got new message\n")

    # Show images
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    im, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)
    # print("Height: {}, Width: {}".format(c[0][0], c[0][1]))
    marker = cv2.minAreaRect(c)
    box = cv2.boxPoints(marker)
    box = np.int0(box)
    
    # print(box) 
    # print("------------------")

    cv2.drawContours(cv_image, [box], -1, (0, 0, 255), 2)
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('RealSense', edged)
    cv2.imshow('RealSense', cv_image)
    cv2.waitKey(1)
    
def callback2(data):
    # Show images
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', cv_image)
    cv2.waitKey(1)
    
def listener():
    rospy.Subscriber("/camera/color/image_raw", Image, callback)
    # rospy.Subscriber("/camera/color/image_raw", Image, callback2)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_subscriber", anonymous=True)
    listener()
