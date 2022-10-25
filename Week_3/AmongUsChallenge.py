import cv2 as cv
import numpy as np
import random

# Create video capture object and read from input file, if input is the camera, pass 0 instead of the video file name
cap = cv.VideoCapture(0)
template_1 = "img/crewmate_grey.jpeg"
template_2 = "img/crewmate_red.jpeg"

pathToTemplate = random.choise([template_1, template_2])
print(pathToTemplate)
template = cv.imread(pathToTemplate, 0)
w, h = template.shape[::-1]

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video stream or file")
else:
    print("Video stream or file opened successfully")
    # read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            method = eval('cv.TM_CCOEFF_NORMED')
            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # Apply template Matching
            res = cv.matchTemplate(gray_frame, template, method)
            maxv = np.max(res)
            minv = np.min(res)
            if maxv > 0.50:
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)


            # Display the resulting frame
            cv.imshow('Frame', frame)
            # break if the user presses 'q'
            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

# When everything done, release the video capture object
cap.release()
#destroy all the windows
cv.destroyAllWindows()
