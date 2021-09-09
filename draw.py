import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

# 1.Paint the image certain color
#blank[100:200, 200:250] = 130,255,200
#cv.imshow('colored', blank)

# 2.Draw Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)
#source, sp,ep, thickness(cv.FILLED / -1 = filled)
cv.imshow('Rectangle',blank)

# 3. Draw Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness = -1)
cv.imshow("Circle", blank)

# 4.Draw Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("Line", blank)

# 5. Write Text
cv.putText(blank, 'Hello my name is SJ', (10,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (150,100,10), 2)
cv.imshow("Text", blank)

cv.waitKey(0)