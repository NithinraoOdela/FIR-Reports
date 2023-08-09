from flask import Flask, render_template, url_for, redirect, request, session
from flask_pymongo import PyMongo
import hashlib
import json
from bson import ObjectId

COUNT = 1

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def encode(collection):
    encoder = JSONEncoder()
    j_str = encoder.encode(collection)
    return json.loads(j_str)



app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'complaints'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/complaints'
mongo = PyMongo(app)

firs = mongo.db.FIR

@app.route('/')
def index():
    fir_list = sorted(firs.find(), key=lambda x: x['id'], reverse=True)
    return render_template('index.html', fir_list=(fir_list))



@app.route('/file_case', methods=["POST", "GET"])
def file_case():
    global COUNT
    if request.method == "POST":
        firs.insert_one({"id": f"FIR_NO-{COUNT}", "Name": request.form['name'], "Mobile": request.form['Mobile'], "Date_of_registration": request.form['Date_of_registration'], "Case_Type": request.form['Case_Type'], "Case_Details": request.form['Case_Details']})
        COUNT += 1
        return redirect(url_for('index'))
    return render_template('file-case.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(port=8080, debug=True)


@app.route('/')
def index():
    fir_list = list(firs.find()) 
    return render_template('index.html', fir_list=fir_list)

