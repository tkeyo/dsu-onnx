import onnxruntime as rt

sess_rfr = rt.InferenceSession('model/rfr_regressor.onnx')
input_name_rfr = sess_rfr.get_inputs()[0].name
label_name_rfr = sess_rfr.get_outputs()[0].name

def estimate_price(input_values):
    param_1 = input_values['param_1']
    model_input = [param_1]
    result = sess_rfr.run([label_name_rfr],{input_name_rfr: model_input})[0]
    return {
            "param_1":param_1,
            "price":int(result.item())
            }
