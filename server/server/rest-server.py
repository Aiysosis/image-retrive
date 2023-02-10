#!flask/bin/python
################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------
# This file implements the REST layer. It uses flask micro framework for server implementation. Calls from front end reaches 
# here as json and being branched out to each projects. Basic level of validation is also being done in this file. #                                                                                                                                  	       
# -------------------------------------------------------------------------------------------------------------------------------
################################################################################################################################
import json.decoder

from flask import Flask, jsonify, abort, request, make_response, url_for, redirect, render_template, send_file
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import shutil
import numpy as np
from search import recommend

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
from tensorflow.python.platform import gfile

app = Flask(__name__, static_url_path="")
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# ==============================================================================================================================
#                                                                                                                              
#    Loading the extracted feature vectors for image retrieval                                                                 
#                                                                          						        
#                                                                                                                              
# ==============================================================================================================================
extracted_features = np.zeros((10000, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# ==============================================================================================================================
#                                                                                                                              
#  This function is used to do the image search/image retrieval
#                                                                                                                              
# ==============================================================================================================================
@app.route('/imgUpload', methods=['GET', 'POST'])
# def allowed_file(filename):
#    return '.' in filename and \
#           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_img():
    listStr = request.form.get("tags")
    tagList = json.loads(listStr)
    print("list", list)
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imgList = recommend(inputloc, extracted_features)
            imgList = imgList.tolist()

            if len(tagList) > 0:
                tagsImg = []
                for item in tagList:
                    txtName = item + '.txt'
                    path = "./database/tags_all/"
                    absPath = os.path.abspath(path + txtName)
                    f = open(absPath, 'r')
                    for line in f.readlines():
                        curline = int(line.strip())
                        tagsImg.append(curline)
                        if curline > 2955: break

                print('tagsImg', tagsImg)
                imgList = list(set(imgList).intersection(set(tagsImg)))

            res = {
                "data": imgList
            }
            return jsonify(res)


# ==============================================================================================================================
#
#  根据index获取图片
#
# ==============================================================================================================================
@app.route("/image/<int:index>", methods=["GET"])
def get_image(index):
    if index <= 1 or index > 2955:
        return ""
    else:
        imgName = "im{}.jpg".format(index)
        path = "./database/dataset/"
        return send_file(os.path.abspath(path + imgName))


@app.route("/tag", methods=["POST"])
def tag_select():
    listStr = request.form.get("tags")
    list = json.loads(listStr)

    # for item in list:

    return "ok"


# ==============================================================================================================================
#                                                                                                                              
#                                           Main function                                                        	            #						     									       
#  				                                                                                                
# ==============================================================================================================================
@app.route("/")
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
