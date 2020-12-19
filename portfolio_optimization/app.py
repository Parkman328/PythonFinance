from flask import Flask, request, jsonify, render_template
import pythonfinance

app = Flask(__name__)


@app.route('/')
def home():
    return "PythonFinance"

# @app.route('/get_tickers',methods=['POST'])
# def predict():
#    '''
 #   For rendering results on HTML GUI
 #   '''
 #   int_features = [int(x) for x in request.form.values()]
 #   final_features = [np.array(int_features)]
 #   prediction = model.predict(final_features)#

   # output = round(prediction[0], 2)

    # return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


@app.route('/get_ticker_data', methods=['POST'])
def get_ticker_data():
    '''
    For direct API calls trought request
    '''
    # print(request)
    data = request.get_json(force=True)
    print('This is Payload {}, {}. {}' .format(
        data['data'], data['start_date'], data['end_date']))
    output = pythonfinance._get_ticker_data(
        data['data'], data['start_date'], data['end_date'])
    print(output) 
    return output.to_json(orient='split')


@app.route('/get_ticker_closing', methods=['POST'])
def get_ticker_closing():
    '''
    For direct API calls trought request
    '''
    # print(request)
    data = request.get_json(force=True)
    print('This is Payload {}, {}. {}' .format(
        data['data'], data['start_date'], data['end_date']))
    output = pythonfinance._get_ticker_closing(
        data['data'], data['start_date'], data['end_date'])
    print(output)
    return output.to_json(orient='split')


@app.route('/get_tickers', methods=['POST'])
def get_tickers():
    '''
    For direct API calls trought request
    '''
    # print(request)
    data = request.get_json(force=True)
    print('This is Payload {}, {}. {}' .format(data))
    output = pythonfinance._get_tickers(data['data'], data['start_date'], data['end_date'], data['attrib'])
    print(output)
    return output.to_json(orient='split')


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug='True', host='0.0.0.0')
