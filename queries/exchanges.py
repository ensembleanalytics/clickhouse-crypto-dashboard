import warnings
import pandas as pd
import numpy as np
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse, tables

tables = tables[(tables['section'] == 'Analytics') & (tables['category'] == 'DEX')].copy()

def volume_data(protocol):
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # try:
    #     table = tables.loc[(tables['description'] == 'Volumes') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         toStartOfDay(timestamp) as timestamp,
    #         concat(concat(token0, '-'), token1) as pair,
    #         sum(token0volumeUSD + token1volumeUSD) as volume
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     group by
    #         timestamp, pair
    #     order by
    #         timestamp
    #     ''' % (table, protocol)
    #     )
    # except:
    #     data = pd.DataFrame()
    #
    # return data

    # dummy data
    return pd.DataFrame({
        'timestamp': pd.date_range(start='2023-06-01', periods=90, freq='D'),
        'pair': ['BTC-USD', 'ETH-USD', 'BTC-USDT'] * 30,
        'volume': np.cumsum(np.random.lognormal(size=90))
    })
    

def liquidity_data(protocol):
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # try:
    #     table = tables.loc[(tables['description'] == 'Liquidity') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         toStartOfDay(timestamp) as timestamp,
    #         concat(concat(token0, '-'), token1) as pair,
    #         sum(token0reserveUSD + token1reserveUSD) as liquidity
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     group by
    #         timestamp, pair
    #     order by
    #         timestamp
    #     ''' % (table, protocol)
    #     )
    #
    # except:
    #     data = pd.DataFrame()
    #
    # return data
    # dummy data
    return pd.DataFrame({
        'timestamp': pd.date_range(start='2023-06-01', periods=90, freq='D'),
        'pair': ['BTC-USD', 'ETH-USD', 'BTC-USDT'] * 30,
        'liquidity': np.cumsum(np.random.lognormal(size=90))
    })