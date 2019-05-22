import os
import cv2
from PIL import Image
import numpy as np
from keras.models import Model



def l2_normalize(x):
    return x / np.sqrt(np.sum(np.multiply(x, x)))


def findEuclideanDistance(source_representation, test_representation):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)
    return euclidean_distance


def driver1(model, detector, img_src):

    print(img_src)


    # img_src = "/home/amit/Music/Hackathon/Attendace Marker/ModelAndCode/DataSet/batch/attendances/todayDate/images"
    stud_img_src = "/home/amit/Music/Hackathon/Attendace Marker/ModelAndCode/DataSet/batch/students/stud_img_src/"
    class_strength = 11
    class_photos = 3
    dim = (160, 160)

    attendance = []

    files = os.listdir(img_src)
    attendance = []
    all_Student = []
    temp_file = os.listdir(stud_img_src)
    for file_name in temp_file:
        all_Student.append(file_name)
    for file_name in files:
        if file_name != ".DS_Store":
            img = cv2.imread(img_src + '/' + file_name)
            faces = detector.detect_faces(img)

            face_coordinates = []

            for j in range(len(faces)):
                temp = faces[j]
                temp = temp["box"]
                face_coordinates.append(temp)

            imageObject = Image.open(img_src + '/' + file_name)

            for k in range(len(face_coordinates)):
                cropped = imageObject.crop((face_coordinates[k][0],face_coordinates[k][1],face_coordinates[k][0]+ face_coordinates[k][2],face_coordinates[k][1]+face_coordinates[k][3]))
                cropped = np.array(cropped)
                resized_cropped = cv2.resize(cropped,dim,interpolation=cv2.INTER_AREA)
                reshaped_cropped = resized_cropped.reshape(1,resized_cropped.shape[0],resized_cropped.shape[1],resized_cropped.shape[2])
                crop_val = l2_normalize(model.predict(reshaped_cropped)[0,:])

                min_euc = 1
                weights = [0.6, 0.12, 0.12, 0.08, 0.08]
                file1 = os.listdir(stud_img_src)
                for file_name in file1:
                    #all_Student.append(file_name)
                    student = stud_img_src + file_name
                    sum_euclidean_distance = 0
                    for m in range(1):
                        pic_val = np.load(student + "/{}.npy".format(m+1))
                        euclidean_distance = findEuclideanDistance(crop_val, pic_val)
                        sum_euclidean_distance += euclidean_distance#*weights[m]

                    # sum_euclidean_distance /= 5

                    if min_euc > sum_euclidean_distance:
                        min_euc = sum_euclidean_distance
                        roll_present = file_name

               # print(roll_present)
                
                email = roll_present 
                attendance.append(email)        



    with open('present.txt', 'w+') as f:
        for item in attendance:
            f.write("%s" % item + "@students.iitmandi.ac.in\n")
    absent = []
    flag=1
    for i in range(11):
        flag=0
        for j in range(len(attendance)):
            
            if attendance[j] == all_Student[i]:
                flag=1
        if flag ==0 :
            absent.append(all_Student[i])
    with open('absent.txt', 'w+') as f:
        for item in absent:
            f.write("%s" % item+ "@students.iitmandi.ac.in\n" )




# for i in range(class_photos):

# 	print("inLoop")

# 	img  = cv2.imread(img_src + "/Img_{}.jpg".format(i+1))
# 	faces = detector.detect_faces(img)

# 	face_coordinates = []

# 	for j in range(len(faces)):
# 	    temp = faces[j]
# 	    temp = temp["box"]
# 	    face_coordinates.append(temp)

# 	imageObject = Image.open(img_src + "/Img_{}.jpg".format(i+1))

# 	for k in range(len(face_coordinates)):
# 		cropped = imageObject.crop((face_coordinates[k][0],face_coordinates[k][1],face_coordinates[k][0]+ face_coordinates[k][2],face_coordinates[k][1]+face_coordinates[k][3]))
# 		cropped = np.array(cropped)
# 		resized_cropped = cv2.resize(cropped,dim,interpolation=cv2.INTER_AREA)
# 		reshaped_cropped = resized_cropped.reshape(1,resized_cropped.shape[0],resized_cropped.shape[1],resized_cropped.shape[2])
# 		crop_val = l2_normalize(model.predict(reshaped_cropped)[0,:])

# 		min_euc = 1

# 		for l in range(class_strength):
# 			student = stud_img_src + "rollNo_{}".format(l+1)
# 			sum_euclidean_distance = 0
# 			for m in range(1):
# 				pic_val = np.load(student + "/{}.npy".format(m+1))
# 				euclidean_distance = findEuclideanDistance(crop_val, pic_val)
# 				sum_euclidean_distance += euclidean_distance

# 			# sum_euclidean_distance /= 5

# 			if min_euc > sum_euclidean_distance:
# 				min_euc = sum_euclidean_distance
# 				roll_present = l+1

# 		print(roll_present)
# 		attendance.append(roll_present)		

# with open('attnew.txt', 'w') as f:
# 	for item in attendance:
# 		f.write("%s\n" % item)
	









