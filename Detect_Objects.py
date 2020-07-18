import cv2
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
from tqdm import tqdm
import numpy
numpy.set_printoptions(threshold=numpy.nan)

img=cv2.imread("shape.png",0)


rows=img.shape[0]
cols=img.shape[1]
print(rows,cols)
img2=img.copy()


for row in range(rows):
    for col in range(cols):
        if img2[row][col]==255:
            img2[row][col]=0

        else:

            img2[row][col]=1

# img_list=[
#         [0 ,     0   ,   0  ,    0   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0],
#       [0 ,     1   ,   1  ,    1   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0],
#       [0 ,     1   ,   1  ,    1   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0],
#       [0 ,     1   ,   1  ,    1   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0],
#       [0 ,     0   ,   0  ,    0   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0],
#       [0 ,     0   ,   0  ,    0   ,   1  ,    0   ,   0  ,    1   ,   1   ,   0],
#       [0 ,     0   ,   0  ,    0   ,   1  ,    0   ,   0  ,    1   ,   1   ,   0],
#       [0 ,     0   ,   0  ,    0   ,   1  ,    1   ,   1  ,    1   ,   1   ,   0],
#       [0 ,     1   ,   1  ,    1   ,   1  ,    1   ,   1  ,    1   ,   1   ,   0],
#       [0 ,     1   ,   1  ,    1   ,   1  ,    1   ,   1  ,    1   ,   1   ,   0],
#       [0 ,     0   ,   0  ,    0   ,   0  ,    0   ,   0  ,    0   ,   0   ,   0]]
#
# img3=np.array(img_list)
#
# img2=img3.copy()
# #
# rows=img2.shape[0]
# cols=img2.shape[1]
# #
#
# # print(img2)
print("\n\nresult is \n\n\n")
def give_neighbors(i,j):
    positions=[]
    for o in range(-1,1):
        positions.append([i+o,j+o])


    return positions


label_count=0

matching=[]
curr_label=0

for row in tqdm(range(1,rows),desc="Parsing rows"):
    # print(row," row")
    for col in tqdm(range(1,cols),desc="Parsing cols"):
        # print(col," col")

        upp_arr=1
        down_arr=1

        neighbors_flag=0

        if row-1<0:
            upp_arr=0
            neighbors_flag=1
        if col-1<0:
            down_arr=0
            neighbors_flag=1

        if img2[row-upp_arr][col] ==0 and img2[row][col-down_arr]==0 and img2[row][col]==0:
            continue

        if img2[row-upp_arr][col] ==0 and img2[row][col-down_arr]==0 :
            # print("Both equal to 0",row,col,img2[row][col])
            label_count=curr_label+1
            curr_label=label_count

            if img2[row][col]!=curr_label and img2[row][col]!=0 :
                img2[row,col]=label_count

        # print("Both equal to 0",row,col,img2[row][col])

        upper_val=img2[row-upp_arr][col]
        left_val=img2[row][col-down_arr]

        neighbors=[upper_val,left_val]


        if left_val!=upper_val and (0 in neighbors):  ## 0, class pass it
            pass

        if left_val==upper_val and (0 not in neighbors):  ## Pixel having same class neighbor pixels
            pass

        if left_val!=upper_val and (0 not in neighbors):   ## Deals with Conflicting pixels , intersections
            # matching.append([left_val,upper_val])

            first_time=1


            # if len(matching)==0:
            #     matching.append([left_val,upper_val])
            #
            for clsters in matching:

                # print(clsters,"Beeofre")
                if left_val in clsters or upper_val in clsters:
                    clsters+=[left_val,upper_val]
                    # print(clsters,"After")
                    first_time=0
                    break

            if first_time==0:
                pass
            else:
                matching.append([left_val,upper_val])


        if img2[row][col]!=0 and (left_val!=0 or upper_val!=0):
            # print(left_val,upper_val)
            img2[row,col]=max(left_val,upper_val)

# print(img2)



# matching=list(set(matching))
# print(matching)
print(len(matching))

final_cluster=[]

print("Matching is ",matching)

for clster in tqdm(matching,desc='clustering'):

    clster_max=max(clster)

    final_cluster.append(clster_max)

    for row in tqdm(range(rows),desc='rows'):
        for col in tqdm(range(cols),desc='cols'):
            if img2[row][col] in clster:
                img2[row][col]=clster_max


print(img2)
print(np.unique(img2))

print("Number of unique objects are ",len(np.unique(img2))-1)

cv2.imshow("Output image ",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
