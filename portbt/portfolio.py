import pandas as pd
from pandas import DataFrame, Series
from typing import Union

from .backtest_functions import backtest_with_rebalance, backtest_without_rebalance
from .utils import format_prices


class Backtest:
    def __init__(self):
        self.prices: Union[DataFrame, Series] = pd.DataFrame()
        self.values: Union[DataFrame, Series] = pd.DataFrame()
        self.exposure: Union[DataFrame, Series] = pd.DataFrame()
        self.result: Union[DataFrame, Series] = pd.DataFrame()
        self.all_dates: list = []
        self.rebal_dates: list = []

    def set_parameters(self, backtest):
        self.prices = backtest["prices"].copy()
        self.values = backtest["values"].copy()
        self.exposure = backtest["exposure"].copy()
        self.result = backtest["result"].copy()
        self.all_dates = backtest["all_dates"].copy()
        self.rebal_dates = backtest["rebal_dates"].copy()
        return self


class Portfolio:
    def __init__(self, prices: DataFrame = pd.DataFrame()):
        self.prices = format_prices(prices)

    @property
    def tickers(self):
        return self.prices.columns.to_list()

    def run_backtest(
        self,
        rebalance: bool,
        weights: Union[str, dict] = "ew",
        rebal_freq: str = "1M",
    ) -> Backtest:
        """
        Create the Backtest object for the imported prices.
        -----
        parameters:
            rebalance: bool (required)
                If 'True', the backtest will rebalance itself.

            weights: str or dict, default 'ew'
                If dict, than it is the weight for each asset (number between 0 and 1),
                The sum can't be different than one.
                Example:
                    asset_weights = {
                        'asset1': 0.3,
                        'asset2': 0.2,
                        'asset3': 0.5,
                    }
                If 'ew', it runs the backtest using equal weight for all assets (1 / number of assets).

            rebal_freq: str, default '1M'
                Rebalance frequency. Has the same valid inputs as pandas.DataFrame.resample() function.
        """
        if rebalance:
            backtest_results = backtest_with_rebalance(
                prices=self.prices, rebal_weights=weights, rebal_freq=rebal_freq
            )
        else:
            backtest_results = backtest_without_rebalance(
                prices=self.prices, start_weights=weights
            )
        return Backtest().set_parameters(backtest_results)
