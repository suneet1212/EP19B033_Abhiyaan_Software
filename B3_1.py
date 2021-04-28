# References opencv documentation
import cv2
import numpy as np

img = cv2.imread("abhiyaan_opencv_qn1.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.rectangle(img,(300,30),(330,85),(0,0,0),1)
# roi = img[30:85,304:330]
# cv2.imwrite("roi.png",roi)
roi = cv2.imread('roi.png')
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256])

# # normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsv_roi],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(roi,thresh)
res = np.vstack((roi,thresh,res))
# cv.imwrite('res.jpg',res)


cv2.imshow("hist",res)
cv2.waitKey(0)
cv2.destroyAllWindows()