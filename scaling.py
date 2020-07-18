import cv2
import numpy as np
img=cv2.imread("lena.jpg",0)
print(type(img))
#cv2.imshow('image',img)
#cv2.waitKey(1000)
#cv2.destroyAllWindows()
#cv2.imwrite("tstgray.jpg",img)
img2=img.copy()
print(img2.shape)


sm=0

#thresh=100
#maxVal=255


imgs=[]

for k in range(0,8):
	img2=img.copy()
	ex=k
	for i in range(img2.shape[0]):
		for j in range(img2.shape[1]):
			img2[i][j]=int(img2[i][j]/(2**ex))

	print("IMAGE ",k)
	print(len(np.unique(img2)))

	imgs.append(img2)
		# if img2[i][j] > thresh:
		# 	img2[i][j]=maxVal
		# else:
		# 	img2[i][j]=0

cv2.imshow(' 0 image',imgs[0])
cv2.imshow(' 1 image',imgs[1])
cv2.imshow(' 2 image',imgs[2])
cv2.imshow(' 3 image',imgs[3])
cv2.imshow(' 4 image',imgs[4])
cv2.imshow(' 5 image',imgs[5])
cv2.imshow(' 6 image',imgs[6])

#cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()









########################################### SPATIAL RESOLUTION ###############################
# img3=img.copy()

# cv2.imshow('image',img3)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()


# spatial_res=int(input("Enter the rows,cols to be removed"))
# rowno=img3.shape[0]
# colno=img3.shape[1]

# if rowno-spatial_res<0 or colno-spatial_res<0:
	# print("Exceeding the dimension of image")
# else:
	# for _ in range(spatial_res):
		# rowno=img3.shape[0]
		# colno=img3.shape[1]
		# if rowno-1<0 or colno-1<0:continue
		# img3=img3[:-1,:-1]

		# print(img3.shape)
		# cv2.imshow('image',img3)
		# cv2.waitKey(1000)
		# cv2.destroyAllWindows()
