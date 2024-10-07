# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

# TODO Capture webcam image
camera = cv2.VideoCapture(0)

# TODO Get camera image parameters from get()
img_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
img_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(camera.get(cv2.CAP_PROP_FPS))
# TODO Create a window for the video
titel = "test"
cv2.namedWindow(titel, cv2.WINDOW_FREERATIO)
# TODO Start a loop
key = -1
while key == -1:
    
# TODO (In loop) read a camera frame and check if that was successful
    (ret, frame) = camera.read()

        # TODO (In loop) create four flipped tiles of the image
    #flipped = cv2.flip(frame, 1)
    frame_copy = frame.copy()
    ul = frame_copy
    ur = np.fliplr(frame_copy)
    li = np.flipud(frame_copy)
    lr = np.flipud(np.fliplr(frame_copy))
    frame = np.zeros_like(frame_copy)
    frame = cv2.resize(frame, (-1,-1),fx=2.0,fy=2.0)
    frame.[:height,:width] = ul
    frame.[:height,width:width+2] = ur
    frame.[height:height+2,:width] = li
    frame.[height:height+2,width:width+2] = lr
    
        
    


# TODO (In loop) display the image
    cv2.imshow(titel, flipped)

# TODO (In loop) press q to close the window and exit the loop
    key = cv2.waitKey(int((1/fps)*1000))

# TODO Release the video capture object and window
print(key)
camera.release()
cv2.destroyAllWindows()
