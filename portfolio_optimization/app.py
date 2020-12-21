from flask import Flask, request
import datetime
import logging
import pythonfinance

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    log_level = logging.DEBUG
    app.logger.setLevel(log_level)

@app.route('/')
def home():
    app.logger.debug("main debug")
    app.logger.info("main info")
    app.logger.warning("main warning")
    app.logger.error("main error")
    app.logger.critical("main critical")
    return "PythonFinance " +  str(datetime.datetime.now())

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
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}, {}. {}' .format(
        data['data'], data['start_date'], data['end_date']))
    output = pythonfinance._get_ticker_data(
        data['data'], data['start_date'], data['end_date'])
    app.logger.debug(output) 
    return output.to_json(orient='split')


@app.route('/get_ticker_closing', methods=['POST'])
def get_ticker_closing():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}, {}. {}' .format(
        data['data'], data['start_date'], data['end_date']))
    output = pythonfinance._get_ticker_closing(
        data['data'], data['start_date'], data['end_date'])
    app.logger.debug(output)
    return output.to_json(orient='split')


@app.route('/get_tickers', methods=['POST'])
def get_tickers():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}' .format(data))
    output = pythonfinance._get_tickers(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug(output)
    return output.to_json(orient='split')

@app.route('/get_Percent_change', methods=['POST'])
def get_Percent_change():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}' .format(data))
    output = pythonfinance._get_Percent_change(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug(output)
    return output.to_json(orient='split')

@app.route('/get_Mean_Daily_Return', methods=['POST'])
def get_Mean_Daily_Return():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}' .format(data))
    output = pythonfinance._get_Mean_Daily_Return(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug(output)
    return output.to_json(orient='split')

@app.route('/get_Cov_Matrix', methods=['POST'])
def get_Cov_Matrix():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    app.logger.debug('This is Payload {}' .format(data))
    output = pythonfinance._get_Cov_Matrix(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug(output)
    return output.to_json(orient='split')

@app.route('/simulate_random_portfolios', methods=['POST'])
def simulate_random_portfolios():
    '''
    For direct API calls trought request
    '''
    # app.logger.debug(request)
    data = request.get_json(force=True)
    #num_portfolios, mean_returns, cov, rf,tickers
    app.logger.debug('This is Payload {}' .format(data))
    mean_returns = pythonfinance._get_Mean_Daily_Return(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug('Mean Returns')
    app.logger.debug(mean_returns)
    cov = pythonfinance._get_Cov_Matrix(data['data'], data['start_date'], data['end_date'], data['attrib'])
    app.logger.debug('Cov')
    app.logger.debug(cov)
    output = pythonfinance._simulate_random_portfolios(data['num_portfolios'], mean_returns, cov, data['rf'], data['data'])
    app.logger.debug('Output')
    app.logger.debug(output)
    return output.to_json(orient='split')

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug='True', host='0.0.0.0')
