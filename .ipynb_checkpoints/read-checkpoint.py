import cv2 as cv

img = cv.imread('images/dogs/dog_5.jpg')
cv.imshow('Dog', img)

'''
#video read
capture = cv.VideoCapture('')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
'''

#waits for a key to be pressed 0:infinite
cv.waitKey(0) 