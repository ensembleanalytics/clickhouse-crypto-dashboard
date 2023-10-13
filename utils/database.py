import json
from clickhouse_driver import Client

# with open('access/clickhouse.json', 'r') as f:
#     clickhouse = json.load(f)

# client = Client(
#     host=clickhouse['host'],
#     user=clickhouse['user'],
#     password=clickhouse['password'],
#     port=clickhouse['port'],
#     settings={'use_numpy': True}
# )
#
# tables = client.query_dataframe('select * from timeflow_crypto.data_dictionary')

# dummy data
clickhouse = {}

import pandas as pd

tables = pd.DataFrame({
    'section': [
        'Analytics',
        'Analytics',
        'Analytics',
        'Analytics',
        'Analytics',
        'Blockchains',
        'Blockchains',
    ],
    'category': [
        'DEX',
        'DEX',
        'Derivatives',
        'Derivatives',
        'Derivatives',
        'Networks',
        'Networks',
    ],
    'description': [
        'Liquidity',
        'Liquidity',
        'Options',
        'Options',
        'Pools',
        'Blocks',
        'Blocks',
    ],
    'protocol': [
        'Uniswap',
        'SushiSwap',
        'Curve Finance',
        'Convex Finance',
        'Pods Finance',
        'Ethereum',
        'Polygon',
    ]
    
})