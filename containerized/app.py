#!usr/bin/env python

"""
---------------------------------------------------------------------------------------------------
                                        PROGRAM DESCRIPTION
---------------------------------------------------------------------------------------------------
    This file is meant to act as the server running with the docker container. It should contain
    all the necessary files, models, and other libraries needed to run the model. This should
    be designed to work cross platform, on windows/linux/and mac.
"""

# System Modules
import os 
import sys
import base64
import requests
import json
from io import BytesIO
from PIL import Image
from cv2 import cv2
import numpy as np
import image_process
import classifier

# Flask Modules
from flask import Flask, request, Response

# Directory Variables
current_directory = os.getcwd()

if 'containerized' not in current_directory :
    DIRECTORY_PATH = current_directory + '/containerized'
else :
    DIRECTORY_PATH = '.'

MAP = {0:'bench',
       1:'benchpress',
       2:'bicycle',
       3:'dumbbell',
       4:'legpress',
       5:'pullupbar',
       6:'squatrack',
       7:'treadmill',
       8:'yogamat'}

"""
    Main program is located here. Responsible for handling the requests and sending 
    a response to the client
"""

app = Flask(__name__)

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    """ PREDICT THE POTENTIAL PIECE OF EQUIPMENT BASED ON THE REQUEST """
    """
        RECEIVING JSON FORMAT:
        {
            "body" :
                "imgsource" : *base64 value*
        }
    """
    # Extract infomation from the JSON
    data = request.get_json(force=True).get('imgsource')

    path = DIRECTORY_PATH + "/temp/test.png"
    # Decode the BASE64 image and save it into the temp file
    imgdata = base64.b64decode(str(data))
    image = Image.open(BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, img)

    r = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(DIRECTORY_PATH + '/temp/test.png', 'rb')},
        data={'size': 'auto', 'bg_color': 'white'},
        headers={'X-Api-Key': 'iTUtE8hsnt76HMLmfjPAi2hp'},
    )
    if r.status_code == requests.codes.ok:
        with open(DIRECTORY_PATH + '/temp/test.png', 'wb') as out:
            out.write(r.content)
    else:
        print("Error:", r.status_code, r.text)

    # Call the image recognition function
    predictor = classifier.Classifier()
    predicted_label = predictor.image_recognition(DIRECTORY_PATH + '/temp/test.png')
    print(predicted_label)

    max_index = np.argmax(predicted_label[0])
    probability = str(float(predicted_label[0][max_index]*100))
    data_response = {'equipment' : MAP.get(max_index),
                    'probability' : probability
                    }
    response_json = json.dumps(data_response, indent = 4)

    return Response(response = response_json, status=200)
if __name__ == "__main__":
	app.debug = True
	app.run(host = "0.0.0.0", port=int(os.environ.get("PORT", 5000)), threaded=True)