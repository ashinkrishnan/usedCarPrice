import pickle
import json
import pandas as pd
import numpy as np

__columns      = None

__company      = None
__model_name   = None
__Transmission = None
__location     = None
__fuel         = None
__owner        = None


__model        = None


def predict_price(company,model,cc,bph,mileage,km,fuel,trans,owner,year,location):
    input_df = pd.DataFrame({

        'Car_Company': company,
        'Car_Model'  : model,
        'Engine_CC'  : cc,
        'Power_bhp'  : bph,
        'Mileage_kmpl':mileage,
        'Kilometers_Driven':km,
        'Fuel_Type'   : fuel,
        'Transmission': trans,
        'Owner_Type'  : owner,
        'Year':year,
        'Location' :location

                            },index=[0])
    return round(__model.predict(input_df)[0],2).astype(str)






def get_columns():
    return __columns
def get_company_names():
    return __company
def get_model_names():
    return __model_name
def get_transmission():
    return __Transmission
def get_location():
    return __location
def get_fuel():
    return __fuel
def get_owner():
    return __owner

def load_saved_arts():
    print('loading saved arts.....')
    global  __columns
    global  __company
    global  __model_name
    global  __Transmission
    global  __location
    global  __fuel
    global  __owner

    global __model

    with open("./art/data01.json", 'r') as f:
        __columns = json.load(f)['columns']

    with open("./art/data01.json",'r') as f:
        __company = json.load(f)['company']

    with open("./art/data01.json", 'r') as f:
        __model_name   = json.load(f)['model']

    with open("./art/data01.json", 'r') as f:
        __Transmission = json.load(f)['Transmission']

    with open("./art/data01.json", 'r') as f:
        __location = json.load(f)['location']

    with open("./art/data01.json", 'r') as f:
        __fuel = json.load(f)['fuel']

    with open("./art/data01.json", 'r') as f:
        __owner = json.load(f)['owner']

    with open("./art/final_xgbmodel_rev01.pickle",'rb') as f:
        __model = pickle.load(f)

    print('loading done!!!!!!!')



if __name__ == '__main__':
    load_saved_arts()
    print(get_columns())
    print(get_company_names())
    print(get_model_names())
    print(get_transmission())
    print(get_location())
    print(get_fuel())
    print(get_owner())

    print(predict_price('maruti', 'wagonR', 998, 48.68, 20.0, 77325, 'petrol', 'manual', 'second', 2008, 'pune'))


