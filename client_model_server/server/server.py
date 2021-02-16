from flask import Flask, request, jsonify,redirect
import util
import pandas as pd

app = Flask(__name__)


@app.route('/get_company_names',methods=['GET'])
def get_company_names():
    response = jsonify({
        'company' :util.get_company_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/',methods=['GET','POST'])
def index():
    form = SearchForm(request.form)
    return render_template('app.html',form=form)


@app.route('/get_model_names',methods=['GET'])
def get_model_names():
    response = jsonify({
        'model'  :util.get_model_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/get_transmission',methods=['GET'])
def get_transmission():
    response = jsonify({
        'transmission' :util.get_transmission()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_location',methods=['GET'])
def get_location():
    response = jsonify({
        'location' :util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_fuel',methods=['GET'])
def get_fuel():
    response = jsonify({
        'fuel':util.get_fuel()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_owner',methods=['GET'])
def get_owner():
    response = jsonify({
        'owner':util.get_owner()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_car_price',methods=['GET','POST'])
def predict_car_price():

    Car_Company = request.form['Car_Company']
    Car_Model   = request.form['Car_Model']
    Engine_CC   = int(request.form['Engine_CC'])
    Power_bhp   = float(request.form['Power_bhp'])
    Mileage_kmpl= float(request.form['Mileage_kmpl'])
    Kilometers_Driven = int(request.form['Kilometers_Driven'])
    Fuel_Type   = request.form['Fuel_Type']
    Transmission= request.form['Transmission']
    Owner_Type  = request.form['Owner_Type']
    Year = int(request.form['Year'])
    Location = request.form['Location']


    response = jsonify({
        'Estimated_Price' : util.predict_price(Car_Company,Car_Model,Engine_CC,Power_bhp,Mileage_kmpl,Kilometers_Driven,Fuel_Type,Transmission,Owner_Type,Year,Location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




if __name__ == "__main__" :
    print("Starting Python Flask Server for Car Price Prediction....")
    util.load_saved_arts()
    app.run(debug=True)
