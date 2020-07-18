import joblib
import numpy as np

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
joblib_file = dir_path + '\\ml\\house_model.joblib'

model = joblib.load(joblib_file)

def predict_house(X_test):
    X_test = np.array(X_test)
    X_test = X_test.reshape(1, -1)
    price = model.predict(X_test)
    return price[0]