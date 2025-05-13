import json
import os
import FindImage
import CO2Calcs as calcs
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\Basket"
ALLOWED_EXTENSION = set(['jpeg','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

def empty_basket():
   os.remove(os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0]))


app = Flask(__name__)
@app.route("/media/upload", methods = ['POST'])
def upload_media():

    car_type = ""

    if(False):
        return jsonify({'error': ' other media being processed'})
    
    if 'file' not in request.files:
        return jsonify({'error': 'media not provided'}),400
    
    file = request.files['file']
    print(file)
    
    if file.filename == '':
        return jsonify({'error': 'no file selected'}),400
    
  
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(UPLOAD_FOLDER)
        file.save(os.path.join(UPLOAD_FOLDER, str(filename)))
        print("media uploaded successfully. processing")
        
        car_type = FindImage.FindImage()
        empty_basket()
        
        if(car_type == ""):
            return jsonify({'msg': 'error processing image'}),500
    else:
         return jsonify({'msg': 'file not proper'}),500
    
    print(car_type[2:])
    for x in range(0,10):
        print()
    print(calcs.calculte_co2_per_mile([car_type[2:]]))
    return jsonify({'msg':  calcs.calculte_co2_per_mile(car_type[2:])})
    

if(__name__ == '__main__'): 
    app.run(debug= True, port=5000)

def media_finished_being_used():
    using_media = False

