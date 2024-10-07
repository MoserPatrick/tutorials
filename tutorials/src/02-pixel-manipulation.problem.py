# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color
img_gray = cv2.imread("./tutorials/data/images/chewing_gum_balls10.jpg", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./tutorials/data/images/chewing_gum_balls10.jpg", cv2.IMREAD_COLOR)

img = img_gray

# TODO Do some print out about the loaded data using type, dtype and shape
print(type(img))
print(img.dtype)
print(img.shape)

# TODO Continue with the grayscale image

# TODO Extract the size or resolution of the image
if (img.all() == img_gray.all()):
    height, width = img.shape
    print(height)
    print(width)
else:
    height, width, color= img.shape
    print(height)
    print(width)

# TODO Resize image
img = cv2.resize(img,(300,200))

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row
#print(img[0,:])


# TODO Print first column
#print(img[:,0])

# TODO Continue with the color image
img = img_color
img = cv2.resize(img,(300,200))

# TODO Set an area of the image to black
#img[100:150,20:80] = 0

# TODO Show the image and wait until key pressed
win_name = "Fenster"
cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
cv2.imshow(win_name, img)
cv2.waitKey(0)

# TODO Find all used colors in the image
all_rgb_codes = img.reshape(-1, img.shape[-1])
unique_rgbs = np.unique(all_rgb_codes, axis=0, return_counts= False)
print("Those are the Colors: " + str(unique_rgbs))
# TODO Copy one part of an image into another one
img_filler = img[100:150,20:80]
img[150:200,20:80] = img_filler
# TODO Save image to a file
print(cv2.imwrite("image.jpg", img))
# TODO Show the image again
win_name = "Fenster"
cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
cv2.imshow(win_name, img)
cv2.waitKey(0)

# TODO Show the original image (copy demo)

