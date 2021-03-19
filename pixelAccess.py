# we importing the necessarily required packages for this program
import argparse
import cv2

# we now creating the object of the argumentParser and passing arguments on that
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image path")
args = vars(ap.parse_args())

# now, we loading the image
image = cv2.imread(args["image"])

# we access the height and width of the image using the shape library and showing the result
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

# In opencv all images are just like numpy array and stores like a matrix.
# The top most first pixel we can access through the values of x,y (0, 0) as
# we already explained before the python index starts from 0 not from 1.
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# now, we are going to change the pixel value of (0, 0) to red tuple
image[0, 0] = (0, 0, 255)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# now, we are going to compute the centre of the image, which simply divides the width and height
# by 2
(cX, cY) = (w // 2, h // 2)

# As we are using the NumPy array, so we can use the slice method to access the large pixels
# of the image -- let's grab the top-left corner
imageTarget = image[0:cY, 0:cX]
cv2.imshow("Top-Left image Corner", imageTarget)
cv2.waitKey(0)

# Now, as we did before top-left cropped, we are going to do similar way for the
# top-right, bottom-left and bottom-right and display their results on the screen
topright = image[0:cY, cX:w]
bottomright = image[cY:h, cX:w]
bottomleft = image[cY:h, 0:cX]
cv2.imshow("Top-Right image", topright)
cv2.imshow("Bottom-Right image", bottomright)
cv2.imshow("Bottom-Left image", bottomleft)
cv2.waitKey(0)

# now we are going to change the colour of the bottomleft colour of the cropped image to red
image[cY:h, 0:cX] = (0, 0, 255)
# Will display the new updated image
cv2.imshow("After change the pixel colour", image)
cv2.waitKey(0)
