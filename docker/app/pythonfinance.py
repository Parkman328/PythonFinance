
import pandas as pd  
import numpy as np
from pandas_datareader import data, wb
import scipy.optimize as sco
from scipy import stats


def _get_tickers(tickers_str, start, end, attrib):
    tickers = list(tickers_str.replace(" ", "").split(","))
    ticker_data = pd.DataFrame([data.DataReader(x, attrib, start, end)['Adj Close'] for x in tickers]).T
    ticker_data.columns = tickers
    return ticker_data

def _get_ticker_data(ticker, start, end):
    ticker_data = data.DataReader(ticker, 'yahoo', start, end)
    return ticker_data

def _get_ticker_closing(ticker, start, end):
    ticker_data = data.DataReader(ticker, 'yahoo', start, end)
    return ticker_data["Adj Close"]

def _get_Percent_change(ticker, start, end, attrib):
    ticker_data = _get_tickers(ticker,start, end, attrib)
    return_data = ticker_data.pct_change()
    return_data.round(6)
    return return_data

def _get_Mean_Daily_Return(ticker, start, end, attrib):
    ticker_data = _get_Percent_change(ticker,start, end, attrib)
    return_data = ticker_data.round(6)
    #print(type(return_data))
    return round(return_data.mean(),6)

def _get_Cov_Matrix(ticker, start, end, attrib):
    ticker_data = _get_Percent_change(ticker,start, end, attrib)
    return_data = ticker_data
    cov_matrix = return_data.cov()
    return cov_matrix

def _calc_portfolio_perf(weights, mean_returns, cov, rf):
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov, weights))) * np.sqrt(252)
    sharpe_ratio = (portfolio_return - rf) / portfolio_std
    return portfolio_return, portfolio_std, sharpe_ratio


def _simulate_random_portfolios(num_portfolios, mean_returns, cov, rf, tickers_str):
    results_matrix = np.zeros((len(mean_returns)+3, num_portfolios))
    tickers = list(tickers_str.replace(" ", "").split(","))
    for i in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        portfolio_return, portfolio_std, sharpe_ratio = _calc_portfolio_perf(weights, mean_returns, cov, rf)
        results_matrix[0,i] = portfolio_return
        results_matrix[1,i] = portfolio_std
        results_matrix[2,i] = sharpe_ratio
        #iterate through the weight vector and add data to results array
        for j in range(len(weights)):
            results_matrix[j+3,i] = weights[j]
            
    results_df = pd.DataFrame(results_matrix.T,columns=['ret','stdev','sharpe'] + [ticker for ticker in tickers])
        
    return results_df