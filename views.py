import joblib
from models import fetchRelevantList
import numpy as np

def carValueView(make, model, year, mileage):
    list = fetchRelevantList(make, model, year)
    if not list:
        return [0.0,list]
    regression_model = joblib.load('mLModel/final_model.sav')
    label_encoder = joblib.load('mLModel/label_encoder.sav')
    car = make + "-" + model + "-" + str(year)
    encoded_car = label_encoder.transform([car])
    carValue = round(regression_model.predict(np.array([encoded_car[0], mileage]).reshape(1,-1))[0], 2)
    return [carValue,list]
