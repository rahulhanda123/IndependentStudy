from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import disp_utils
import cv2

image = cv2.imread('../Data/cluster_red.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


#put all pixels in a list

pixels_list = image.reshape((image.shape[0]*image.shape[1], 3))
print "starting"
clt = KMeans(n_clusters = 14)
print "initialized kmeans"
clt.fit(pixels_list)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = disp_utils.centroid_histogram(clt)
bar = disp_utils.plot_colors(hist, clt.cluster_centers_)

print clt.cluster_centers_
#show image
plt.figure()
plt.axis('off')
plt.imshow(image)


plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
