# libraries
import numpy as np
import pickle
from scaler import MinMaxScaler

# warnings removal
import warnings
warnings.filterwarnings('ignore')


# function to perform prediction
def model_predict(cycle, weight_gain, hair_growth, skin_darkening, fast_food, follicle_no_l, follicle_no_r):

    # scale cycle
    cycle_scaler = MinMaxScaler(2, 5)
    cycle = cycle_scaler.transform(cycle)

    # scale follicle_no_l
    fnl_scaler = MinMaxScaler(0, 18)
    follicle_no_l = fnl_scaler.transform(follicle_no_l)

    # scale follicle_no_r
    fnr_scaler = MinMaxScaler(0, 20)
    follicle_no_r = fnr_scaler.transform(follicle_no_r)

    # load models from the .sav file
    with open('svc_model.sav', 'rb') as file:
        model = pickle.load(file)

    # reshaping and giving output
    array = np.array([cycle, weight_gain, hair_growth, skin_darkening, fast_food, follicle_no_l, follicle_no_r])
    pcos = model.predict(array.reshape(1, -1))
    if pcos == [1]:
        return True
    return False

# predicting test data
# prediction for True
# print(model_predict(2, 1, 1,0, 0, 12, 12))
# prediction for False
# print(model_predict(4, 0, 0,0, 0, 17, 18))