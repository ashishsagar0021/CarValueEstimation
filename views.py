import joblib
from sklearn.preprocessing import LabelEncoder

def carValueView(make, model, year, mileage):
    regression_model = joblib.load('finalized_model.sav')
    car = make + "-" + model + "-" + str(year)

    userInput = [car, mileage]
    carValue = regression_model.predict(userInput)
    return carValue