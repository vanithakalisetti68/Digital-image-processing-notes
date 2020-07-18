import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg", 0)
cv2.imshow("Actual Image", img)


h, w = img.shape
def intensity_res(img, bits):
    new = np.zeros([h, w], dtype=np.uint8)
    multiplier = 2**(8 - bits)
    for row in range(h):
        for col in range(w):
            val = img[row, col]
            new[row, col] = int(val/multiplier)
            val = new[row, col]
            new[row, col] = val*multiplier

    print("IMAGE ",8-bits," bits")
    print("unique elems are ",len(np.unique(new)))
    print(new)
    print("===\n\n")
    return new

print(img)

cv2.imshow("1bit Intensity", intensity_res(img, 1))
cv2.imshow("2bit Intensity", intensity_res(img, 2))
cv2.imshow("3bit Intensity", intensity_res(img, 3))
cv2.imshow("4bit Intensity", intensity_res(img, 4))
cv2.imshow("5bit Intensity", intensity_res(img, 5))
cv2.imshow("6bit Intensity", intensity_res(img, 6))
cv2.imshow("7bit Intensity", intensity_res(img, 7))
cv2.imshow("8bit Intensity", intensity_res(img, 7))

cv2.waitKey(0)
cv2.destroyAllWindows()
