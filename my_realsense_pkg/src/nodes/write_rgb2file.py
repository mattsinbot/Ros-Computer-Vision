# import the necessary packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import cv2

"""
This code reads an image and writes down the R, G, B data into three separate files.
"""

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# open a file
fp_blue = open("data/blue_channel.txt", 'w')
fp_red = open("data/red_channel.txt", 'w')
fp_green = open("data/green_channel.txt", 'w')

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

