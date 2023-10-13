import dash
import pandas as pd
import dash_core_components as dcc
from dash_table import FormatTemplate
from dash_table.Format import Format, Scheme
from dateutil.relativedelta import relativedelta

from queries.home import total_value_locked_data, top_pools_data
from utils.frontend import no_data_error, small_table, large_table, line_chart
from utils.database import tables

def update_total_value_locked_data():
    return total_value_locked_data()


def update_total_value_locked_table(data):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    data = pd.read_json(data, orient='records')
    
    if not data.empty:
        # data = data[data['timestamp'] == data['timestamp'].max()]
        # data = data.drop(labels=['timestamp'], axis=1).reset_index(drop=True)
        #
        # if 'dex-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['protocol'].apply(lambda x: x.lower()).isin([x.lower() for x in tables.loc[tables['category'] == 'DEX', 'protocol'].unique()])]
        #
        # elif 'derivatives-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['protocol'].apply(lambda x: x.lower()).isin([x.lower() for x in tables.loc[tables['category'] == 'Derivatives', 'protocol'].unique()])]
        #
        # elif 'lending-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['protocol'].apply(lambda x: x.lower()).isin([x.lower() for x in tables.loc[tables['category'] == 'Lending', 'protocol'].unique()])]

        table = small_table(
            data=data.to_dict(orient='records'),
            columns=[
                {'name': 'Network', 'id': 'network', 'type': 'text'},
                {'name': 'Protocol', 'id': 'protocol', 'type': 'text'},
                {'name': 'TVL', 'id': 'tvl', 'type': 'numeric', 'format': FormatTemplate.money(0)},
            ],
            style={'text-align': 'left'}
        )

        table.id = 'total-value-locked-table'
        
        return table
    
    else:
        return no_data_error(top='8vw', left='20vw')


def update_total_value_locked_figure(data, table):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    data = pd.read_json(data, orient='records')
    # table = pd.DataFrame(table)
    
    if not data.empty:
        # if not table.empty:
        #     data = data[data['protocol'].isin(table['protocol'].unique().tolist())]
        #
        # data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
        # data = data.set_index('timestamp')[['tvl']].resample('D').sum().reset_index()
        #
        # if '1d-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['timestamp'] >= data['timestamp'].max() - relativedelta(days=1)]
        #
        # elif '7d-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['timestamp'] >= data['timestamp'].max() - relativedelta(days=7)]
        #
        # elif '1m-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['timestamp'] >= data['timestamp'].max() - relativedelta(months=1)]
        #
        # elif '3m-total-value-locked.n_clicks' in changed_id:
        #     data = data[data['timestamp'] >= data['timestamp'].max() - relativedelta(months=3)]
        
        return dcc.Graph(
            figure=line_chart(
                data=data,
                x='timestamp',
                y='tvl',
                name='TVL',
                axistitle='',
                tickformat='$,.0f',
            ),
            config={
                'responsive': True,
                'autosizable': True,
                'displaylogo': False,
            },
            style={
                'height': '100%',
                'width': '100%'
            }
        )
    
    else:
        return no_data_error(top='8vw', left='20vw')
    

def update_top_pools_table():
    data = top_pools_data()
    if not data.empty:
        # data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
        # if 'pair' in data.columns:
        #     data['pair'] = data['pair'].apply(lambda x: x.replace('/', '-'))
        
        return large_table(
            data=data.to_dict(orient='records'),
            columns=[
                {'name': 'Network', 'id': 'network', 'type': 'text'},
                {'name': 'Protocol', 'id': 'protocol', 'type': 'text'},
                {'name': 'Pair', 'id': 'pair', 'type': 'text'},
                {'name': 'Age', 'id': 'age', 'type': 'numeric', 'format': Format(scheme=Scheme.decimal_integer)},
                {'name': 'Volume', 'id': 'volume', 'type': 'numeric', 'format': FormatTemplate.money(0)},
                {'name': 'Liquidity', 'id': 'liquidity', 'type': 'numeric', 'format': FormatTemplate.money(0)},
                {'name': 'Timestamp', 'id': 'timestamp', 'type': 'datetime'},
            ],
            style={
                'text-align': 'left',
                'max-width': '12vw',
                'min-width': '6vw'
            }
        )
    
    else:
        return no_data_error(top='8vw', left='43.5vw')