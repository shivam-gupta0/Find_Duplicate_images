import glob
import cv2
import numpy as np
import os



def rotate_img(image):
    image = np.rot90(image, k=1, axes=(0, 1))
    return image


Folder_path = "Image_Folder_Path"
Duplicate_Folder_Path = "Duplicate_Image_Folder_Path"

duplicate = []
img1 = glob.glob(Folder_path + "\\*.jpg")
img2 = glob.glob(Folder_path + "\\*.jpg")
for im1 in img1:
    for im2 in img2:
        if im1 != im2:
            img = cv2.imdecode(np.fromfile(im1, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            img = img[..., 0:3]
            matrix1 = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)

            img = cv2.imdecode(np.fromfile(im2, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
            img = img[..., 0:3]
            matrix2 = cv2.resize(img, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)

            err = np.sum((matrix1.astype("float") - matrix2.astype("float")) ** 2)
            mse_score = err / float(matrix1.shape[0] * matrix1.shape[1])
            if mse_score == 0:
                imgg1 = cv2.imread(im1)
                height1, width1 = imgg1.shape[:2]
                imgg2 = cv2.imread(im2)
                height2, width2 = imgg2.shape[:2]

                # VISUALIZE SIMILAR IMAGES
                """
                cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("img1", 400, 400)
                cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("img2", 400, 400)
                cv2.imshow("img1",imgg1)
                cv2.imshow("img2",imgg2)
                if cv2.waitKey(0) & 0xFF == ord('q'):
                    break
                """
                
                if height1 * width1 > height2 * width2:
                    duplicate.append(im2)
                else:
                    duplicate.append(im1)

    img2.remove(im1)

for i in duplicate:
    os.rename(i, Duplicate_Folder_Path+'\\'+i[len(Folder_path)+1:])

print(duplicate)
