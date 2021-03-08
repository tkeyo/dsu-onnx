import joblib

sess_rfr = joblib.load('model/rfr_regressor.joblib')

def estimate_price(input_values):
    param_1 = input_values['param_1']
    model_input = [param_1]
    result = sess_rfr.predict([model_input])
    return {
            "param_1":param_1,
            "price":int(result.item())
            }
