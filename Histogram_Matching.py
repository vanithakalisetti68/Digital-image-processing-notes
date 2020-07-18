import numpy as np
import cv2
import matplotlib.pyplot as plt

def cumulative_histogram(hist):
    cum_hist = hist.copy()

    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]

    return cum_hist


def histogram(img):
    height = img.shape[0]
    width = img.shape[1]

    hist = np.zeros((256))

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            hist[a] += 1

    return hist

img_ref = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img_org=img.copy()

height = img.shape[0]
width = img.shape[1]
pixels = width * height

height_ref = img_ref.shape[0]
width_ref = img_ref.shape[1]
pixels_ref = width_ref * height_ref

hist = histogram(img)
hist_ref =histogram(img_ref)

cum_hist = cumulative_histogram(hist)
cum_hist_ref = cumulative_histogram(hist_ref)

prob_cum_hist = cum_hist / pixels

prob_cum_hist_ref = cum_hist_ref / pixels_ref

K = 256
new_values = np.zeros((K))


############################ Magical part ##########################
for a in np.arange(K):
    j = K - 1
    while True:
        new_values[a] = j
        j = j - 1
        if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
            break

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = new_values[a]
        img.itemset((i,j), b)



cv2.imwrite('hist_matched.jpg', img)
#By Murali
cv2.imshow('Resulting image',img)
cv2.imshow('Original image',img_org)
cv2.imshow('Reference image',img_ref)

plt.hist(img.ravel(),256,[0,256],label="Resulting hist");
plt.hist(img_ref.ravel(),256,[0,256],label="REference hist");
plt.hist(img_org.ravel(),256,[0,256],label="Original hist");
plt.legend(loc='upper right')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
