import pandas as pd
from pandas import DataFrame, Series

from .backtest_functions import backtest_with_rebalance, backtest_without_rebalance


class Backtest:
    def __init__(self):
        self.prices: DataFrame | Series = pd.DataFrame()
        self.values: DataFrame | Series = pd.DataFrame()
        self.exposure: DataFrame | Series = pd.DataFrame()
        self.result: DataFrame | Series = pd.DataFrame()
        self.all_dates: list = []
        self.rebal_dates: list = []

    def set_parameters(self, backtest):
        self.values = backtest["values"].copy()
        self.exposure = backtest["exposure"].copy()
        self.result = backtest["result"].copy()
        self.all_dates = backtest["all_dates"].copy()
        self.rebal_dates = backtest["rebal_dates"].copy()
        return self


class Portfolio:
    def __init__(self, prices: DataFrame = pd.DataFrame()):
        self.prices = prices

    @property
    def tickers(self):
        return self.prices.columns.to_list()

    def run_backtest_with_rebalance(self, rebal_weights="ew", rebal_freq="1M"):
        backtest_results = backtest_with_rebalance(prices=self.prices, rebal_weights=rebal_weights, rebal_freq=rebal_freq)
        backtest = Backtest()
        backtest = backtest.set_parameters(backtest_results)
        return backtest

    def run_backtest_without_rebalance(self, start_weights="ew"):
        backtest_results = backtest_without_rebalance(prices=self.prices, start_weights=start_weights)
        backtest = Backtest()
        backtest = backtest.set_parameters(backtest_results)
        return backtest
