import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('../Data/test1.jpg',0)
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# img = clahe.apply(img_raw)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=-1)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=-1)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.show()
plt.savefig("clahe.png")
cv2.imwrite("laplacian.png",laplacian)
cv2.imwrite("sobelx_shcarr.png",sobelx)
cv2.imwrite("sobely_scharr.png",sobely)
