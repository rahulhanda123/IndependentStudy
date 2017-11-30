import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../Data/test1.jpg',0)
img_color = cv2.imread('../Data/test1.jpg')
imS = cv2.resize(img, (800, 600))
imS_color = cv2.resize(img_color, (800, 600))
#hist,bins = np.histogram(img.flatten(),256,[0,256])

#cdf = hist.cumsum()
#cdf_normalized = cdf * hist.max()/ cdf.max()

#plt.plot(cdf_normalized, color = 'b')
#plt.hist(img.flatten(),256,[0,256], color = 'r')
#plt.xlim([0,256])
#plt.legend(('cdf','histogram'), loc = 'upper left')
#plt.show()
#
img2 = cv2.equalizeHist(imS)

# res = np.hstack((imS,img2))
res2 = cv2.cvtColor(imS_color, cv2.COLOR_BGR2YCR_CB)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
res3 = clahe.apply(img)

res4 = cv2.cvtColor(imS_color,cv2.COLOR_BGR2HSV);
#CV_BGR2YCrCb
# cv2.namedWindow('display', cv2.WINDOW_NORMAL);
# cv2.resizeWindow('display', 600,600)
# cv2.imshow('display', res)
# cv2.imshow('original', imS)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.subplot(2,2,1),plt.imshow(res4)
plt.title('HSV'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(img2,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(imS_color)
plt.title('YcrCb'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(res3,cmap = 'gray')
plt.title('clahe'), plt.xticks([]), plt.yticks([])
plt.show()