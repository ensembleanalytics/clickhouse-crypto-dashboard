import warnings
import pandas as pd
import numpy as np
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse

def total_value_locked_data():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # data = client.query_dataframe(query='''
    # select
    #     *
    # from
    #     timeflow_crypto.tvl_aggregated
    # where
    #     timestamp != 0
    # ''')
    #
    # return data.to_json(orient='records')
    return pd.DataFrame({
        'timestamp': pd.date_range(start='01-09-2023', periods=10, freq='D'),
        'network': ['Ethereum', 'Polygon'] * 5,
        'protocol': ['Uniswap', 'SushiSwap', 'Uniswap', 'Curve Finance', 'Convex Finance'] * 2,
        'tvl': np.cumsum(np.random.lognormal(size=10))
    }).to_json(orient='records')


def top_pools_data():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # data = client.query_dataframe(query='''
    # select
    #     *
    # from
    #     timeflow_crypto.liquidity_pools_aggregated
    # ''')
    #
    # return data
    return pd.DataFrame({
        'timestamp': pd.date_range(start='01-09-2023', periods=10, freq='D'),
        'network': ['Ethereum', 'Polygon'] * 5,
        'protocol': ['Uniswap', 'SushiSwap', 'Uniswap', 'Curve Finance', 'Convex Finance'] * 2,
        'pair': ['ETH-USD', 'BTC-USD'] * 5,
        'age': np.random.lognormal(size=10),
        'volume': np.random.lognormal(size=10),
        'liquidity': np.random.lognormal(size=10)
    })
 