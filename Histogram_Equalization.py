import cv2
import numpy as np
import matplotlib.pyplot as plt #importing matplotlib
img=cv2.imread("lena.jpg",0)

rows=img.shape[0]
cols=img.shape[1]

# gray_levels=np.unique(img)
# print(gray_levels)
unique, counts = np.unique(img, return_counts=True)


pdfs=[]
cdf=0
cdfs={}
for pixl,count in zip(unique,counts):
    pdf=count/(rows*cols)
    pdfs.append(pdf)
    cdf+=pdf
    cdfs[pixl]=cdf

cdfmapping={}

L=255

for pixl in unique:

    cdfmapping[pixl]=int(cdfs[pixl]*L)


print("Initial gray levels",len(unique))
print("Final gray levels",len(set(list(cdfmapping.values()))))

print("Pixel mapping is ",cdfmapping)


img2=img.copy()

for row in range(rows):
    for col in range(cols):
        img2[row][col]=cdfmapping[img[row][col]]


plt.hist(img.ravel(),256,[0,256],label="org");
plt.hist(img2.ravel(),256,[0,256],label="Equalized");
plt.legend(loc='upper right')
plt.show()

cv2.imshow("First image",img)

cv2.imshow("Second image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
