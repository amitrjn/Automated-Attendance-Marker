from google.colab import drive
drive.mount('/content/drive')





import sys
sys.path.append('/content/drive/My Drive/DL_Hackathon/project/mtcnn-master')
from mtcnn.mtcnn import MTCNN
import tensorflow as tf
import keras
import cv2
import numpy as np
from keras.models import Model
sys.path.append('/content/drive/My Drive/DL_Hackathon/project')
from inception_resnet_v1 import *

project_path = '/content/drive/My Drive/DL_Hackathon/project/'

detector = MTCNN()

def l2_normalize(x):
 return x / np.sqrt(np.sum(np.multiply(x, x)))

model = InceptionResNetV1()
model.load_weights(project_path + 'model/facenet_weights.h5')


from PIL import Image




stud_img_src = project_path + "DataSet/batch/students/stud_img_src/"

class_strength = 7

dim = (160, 160)

for i in range(class_strength):
    stud_pics = stud_img_src + "rollNo_{}".format(i+1)
    for j in range(5):
        pic = stud_pics + "/{}.jpg".format(j+1)
        pic_cv = cv2.imread(pic)
        face = detector.detect_faces(pic_cv)
        if len(face)!=0:
            face_coordinate = face[0]["box"]
            imageObject = Image.open(pic)
            cropped = imageObject.crop((face_coordinate[0],face_coordinate[1],face_coordinate[0]+ face_coordinate[2],face_coordinate[1]+face_coordinate[3]))
            cropped = np.array(cropped)
            resized_pic = cv2.resize(cropped,dim,interpolation=cv2.INTER_AREA)
            cv2.imwrite(stud_pics + "/face_{}.jpg".format(j+1), resized_pic)
            reshaped_pic = resized_pic.reshape(1,resized_pic.shape[0],resized_pic.shape[1],resized_pic.shape[2])
            pic_representation = l2_normalize(model.predict(reshaped_pic)[0,:])
            np.save(stud_pics + "/{}.npy".format(j+1), pic_representation)
        else:
            resized_pic = cv2.resize(pic_cv,dim,interpolation=cv2.INTER_AREA)
            cv2.imwrite(stud_pics + "/face_{}.jpg".format(j+1), resized_pic)
            reshaped_pic = resized_pic.reshape(1,resized_pic.shape[0],resized_pic.shape[1],resized_pic.shape[2])
            pic_representation = l2_normalize(model.predict(reshaped_pic)[0,:])
            np.save(stud_pics + "/{}.npy".format(j+1), pic_representation)







img_src = project_path + "DataSet/batch/attendances/todayDate/images"
# img_src = "./Dataset/batch/attendances/todayDate/images"
stud_img_src = project_path + "/DataSet/batch/students/stud_img_src/"
class_strength = 7
dim = (160, 160)

img  = cv2.imread(img_src + "/Img_{}.jpg".format(1))
cv2.imwrite("nin.jpg", img)



def l2_normalize(x):
 return x / np.sqrt(np.sum(np.multiply(x, x)))


def findEuclideanDistance(source_representation, test_representation):
 euclidean_distance = source_representation - test_representation
 euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
 euclidean_distance = np.sqrt(euclidean_distance)
 return euclidean_distance








for i in range(1):

    img  = cv2.imread(img_src + "/Img_1.jpg")
    faces = detector.detect_faces(img)

    face_coordinates = []

    for j in range(len(faces)):
        temp = faces[j]
        temp = temp["box"]
        face_coordinates.append(temp)

    imageObject = Image.open(img_src + "/Img_1.jpg")
    
    print("hello")
    print(len(face_coordinates))
    print(face_coordinates)

    for k in range(len(face_coordinates)):
#         print("hello2")
        cropped = imageObject.crop((face_coordinates[k][0],face_coordinates[k][1],face_coordinates[k][0]+ face_coordinates[k][2],face_coordinates[k][1]+face_coordinates[k][3]))
        cropped = np.array(cropped)
        resized_cropped = cv2.resize(cropped,dim,interpolation=cv2.INTER_AREA)
#         cv2.imwrite("/home/amit/Documents/DL_Hackathon/project/DataSet/Img_{}.jpg".format(k), resized_cropped)
        reshaped_cropped = resized_cropped.reshape(1,resized_cropped.shape[0],resized_cropped.shape[1],resized_cropped.shape[2])
        crop_val = l2_normalize(model.predict(reshaped_cropped)[0,:])

        min_euc = 10

        for l in range(class_strength):
#             print("n" + str(l))
            student = stud_img_src + "rollNo_{}".format(l+1)
            sum_euclidean_distance = 0
            local_min = 10
            for m in range(1):
                pic_val = np.load(student + "/{}.npy".format(m+1))
                euclidean_distance = findEuclideanDistance(crop_val, pic_val)
                print(euclidean_distance)
#                 sum_euclidean_distance += euclidean_distance
                if local_min > euclidean_distance:
                    local_min = euclidean_distance
#                 roll_present = l+1

#             sum_euclidean_distance /= 5

            if min_euc > local_min:
                min_euc = local_min
                roll_present = l+1
        
#         print("hello4")
        print(roll_present)

	    #Mark the roll no. roll_present PRESENT in DataBase		



