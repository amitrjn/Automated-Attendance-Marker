import sys
sys.path.append('./mtcnn-master')
from mtcnn.mtcnn import MTCNN
import tensorflow as tf
import keras
import cv2
import os
import numpy as np
from keras.models import Model
from PIL import Image

from inception_resnet_v1 import *

detector = MTCNN()

def l2_normalize(x):
 return x / np.sqrt(np.sum(np.multiply(x, x)))

model = InceptionResNetV1()
model.load_weights('model/facenet_weights.h5')

stud_img_src = "DataSet/batch/students/stud_img_src/"

# SET THIS VARIABLE BEFORE RUNNING CODE

class_strength = 11

dim = (160, 160)

files = os.listdir(stud_img_src)

for file_name in files:
	stud_pics = stud_img_src + file_name
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
			# cv2.imwrite("face_{}.jpg".format(j+1), resized_pic)
			reshaped_pic = resized_pic.reshape(1,resized_pic.shape[0],resized_pic.shape[1],resized_pic.shape[2])
			pic_representation = l2_normalize(model.predict(reshaped_pic)[0,:])
			np.save(stud_pics + "/{}.npy".format(j+1), pic_representation)
		else:
			resized_pic = cv2.resize(pic_cv,dim,interpolation=cv2.INTER_AREA)
			# cv2.imwrite("face_{}.jpg".format(j+1), resized_pic)
			reshaped_pic = resized_pic.reshape(1,resized_pic.shape[0],resized_pic.shape[1],resized_pic.shape[2])
			pic_representation = l2_normalize(model.predict(reshaped_pic)[0,:])
			np.save(stud_pics + "/{}.npy".format(j+1), pic_representation)



