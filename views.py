import joblib
import pickle
from models import fetchRelevantList
import numpy as np

def carValueView(make, model, year, mileage):
    list = fetchRelevantList(make, model, year)
    if not list:
        return [0.0,list]
    car = make + "-" + model + "-" + str(year)
    # Load params pkl file
    with open('mLModel/final_param.pkl', 'rb') as file:
        params = pickle.load(file)

    # Load the scaler from scaler.pkl
    with open("mLModel/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    scaler_input = np.array([[mileage, 1]])
    scaler_output = scaler.transform(scaler_input)
    input_mileage = scaler_output[0][0]

    m = -0.28314033
    c = -0.24260677

    if car in params.keys():
        m = params[car][0][0].flatten()[0]
        c = params[car][1].flatten()[0]

    price = m*input_mileage + c
    model_out = np.array([[1, price]])
    actual_price = scaler.inverse_transform(model_out)
    return [round(max(int(round(actual_price[0][1],-2)),0),2),list]

# Standardize the input mileage
