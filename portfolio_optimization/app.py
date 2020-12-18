from flask import Flask, request, jsonify, render_template
import pythonfinance

app = Flask(__name__)


@app.route('/')
def home():
    return "PythonFinance"

#@app.route('/get_tickers',methods=['POST'])
#def predict():
#    '''
 #   For rendering results on HTML GUI
 #   '''
 #   int_features = [int(x) for x in request.form.values()]
 #   final_features = [np.array(int_features)]
 #   prediction = model.predict(final_features)#

   # output = round(prediction[0], 2)

    #return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/get_tickers',methods=['POST'])
def get_tickers():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    
    output = data
    return jsonify(output)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug ='True', host='0.0.0.0')