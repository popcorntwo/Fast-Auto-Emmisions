import json
import os
import FindImage
import CO2Calcs as calcs
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
#UPLOAD_FOLDER = r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\Basket"
UPLOAD_FOLDER = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "Basket")
ALLOWED_EXTENSION = set(['jpeg','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

def empty_basket():
   os.remove(os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0]))

app = Flask(__name__)

@app.route("/media/upload/co2perkilometer/report", methods = ['POST'])
def co2_per_kilometer_report():
    

    car_type = ""

    if(False):
        return jsonify({'error': ' other media being processed'})
    
    if 'file' not in request.files:
        return jsonify({'error': 'media not provided'}),400

    if request.is_json:
        data = request.get_json(silent=True) or {}
        milage = data.get('milage')
    else:
        milage = request.form.get('milage')

    if milage is None:
        return jsonify({'error': 'no milage detected'}),400

  
    file = request.files['file']
    print(file)
    
    if file.filename == '':
        return jsonify({'error': 'no file selected'}),400
    
    
    milage = request.form['milage']

    if(not milage.isdigit()):
        return jsonify({'error': 'milage contains non-numbers'}),400
    
    milage = float(milage)
    
    print(milage)
  
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(UPLOAD_FOLDER)
        file.save(os.path.join(UPLOAD_FOLDER, str(filename)))
        print("media uploaded successfully. processing")
        
        car_type = FindImage.FindImage()[2:].replace(" ","")
      
        
        if(car_type == ""):
            return jsonify({'msg': 'error processing image'}),500
    else:
         return jsonify({'msg': 'file not proper'}),500
    
    print(car_type)
    print(milage)
    print(calcs.calculte_co2_per_kilometer(car_type))
    return jsonify({'msg':  calcs.report(milage,calcs.calculte_co2_per_kilometer(car_type))})










@app.route("/media/upload/co2perkilometer/percentthisyear", methods = ['POST'])
def co2_per_kilometer_percentthisyear():
    

    car_type = ""

    if(False):
        return jsonify({'error': ' other media being processed'})
    
    if 'file' not in request.files:
        return jsonify({'error': 'media not provided'}),400

    if request.is_json:
        data = request.get_json(silent=True) or {}
        milage = data.get('milage')
    else:
        milage = request.form.get('milage')

    if milage is None:
        return jsonify({'error': 'no milage detected'}),400

  
    file = request.files['file']
    print(file)
    
    if file.filename == '':
        return jsonify({'error': 'no file selected'}),400
    
    
    milage = request.form['milage']

    if(not milage.isdigit()):
        return jsonify({'error': 'milage contains non-numbers'}),400
    
    milage = float(milage)
    
    print(milage)
  
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(UPLOAD_FOLDER)
        file.save(os.path.join(UPLOAD_FOLDER, str(filename)))
        print("media uploaded successfully. processing")
        
        car_type = FindImage.FindImage()[2:].replace(" ","")
      
        
        if(car_type == ""):
            return jsonify({'msg': 'error processing image'}),500
    else:
         return jsonify({'msg': 'file not proper'}),500
    percent = ((calcs.calculte_co2_per_kilometer(car_type) * milage) / 23000000) * 100
    return jsonify({'msg':  str(int(percent))})









@app.route("/media/upload/co2perkilometer", methods = ['POST'])
def co2_per_kilometer():

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
        
        car_type = FindImage.FindImage()[2:].replace(" ","")

        
        if(car_type == ""):
            return jsonify({'msg': 'error processing image'}),500
    else:
         return jsonify({'msg': 'file not proper'}),500

    print(calcs.calculte_co2_per_kilometer(car_type))
    return jsonify({'msg':  calcs.calculte_co2_per_kilometer(car_type)})
    

if(__name__ == '__main__'): 
    app.run(debug= True, port=5000)

def media_finished_being_used():
    using_media = False

