# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to import the opencv module which is called 'cv2'
import cv2 
# TODO Check the opencv version
print(cv2.__version__)
# TODO Load an image with image reading modes using 'imread'
img = cv2.imread("./tutorials/data/images/chewing_gum_balls10.jpg", cv2.IMREAD_COLOR)
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.

# TODO Resize image with 'resize'
img = cv2.resize(img ,(500,500))

# TODO Rotate image (but keep it rectangular) with 'rotate'
img = cv2.rotate(img, cv2.ROTATE_180)

# TODO Save image with 'imwrite'
print(cv2.imwrite("image.jpg", img))
# TODO Show the image with 'imshow'
win_name = "Fenster"
cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
cv2.imshow(win_name, img)
cv2.waitKey(0)