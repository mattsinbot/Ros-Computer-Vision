"""
1. This code identifies pixels with particular color sheds.
2. USAGE : python detect_color.py --image test.png
"""

# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2



"""
def cv2pyplot(img):
	newimg = np.zeros(img.shape)
	newimg[:, :, 0] = np.copy(img[:, :, 2])
	newimg[:, :, 2] = np.copy(img[:, :, 0])
	newimg[:, :, 1] = np.copy(img[:, :, 1])
	return newimg
"""

def write_data(file_name, img_data):
	for i in range(img_data.shape[0]):
		for j in range(img_data.shape[1]):
			if img_data[i, j, 0] > 0 or img_data[i, j, 1] > 0 or img_data[i, j, 2] > 0:
				file_name.write(str(1)+", ")
			else:
				file_name.write(str(0)+", ")
		file_name.write("\n")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# open a file
fp_blue = open("data/blue.txt", 'w')
fp_red = open("data/red.txt", 'w')
fp_green = open("data/green.txt", 'w')

# define the list of boundaries
boundaries = [
	([150, 100, 60], [200, 150, 100]),
	([0, 0, 240], [50, 50, 255]),
	([50, 190, 130], [100, 230, 160])]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

# loop over the boundaries
count = 0
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	if count == 0:
		write_data(fp_blue, output)
	elif count == 1:
		write_data(fp_red, output)
	else:
		write_data(fp_green, output)
	
	print(output.shape)
	count += 1
	
	plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
	plt.show()

	# show the images
	# cv2.imshow("images", np.hstack([image, output]))
	# cv2.waitKey(0)
