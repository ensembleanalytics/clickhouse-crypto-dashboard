import warnings
import pandas as pd
import numpy as np
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse, tables

tables = tables[(tables['section'] == 'Analytics') & (tables['category'] == 'Derivatives')].copy()

def query_data(protocol):
    # try:
    #     client = Client(
    #         host=clickhouse['host'],
    #         user=clickhouse['user'],
    #         password=clickhouse['password'],
    #         settings={'use_numpy': True}
    #     )
    #
    #     table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #         select
    #             *
    #         from
    #             %s
    #         where
    #             protocol == '%s'
    #     ''' % (table, protocol)
    #     )
    #
    # except:
    #     data = pd.DataFrame()
    #
    # return data

    # dummy data
    return pd.DataFrame({
        'a': np.random.randint(low=0, high=100, size=10),
        'b': np.random.randint(low=0, high=100, size=10),
        'c': np.random.randint(low=0, high=100, size=10),
    })
        

def pods_finance_pools():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # table = tables.loc[(tables['protocol'] == 'Pods Finance') & (tables['description'] == 'Pools'), 'table'].values[0]
    #
    # data = client.query_dataframe(query=
    # '''
    # select
    #     *
    # from
    #     %s
    # order by
    #     expiration desc
    # ''' % table
    # )
    #
    # return data
    return pd.DataFrame({
        'network': np.random.choice(['Ethereum', 'Polygon'], 10),
        'timestamp': pd.date_range(start='2023-09-01', freq='T', periods=10),
        'optionType': np.random.choice(['Call', 'Put'], 10),
        'exerciseType': np.random.choice(['European', 'American'], 10),
        'underlyingAsset': np.random.choice(['ETH', 'BTC'], 10),
        'strikeAsset': np.random.choice(['USD', 'USDT'], 10),
        'strikePrice': np.random.lognormal(size=10),
        'expiration': pd.date_range(start='2023-09-10', freq='T', periods=10),
    })


def pods_finance_options():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # table = tables.loc[(tables['protocol'] == 'Pods Finance') & (tables['description'] == 'Options'), 'table'].values[0]
    #
    # data = client.query_dataframe(query=
    # '''
    # select
    #     *
    # from
    #     %s
    # order by
    #     expiration desc
    # ''' % table
    # )
    #
    # return data
    return pd.DataFrame({
        'network': np.random.choice(['Ethereum', 'Polygon'], 10),
        'timestamp': pd.date_range(start='2023-09-01', freq='T', periods=10),
        'optionType': np.random.choice(['Call', 'Put'], 10),
        'exerciseType': np.random.choice(['European', 'American'], 10),
        'underlyingAsset': np.random.choice(['ETH', 'BTC'], 10),
        'strikeAsset': np.random.choice(['USD', 'USDT'], 10),
        'strikePrice': np.random.lognormal(size=10),
        'expiration': pd.date_range(start='2023-09-10', freq='T', periods=10),
    })


def pods_finance_actions():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # table = tables.loc[(tables['protocol'] == 'Pods Finance') & (tables['description'] == 'Trades'), 'table'].values[0]
    #
    # data = client.query_dataframe(query=
    # '''
    # select
    #   action
    # from
    #   %s
    # ''' % table
    # )
    #
    # return data
    return pd.DataFrame({'action': np.random.choice(['Buy', 'Sell'], 10)})


def synthetix_exchanges():
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # table = tables.loc[(tables['protocol'] == 'Synthetix') & (tables['description'] == 'Exchanges'), 'table'].values[0]
    #
    # data = client.query_dataframe(query=
    # '''
    # select
    #     *
    # from
    #     %s
    # ''' % table
    # )
    #
    # return data
    return pd.DataFrame()