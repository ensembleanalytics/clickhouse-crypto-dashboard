import warnings
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dash import dcc
from dash.dash_table import FormatTemplate
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse, tables
from utils.frontend import no_data_error, small_table

tables = tables[(tables['section'] == 'Analytics') & (tables['category'] == 'DEX')].copy()

def liquidity(protocol, pair):
        
    token0, token1 = pair.split(sep='-')
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': False}
    # )
    #
    # try:
    #     table = tables.loc[(tables['description'] == 'Liquidity') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         timestamp,
    #         token0,
    #         token1,
    #         token0reserveUSD,
    #         token1reserveUSD
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     and
    #         (token0 = '%s' and token1 = '%s') or (token1 = '%s' and token0 = '%s')
    #     order by
    #         timestamp desc
    #     ''' % (table, protocol, token0, token1, token0, token1)
    #     )
    #
    # except:
    #     data = pd.DataFrame()

    # dummy data
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
        'token0': [token0] * 43200,
        'token1': [token1] * 43200,
        'token0reserveUSD': np.cumsum(np.random.lognormal(size=43200)),
        'token1reserveUSD': np.cumsum(np.random.lognormal(size=43200)),
    })
    
    if not data.empty:
        data = data.set_index(['timestamp']).groupby(by=['token0', 'token1'])[['token0reserveUSD', 'token1reserveUSD']]
        data = data.resample('D').last().fillna(method='ffill').reset_index()
        
        df = pd.DataFrame({
            'timestamp': data['timestamp'],
            'token0': np.where(data['token0'] == token0, data['token0reserveUSD'], data['token1reserveUSD']),
            'token1': np.where(data['token1'] == token1, data['token1reserveUSD'], data['token0reserveUSD'])
        })
        
        layout = dict(
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=8,
            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=8,
                ),
            ),
            xaxis=dict(
                type='date',
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            yaxis=dict(
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                tickformat='$,.0f',
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            hoverlabel=dict(
                bgcolor='#ffffff',
                bordercolor='#d9d9d9',
                namelength=-1,
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=6
                ),
            )
        )
        
        traces = []
        
        traces.append(
            go.Scatter(
                x=df['timestamp'],
                y=df['token0'],
                name=token0,
                fillcolor='rgba(68, 180, 40, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(68, 180, 40)',
                    shape='spline'
                ),
            )
        )
        
        traces.append(
            go.Scatter(
                x=df['timestamp'],
                y=df['token1'],
                name=token1,
                fillcolor='rgba(243, 158, 30, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(243, 158, 30)',
                    shape='spline'
                ),
            )
        )
        
        return dcc.Graph(
            figure=go.Figure(data=traces, layout=layout),
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


def volume(protocol, pair):
    
    token0, token1 = pair.split(sep='-')
    
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': False}
    # )
    #
    # try:
    #     table = tables.loc[(tables['description'] == 'Volumes') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         timestamp,
    #         token0,
    #         token1,
    #         token0volumeUSD,
    #         token1volumeUSD
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     and
    #         (token0 = '%s' and token1 = '%s') or (token1 = '%s' and token0 = '%s')
    #     order by
    #         timestamp desc
    #     ''' % (table, protocol, token0, token1, token0, token1)
    #     )
    #
    # except:
    #     data = pd.DataFrame()
    
    # dummy data
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
        'token0': [token0] * 43200,
        'token1': [token1] * 43200,
        'token0volumeUSD': np.cumsum(np.random.lognormal(size=43200)),
        'token1volumeUSD': np.cumsum(np.random.lognormal(size=43200)),
    })
    
    if not data.empty:
        data = data.set_index(['timestamp']).groupby(by=['token0', 'token1'])[['token0volumeUSD', 'token1volumeUSD']]
        data = data.resample('D').last().fillna(method='ffill').reset_index()
        
        df = pd.DataFrame({
            'timestamp': data['timestamp'],
            'token0': np.where(data['token0'] == token0, data['token0volumeUSD'], data['token1volumeUSD']),
            'token1': np.where(data['token1'] == token1, data['token1volumeUSD'], data['token0volumeUSD'])
        })
        
        layout = dict(
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=8,
            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=8,
                ),
            ),
            xaxis=dict(
                type='date',
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            yaxis=dict(
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                tickformat='$,.0f',
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            hoverlabel=dict(
                bgcolor='#ffffff',
                bordercolor='#d9d9d9',
                namelength=-1,
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=6
                ),
            )
        )
    
        traces = []
    
        traces.append(
            go.Scatter(
                x=df['timestamp'],
                y=df['token0'],
                name=token0,
                fillcolor='rgba(68, 180, 40, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(68, 180, 40)',
                    shape='spline'
                ),
            )
        )
    
        traces.append(
            go.Scatter(
                x=df['timestamp'],
                y=df['token1'],
                name=token1,
                fillcolor='rgba(243, 158, 30, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(243, 158, 30)',
                    shape='spline'
                ),
            )
        )
    
        return dcc.Graph(
            figure=go.Figure(data=traces, layout=layout),
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
    
    
def prices(protocol, pair):
        
    token0, token1 = pair.split(sep='-')
    #
    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': False}
    # )
    #
    # try:
    #     table = tables.loc[(tables['description'] == 'Reserves') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         timestamp,
    #         token0symbol as token0,
    #         token1symbol as token1,
    #         token0price,
    #         token1price
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     and
    #        token0 = '%s' and token1 = '%s'
    #     ''' % (table, protocol, token0, token1)
    #     )
    #
    # except:
    #     data = pd.DataFrame()
    
    # dummy data
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
        'token0': [token0] * 43200,
        'token1': [token1] * 43200,
        'token0price': np.cumsum(np.random.normal(size=43200)),
        'token1price': np.cumsum(np.random.normal(size=43200)),
    })
    
    if not data.empty:
        data = data.set_index(['timestamp']).groupby(by=['token0', 'token1'])[['token0price', 'token1price']]
        data = data.resample('D').last().fillna(method='ffill').reset_index()
        
        layout = dict(
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=8,
            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=8,
                ),
            ),
            xaxis=dict(
                type='date',
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            yaxis=dict(
                title=dict(
                    text=token0 + '-' + token1,
                    font=dict(
                        family='Helvetica',
                        color='#667085',
                        size=8
                    )
                ),
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                minexponent=6,
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
                side='left',
            ),
            yaxis2=dict(
                title=dict(
                    text=token1 + '-' + token0,
                    font=dict(
                        family='Helvetica',
                        color='#667085',
                        size=8
                    )
                ),
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                minexponent=6,
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
                side='right',
                anchor='x',
                overlaying='y'
            ),
        )
        
        traces = []
        
        traces.append(
            go.Scatter(
                x=data['timestamp'],
                y=data['token0price'],
                mode='lines',
                name=token0 + '-' + token1,
                line=dict(
                    width=1,
                    color='rgb(68, 180, 40)',
                ),
                yaxis='y'
            )
        )
        
        traces.append(
            go.Scatter(
                x=data['timestamp'],
                y=data['token1price'],
                mode='lines',
                name=token1 + '-' + token0,
                line=dict(
                    width=1,
                    color='rgb(243, 158, 30)',
                ),
                yaxis='y2'
            )
        )
        
        return dcc.Graph(
            figure=go.Figure(data=traces, layout=layout),
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
        return no_data_error(top='8vw', left='43.5vw')


def transactions(protocol, pair):
    
    token0, token1 = pair.split(sep='-')

    # client = Client(
    #     host=clickhouse['host'],
    #     user=clickhouse['user'],
    #     password=clickhouse['password'],
    #     settings={'use_numpy': True}
    # )
    #
    # try:
    #
    #     table = tables.loc[(tables['description'] == 'Trades') & (tables['protocol'] == protocol), 'table'].values[0]
    #
    #     data = client.query_dataframe(query=
    #     '''
    #     select
    #         timestamp,
    #         token0,
    #         token1,
    #         token0inflowUSD,
    #         token0outflowUSD,
    #         token1inflowUSD,
    #         token1outflowUSD
    #     from
    #         %s
    #     where
    #         protocol == '%s'
    #     and
    #         (token0 = '%s' and token1 = '%s') or (token1 = '%s' and token0 = '%s')
    #     order by
    #         timestamp desc
    #     ''' % (table, protocol, token0, token1, token0, token1)
    #     )
    #
    # except:
    #     data = pd.DataFrame()
    
    # dummy data
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
        'token0': [token0] * 43200,
        'token1': [token1] * 43200,
        'token0inflowUSD': [0] * 43200,
        'token0outflowUSD': np.cumsum(np.random.lognormal(size=43200)),
        'token1inflowUSD': np.cumsum(np.random.lognormal(size=43200)),
        'token1outflowUSD': [0] * 43200
    })
    
    if not data.empty:
        data['DEX'] = protocol
        data.rename(columns={'timestamp': 'Timestamp'}, inplace=True)
        
        data['Transaction'] = np.where(
            data['token0inflowUSD'] == 0,
            'Swap ' + data['token0'] + ' for ' + data['token1'],
            'Swap ' + data['token1'] + ' for ' + data['token0']
        )
        
        data['Outflow'] = np.where(
            data['token0inflowUSD'] == 0,
            data['token0outflowUSD'].apply(lambda x: format(x, ',.2f')) + ' ' + data['token0'],
            data['token1outflowUSD'].apply(lambda x: format(x, ',.2f')) + ' ' + data['token1']
        )
        
        data['Inflow'] = np.where(
            data['token0inflowUSD'] == 0,
            data['token1inflowUSD'].apply(lambda x: format(x, ',.2f')) + ' ' + data['token1'],
            data['token0inflowUSD'].apply(lambda x: format(x, ',.2f')) + ' ' + data['token0']
        )
        
        data['Total Value'] = data[['token0inflowUSD', 'token0outflowUSD', 'token1inflowUSD', 'token1outflowUSD']].sum(axis=1)
        data = data[['DEX', 'Transaction', 'Timestamp', 'Inflow', 'Outflow', 'Total Value']]
        
        # generate the table
        table = small_table(
            data=data.to_dict(orient='records'),
            columns=[
                {'name': 'DEX', 'id': 'DEX', 'type': 'text'},
                {'name': 'Transaction', 'id': 'Transaction', 'type': 'text'},
                {'name': 'Timestamp', 'id': 'Timestamp', 'type': 'datetime'},
                {'name': 'Inflow', 'id': 'Inflow', 'type': 'text'},
                {'name': 'Outflow', 'id': 'Outflow', 'type': 'text'},
                {'name': 'Total Value', 'id': 'Total Value', 'type': 'numeric', 'format': FormatTemplate.money(0)},
            ],
            style={'text-align': 'left', 'min-width': '4vw'}
        )
        
        # generate the graph
        count = data.set_index('Timestamp').groupby(by='Transaction')[['Transaction']].resample('D').count()
        value = data.set_index('Timestamp').groupby(by='Transaction')[['Total Value']].resample('D').sum()
        
        if count.shape[0] < 5 or value.shape[0] < 5:
            count = data.set_index('Timestamp').groupby(by='Transaction')[['Transaction']].resample('H').count()
            value = data.set_index('Timestamp').groupby(by='Transaction')[['Total Value']].resample('H').sum()
        
        count = count.rename(columns={'Transaction': 'Count'}).reset_index()
        value = value.rename(columns={'Total Value': 'Value'}).reset_index()
        
        layout = dict(
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(t=30, b=10, l=10, r=10),
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=8,
            ),
            legend=dict(
                traceorder='normal',
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=8,
                ),
            ),
            xaxis=dict(
                type='date',
                color='#667085',
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            yaxis=dict(
                color='#667085',
                tickformat='$,.0f',
                title=dict(
                    text='Value',
                    font=dict(
                        family='Helvetica',
                        color='#667085',
                        size=8
                    ),
                ),
                tickfont=dict(
                    family='Helvetica',
                    color='#667085',
                    size=6
                ),
                linecolor='#d9d9d9',
                mirror=True,
                showgrid=False,
            ),
            hoverlabel=dict(
                bgcolor='#ffffff',
                bordercolor='#d9d9d9',
                namelength=-1,
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=6
                ),
            )
        )
    
        traces = []
    
        traces.append(
            go.Scatter(
                x=count.loc[count['Transaction'] == 'Swap ' + token0 + ' for ' + token1, 'Timestamp'],
                y=count.loc[count['Transaction'] == 'Swap ' + token0 + ' for ' + token1, 'Count'],
                text=['count'],
                mode='lines',
                name='Swap ' + token0 + ' for ' + token1,
                visible=False,
                showlegend=False,
                fillcolor='rgba(68, 180, 40, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(68, 180, 40)',
                    shape='spline'
                )
            )
        )
    
        traces.append(
            go.Scatter(
                x=count.loc[count['Transaction'] == 'Swap ' + token1 + ' for ' + token0, 'Timestamp'],
                y=count.loc[count['Transaction'] == 'Swap ' + token1 + ' for ' + token0, 'Count'],
                text=['count'],
                mode='lines',
                name='Swap ' + token1 + ' for ' + token0,
                visible=False,
                showlegend=False,
                fillcolor='rgba(243, 158, 30, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(243, 158, 30)',
                    shape='spline'
                ),
            )
        )
        
        traces.append(
            go.Scatter(
                x=value.loc[value['Transaction'] == 'Swap ' + token0 + ' for ' + token1, 'Timestamp'],
                y=value.loc[value['Transaction'] == 'Swap ' + token0 + ' for ' + token1, 'Value'],
                text=['value'],
                mode='lines',
                name='Swap ' + token0 + ' for ' + token1,
                visible=False,
                showlegend=False,
                fillcolor='rgba(68, 180, 40, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(68, 180, 40)',
                    shape='spline'
                ),
            )
        )
    
        traces.append(
            go.Scatter(
                x=value.loc[value['Transaction'] == 'Swap ' + token1 + ' for ' + token0, 'Timestamp'],
                y=value.loc[value['Transaction'] == 'Swap ' + token1 + ' for ' + token0, 'Value'],
                text=['value'],
                mode='lines',
                name='Swap ' + token1 + ' for ' + token0,
                visible=False,
                showlegend=False,
                fillcolor='rgba(243, 158, 30, 0.1)',
                stackgroup=pair,
                line=dict(
                    width=1,
                    color='rgb(243, 158, 30)',
                    shape='spline'
                ),
            )
        )
    
        figure = dcc.Graph(
            id='pair-transactions-figure',
            figure=go.Figure(data=traces, layout=layout),
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
    
        return [table, figure]
    
    else:
        return [no_data_error(top='8vw', left='20vw'), no_data_error(top='7vw', left='20vw')]
