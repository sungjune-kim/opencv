import cv2 as cv

img = cv.imread('images/bananas/banana_15.jpg')
cv.imshow('Dog', img)

#Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT) # bigger kernel size = more blurier
cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('canny', canny)

#Dilating
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow('dilated',dilated)
'''
#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500))
cv.imshow('resized',resized)

#crop
crop = img[50:200, 200:250]
cv.imshow('crop',crop)
'''
cv.waitKey(0)