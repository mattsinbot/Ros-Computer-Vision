# import the necessary packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import argparse
import rospy
import cv2

"""
1. The depth_scale of D400 devices is 0.001.

2. The RGBD assume that the depth data haven't been multiplied by the depth_scale and therefore convert the values from millimeters to meters by multiplying the raw data by 0.001

3. This code subscribes to the raw depth data and writes down to a file named "depth_channel.txt"
"""


class WriteDepth2File:
	def __init__(self):
		self.fp_depth = open("data/depth_channel.txt", 'w')
		self.has_written = False
		
	def callback(self, data):
		# Show images
		bridge = CvBridge()
		cv_depth_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
		print(cv_depth_image.shape)
		if not self.has_written:
			for i in range(cv_depth_image.shape[0]):
				for j in range(cv_depth_image.shape[1]):
					self.fp_depth.write(str(cv_depth_image[i, j])+", ")
				self.fp_depth.write("\n")
			print("Depth data has been written to a file\n")
			self.has_written = True
		
	def listener(self):
		rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.callback)
		rospy.spin()

if __name__ == '__main__':
    rospy.init_node("realsense_subscriber", anonymous=True)
    write_depth_data = WriteDepth2File()
    write_depth_data.listener()

"""
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# open a file
fp_blue = open("blue_channel.txt", 'w')
fp_red = open("red_channel.txt", 'w')
fp_green = open("green_channel.txt", 'w')

# load the image
image_pyplot = mpimg.imread(args["image"])
image = cv2.imread(args["image"])
image_slice0 = np.copy(image[:, :, 0])
image_slice1 = np.copy(image[:, :, 1])
image_slice2 = np.copy(image[:, :, 2])

for i in range(image_slice0.shape[0]):
    for j in range(image_slice0.shape[1]):
        fp_blue.write(str(image_slice0[i, j])+", ")
        fp_green.write(str(image_slice1[i, j])+", ")
        fp_red.write(str(image_slice2[i, j])+", ")
    fp_blue.write("\n")
    fp_red.write("\n")
    fp_green.write("\n")

# Show image
plt.imshow(image_pyplot)
plt.show()
"""


