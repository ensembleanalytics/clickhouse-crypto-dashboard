import json
import warnings
import datetime
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse
from utils.frontend import no_data_error, section_header, large_table

def get_timedelta(interval, units):
    if units == 'years':
        return relativedelta(years=interval)
    
    elif units == 'months':
        return relativedelta(months=interval)
    
    elif units == 'days':
        return relativedelta(days=interval)
    
    elif units == 'hours':
        return relativedelta(hours=interval)
    
    elif units == 'minutes':
        return relativedelta(minutes=interval)
    
    elif units == 'seconds':
        return relativedelta(seconds=interval)


def query_data(protocol, table, interval, units):

    # try:
    #     try:
    #
    #         client = Client(
    #             host=clickhouse['host'],
    #             user=clickhouse['user'],
    #             password=clickhouse['password'],
    #             settings={'use_numpy': True}
    #         )
    #
    #         start = (datetime.datetime.now() - get_timedelta(interval, units)).strftime('%Y-%m-%d %H:%M:%S')
    #         end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #
    #         data = client.query_dataframe(query='''
    #         select
    #             *
    #         from
    #             %s
    #         where
    #             toDateTime(timestamp) > '%s' and toDateTime(timestamp) < '%s'
    #         and
    #             protocol == '%s'
    #         order by
    #             timestamp desc
    #         ''' % (table, protocol, start, end))
    #
    #     except:
    #
    #         client = Client(
    #             host=clickhouse['host'],
    #             user=clickhouse['user'],
    #             password=clickhouse['password'],
    #             settings={'use_numpy': True}
    #         )
    #
    #         data = client.query_dataframe(query='''
    #         select
    #             *
    #         from
    #             %s
    #         where
    #             protocol == '%s'
    #         ''' % (table, protocol))
    #
    # except:
    #     data = pd.DataFrame()

    # dummy data
    data = pd.DataFrame({
        'a': np.random.randint(low=0, high=100, size=10),
        'b': np.random.randint(low=0, high=100, size=10),
        'c': np.random.randint(low=0, high=100, size=10),
    })
    
    if not data.empty:
        
        return [
            
            section_header('Total Records in Set: ' + format(data.shape[0], ',.0f')),

            large_table(
                data=data.to_dict(orient='records'),
                columns=[{'name': x, 'id': x} for x in data.columns],
                style={
                    'text-align': 'left',
                    'min-width': '10vw',
                    'max-width': '10vw',
                    'width': '10vw',
                    'text-overflow': 'ellipsis'
                },
            ),
            
            [

                json.dumps(data.select_dtypes(include=['int32', 'int64', 'float32', 'float64']).columns.tolist()),
                json.dumps(data.select_dtypes(include=['object']).columns.tolist()),
                json.dumps(data.select_dtypes(include=['datetime64']).columns.tolist()),
                data.to_json(orient='records'),
            
            ]
            
    ]
    
    else:

        return [
            section_header('No Records Found'),
            no_data_error(top='14vw', left='44vw'),
            None
        ]
