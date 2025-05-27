import os
import FindImage as fi
import CO2Calcs as calcs
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from dataclasses import dataclass

UPLOAD_FOLDER = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "Basket")
ALLOWED_EXTENSION = set(['jpeg','jpg'])
RECCOMENDED_CO2 = 23000000

#better stucture support have everything at base be set to None
@dataclass
class Validation_Result:
    error: tuple = None
    milage: float = -1.0
    car_type: str = ""
    co2_per_kilometer: int = 0
 
#functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

def empty_basket():
   os.remove(os.path.join(UPLOAD_FOLDER, os.listdir(UPLOAD_FOLDER)[0]))

def validate_request(require_milage = False):
    returning_validation_result = Validation_Result()
    image_handle_error = auth_and_upload_image(request)
    print (image_handle_error)
    if image_handle_error is None:
        returning_validation_result.car_type = fi.find_image()[2:].replace(" ","") 
        returning_validation_result.co2_per_kilometer = calcs.calculte_co2_per_kilometer(returning_validation_result.car_type)
    else:
        return Validation_Result(error=image_handle_error)
    if require_milage:
        milage_handle_error = auth_milage(request)
        if milage_handle_error is None:
            return Validation_Result(error=milage_handle_error)
        else:
            returning_validation_result.milage=milage_handle_error
    return returning_validation_result
        
#returns eiter tuple if there is a error or null
def auth_and_upload_image(arg):
    if 'file' not in arg.files:
        return jsonify({'error': 'media not provided'}),400
    file = arg.files['file']
    if file.filename == '':
        return jsonify({'error': 'no file selected'}),400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, str(filename)))
    else:
         return jsonify({'error': 'file not proper'}),500
    return None

#returns tuple if hits error or returns the milage as a float
def auth_milage(request):
    milage = -1
    if(request.is_json):
        data = request.get_json(silent=True) or {}
        milage = data.get('milage')
    else:
        milage = request.form.get('milage')
    if milage is None:
        return jsonify({'error': 'no milage detected'}),400
    if not milage.isdigit():
        return jsonify({'error': 'milage contains non-numbers'}),400
    milage = float(milage)
    
    return milage

#main app
app = Flask(__name__)

#Routes
@app.route("/media/upload/co2perkilometer/report", methods = ['POST'])
def co2_per_kilometer_report():
    msg = validate_request(require_milage=True)
    if msg.error is None: return jsonify({'msg':  calcs.report(msg.milage,calcs.calculte_co2_per_kilometer(msg.car_type))})
    return msg.error

@app.route("/media/upload/co2perkilometer/percentthisyear", methods = ['POST'])
def co2_per_kilometer_percentthisyear():
    msg = validate_request(require_milage=True) 
    if msg.error is None:
        percent = (calcs.calculte_co2_per_kilometer(msg.car_type) * msg.milage) / RECCOMENDED_CO2 * 100
        return jsonify({'msg':  str(int(percent))})
    return msg.error

@app.route("/media/upload/co2perkilometer", methods = ['POST'])
def co2_per_kilometer():
    msg: validate_request = validate_request(require_milage=True) 
    if msg.error is None: return jsonify({'msg':  msg.co2_per_kilometer})
    return msg.error

if(__name__ == '__main__'): 
    app.run(debug= True, port=5000)