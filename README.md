# portbt
**portbt** is a Python library designed to make backtesting a custom portfolio of assets easy and intuitive. With PortBT, you can test a range of rebalancing strategies and asset allocations using just a few lines of code. 

## Features
- Simple and intuitive code
- Flexible rebalancing options

## Getting Started
To get started with PortBT, simply install the library using pip
```python
pip install portbt
```
 Import it into your Python project. From there, you just have to create a *Portfolio* object with the asset prices to define your portfolio.
 ```python
import portbt as pbt

# sample from brazil, so decimal "," and sep ";"
prices = pd.read_csv('sample/prices.csv', sep=';', decimal=',')
prices.index = pd.to_datetime(prices.index) # index has to be datetime
prices[prices.columns] = prices[prices.columns].astype(float)
prices.name = 'prices'
prices.index.name = 'date'

print(prices)
```
Output
```
                BBAS3     BOVA11      ITUB4      PETR4     SMAL11      VALE3
date                                                                        
2008-11-28   5.848646  36.595901   6.496692   7.174176  23.760300  13.265061
2008-12-01   5.848646  34.744900   6.289404   6.580500  22.656500  12.286927
2008-12-02   5.828202  35.001598   6.447920   6.544737  22.606501  11.829182
2008-12-03   5.848646  35.293800   6.511325   6.905950  22.426001  11.983371
2008-12-04   5.971348  35.122101   6.567414   6.652028  22.636900  11.607532
...               ...        ...        ...        ...        ...        ...
2023-04-03  38.650002  98.300003  24.030001  24.490000  86.500000  80.309998
2023-04-04  39.290001  98.510002  24.510000  24.270000  87.000000  78.040001
2023-04-05  39.150002  97.629997  24.490000  24.350000  85.650002  76.889999
2023-04-06  39.020000  97.589996  24.410000  24.000000  85.879997  76.750000
2023-04-10  39.040001  98.660004  24.670000  24.510000  86.349998  78.230003
```
---
## Creating the portfolio and backtesting
```python
portfolio = pbt.Portfolio(prices)

backtest = portfolio.run_backtest_without_rebalance()

# backtest.values -> values for each asset (starting capital = 1)
# backtest.exposure -> exposure for each asset
# backtest.result -> backtest result, starting from 1
# backtest.all_dates -> all dates for the backtesting, if needed
# backtest.rebal_dates -> rebalace dates only

# example
print(backtest.exposure)
```
Output
```
               BBAS3    BOVA11     ITUB4     PETR4    SMAL11     VALE3
date                                                                  
2008-11-28  0.166667  0.166667  0.166667  0.166667  0.166667  0.166667
2008-12-01  0.174991  0.166140  0.169408  0.160510  0.166862  0.162088
2008-12-02  0.174798  0.167769  0.174094  0.160021  0.166893  0.156424
2008-12-03  0.173115  0.166956  0.173505  0.166643  0.163393  0.156388
2008-12-04  0.177667  0.167009  0.175911  0.161351  0.165789  0.152272
...              ...       ...       ...       ...       ...       ...
2023-04-03  0.253178  0.102909  0.141708  0.130782  0.139475  0.231949
2023-04-04  0.257288  0.103096  0.144492  0.129566  0.140236  0.225321
2023-04-05  0.258185  0.102898  0.145396  0.130913  0.139037  0.223571
2023-04-06  0.258177  0.103195  0.145399  0.129457  0.139871  0.223901
2023-04-10  0.255589  0.103228  0.145400  0.130815  0.139155  0.225814
```

## Portfolio functions
```
Portfolio.backtest_with_rebalance() -> dict
    Optional parameters:
        rebal_weights: dict | str,
        rebal_freq: str,

Portfolio.backtest_without_rebalance() -> dict
    Optional parameters:
        start_weights: dict | str,
```

## TODO
- Performance metrics and visualizations
- Reports