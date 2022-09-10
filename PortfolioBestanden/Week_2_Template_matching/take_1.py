import cv2 as cv
import numpy as np

# Create a VideoCapture object and read from input file
#input from file
# cap = cv.VideoCapture('PortfolioBestanden\Week_2_Template_matching\data\Mickey_trap.mp4')
cap = cv.VideoCapture('PortfolioBestanden\Week_2_Template_matching\data\Mickey_keuken.mp4')

#check for succesful input
if (cap.isOpened()== False):
    print("Error opening video stream or file")

#template
# template = cv.imread('PortfolioBestanden\Week_2_Template_matching\data\MickeyTrapTemplate.png', 0)
template = cv.imread('PortfolioBestanden\Week_2_Template_matching\data\MickeyKeuken.png', 0)  

# print(template)
w, h = template.shape[::-1]

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        method = eval('cv.TM_CCOEFF_NORMED')

        frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

        res = cv.matchTemplate(frame,template,method)
        
        maxv = np.max(res)
        if maxv>0.60:
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            color = (255, 255, 255)
            thickness = 2
            cv.rectangle(frame, top_left, bottom_right, color, thickness)

            template = frame[top_left[1]:top_left[1]+h,top_left[0]:top_left[0]+w]
        frame = cv.rotate(frame, cv.ROTATE_180)
        # Display the resulting frame
        cv.imshow('Frame',frame)

        # Press Q on keyboard to  exit
        if cv.waitKey(75) & 0xFF == ord('q'):
            break

    # Break the loop
    else: 
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv.destroyAllWindows()