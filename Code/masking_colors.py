from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import numpy as np
import cv2

image = cv2.imread('../Data/cluster_red.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Remember -> OpenCV stores things in BGR order
lowerBound = np.array([0, 0, 0]);
upperBound = np.array([220, 220, 220]);

# this gives you the mask for those in the ranges you specified,
# but you want the inverse, so we'll add bitwise_not...
mask = cv2.inRange(image_rgb, lowerBound, upperBound);
mask_not = cv2.Not(cv_rgb_thresh, cv_rgb_thresh);


res = cv2.bitwise_and(image,image, mask= mask_not)


#show image
plt.figure()
plt.axis('off')
plt.imshow(image)
plt.figure()
plt.imshow(mask)
plt.figure()
plt.imshow(mask)
plt.show()


