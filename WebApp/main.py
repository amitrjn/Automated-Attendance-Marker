import os
import string
import random
import sys
sys.path.append('../ModelAndCode/mtcnn-master')
sys.path.append("../ModelAndCode")
from inception_resnet_v1 import *

from mtcnn.mtcnn import MTCNN

from attendanceMarker import driver1
from flask import Flask, request, redirect, url_for, render_template
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/amit/Music/Hackathon/Attendace Marker/ModelAndCode/DataSet/batch/attendances/'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hemant77wave@gmail.com'
app.config['MAIL_PASSWORD'] = 'HK66@gmail##'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/')
def index():
    return render_template('index.html')
    # raise NotImplementedError


@app.route("/submit", methods=['GET', 'POST'])
def submit():

    PHOTO_DIR = UPLOAD_FOLDER + id_generator() +'/'
    print(PHOTO_DIR)
    os.mkdir(PHOTO_DIR)
    app.config['PHOTO_DIR'] = PHOTO_DIR

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('\n\nNo file part\n\n')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('\n\nNo selected file\n\n')
            return redirect(request.url)
        if file: # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['PHOTO_DIR'], filename))
            model = InceptionResNetV1()
            model.load_weights('../ModelAndCode/model/facenet_weights.h5')
            detector = MTCNN()

            driver1(model=model, detector=detector, img_src = PHOTO_DIR)
            present_ = open('present.txt')
            absent_ = open('absent.txt')
            present_recipients = []
            absent_recipients = []
            for email in present_.readlines():
                present_recipients.append(email[:-1])
            for email in absent_.readlines():
                absent_recipients.append(email[:-1])
            print(present_recipients)

            for present in present_recipients:
                print('Sending present Mail to ' + present)
                msg = Message('Attendance', sender = 'no-reply@howcode.org', recipients = [present], body = 'You have been marked present in today class.')
                mail.send(msg)

            for absent in absent_recipients:
                print('Sending absent Mail to ' + absent)
                msg = Message('Attendance', sender = 'no-reply@howcode.org', recipients = [absent], body = 'You have been marked absent in today class.')
                mail.send(msg)
            
    return "Attendace Done" 


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')