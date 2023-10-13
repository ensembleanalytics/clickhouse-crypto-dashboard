import plotly.graph_objects as go
import dash_core_components as dcc
from dash_table.Format import Format, Scheme
from dash_table import FormatTemplate

import queries.derivatives as queries
from utils.frontend import no_data_error, small_table, large_table

def update_derivatives_data(pathname):
    protocol = pathname.split(sep='/')[-1].replace('-', ' ')
    data = queries.query_data(protocol)
    if not data.empty:
        return large_table(
            data=data.to_dict(orient='records'),
            columns=[{'name': x, 'id': x} for x in data.columns],
            style={
                'text-align': 'left',
                'min-width': '6vw'
            }
        )
    else:
        return no_data_error(top='13vw', left='43.5vw')


def update_pods_finance_pools_table_and_graphs():
    data = queries.pods_finance_pools()
    # data.drop(labels=['protocol', 'pool', 'option'], axis=1, inplace=True)
    
    if not data.empty:
        return [
            small_table(
                data=data.to_dict(orient='records'),
                columns=[
                    {'name': 'Network', 'id': 'network', 'type': 'text'},
                    {'name': 'Timestamp', 'id': 'timestamp', 'type': 'datetime'},
                    {'name': 'Option Type', 'id': 'optionType', 'type': 'text'},
                    {'name': 'Exercise Type', 'id': 'exerciseType', 'type': 'text'},
                    {'name': 'Underlying Asset', 'id': 'underlyingAsset', 'type': 'text'},
                    {'name': 'Strike Asset', 'id': 'strikeAsset', 'type': 'text'},
                    {'name': 'Strike Price', 'id': 'strikePrice', 'type': 'number', 'format': Format(group=True, groups=[3])},
                    {'name': 'Expiration', 'id': 'expiration', 'type': 'datetime'},
                ],
                style={
                    'text-align': 'left',
                    'min-width': '5vw'
                }
            ),
    
            bar_chart(data=data['underlyingAsset'] + ':' + data['strikeAsset'], name='Pool Count'),
            
        ]
    
    else:
        return no_data_error(top='8vw', left='43.5vw')
    

def update_pods_finance_options_table_and_graphs():
    data = queries.pods_finance_options()
    # data.drop(labels=['protocol', 'option'], axis=1, inplace=True)
    if not data.empty:
        return [
            
            small_table(
                data=data.to_dict(orient='records'),
                columns=[
                    {'name': 'Network', 'id': 'network', 'type': 'text'},
                    {'name': 'Timestamp', 'id': 'timestamp', 'type': 'datetime'},
                    {'name': 'Option Type', 'id': 'optionType', 'type': 'text'},
                    {'name': 'Exercise Type', 'id': 'exerciseType', 'type': 'text'},
                    {'name': 'Underlying Asset', 'id': 'underlyingAsset', 'type': 'text'},
                    {'name': 'Strike Asset', 'id': 'strikeAsset', 'type': 'text'},
                    {'name': 'Strike Price', 'id': 'strikePrice', 'type': 'number', 'format': Format(group=True, groups=[3])},
                    {'name': 'Expiration', 'id': 'expiration', 'type': 'datetime'},
                ],
                style={
                    'text-align': 'left',
                    'min-width': '5vw'
                },
                style_conditional=[
                    {
                        'if': {'column_id': 'action'},
                        'width': '3.25vw',
                        'min-width': '3.25vw',
                        'max-width': '3.25vw',
                    },
                ]
            ),
    
            bar_chart(data=data['underlyingAsset'] + ':' + data['strikeAsset'], name='Option Count'),
            pie_chart(data=data['network']),
            pie_chart(data=data['exerciseType']),
            pie_chart(data=data['optionType']),
            pie_chart(data=queries.pods_finance_actions())
        ]

    else:
        return no_data_error(top='8vw', left='43.5vw')


def update_synthetix_options_table_and_graphs():
    data = queries.synthetix_exchanges()
    data.drop(labels=['network', 'protocol', 'transaction'], axis=1, inplace=True)
    data[['fromAmount', 'toAmount']] = data[['fromAmount', 'toAmount']].astype(float).round(2)
    if not data.empty:
        return [
        
            small_table(
                data=data.to_dict(orient='records'),
                columns=[
                    {'name': 'Timestamp', 'id': 'timestamp', 'type': 'datetime'},
                    {'id': 'fromToken', 'name': 'From Token', 'type': 'text'},
                    {'id': 'toToken', 'name': 'To Token', 'type': 'text'},
                    {'id': 'fromAmount', 'name': 'From Amount', 'type': 'number'},
                    {'id': 'toAmount', 'name': 'To Amount', 'type': 'number'},
                    {'id': 'fromAmountUSD', 'name': 'From Amount (USD)', 'type': 'number', 'format': FormatTemplate.money(0)},
                    {'id': 'toAmountUSD', 'name': 'To Amount (USD)', 'type': 'number', 'format': FormatTemplate.money(0)},
                ],
                style={
                    'text-align': 'left',
                    'min-width': '5vw'
                },
                style_conditional=[
                    {
                        'if': {'column_id': 'action'},
                        'width': '3.25vw',
                        'min-width': '3.25vw',
                        'max-width': '3.25vw',
                    },
                ]
            ),
            
            bar_chart(data=data['fromToken'] + '->' + data['toToken'], name='Exchange Count')
            
        ]


def pie_chart(data):
    data = data.value_counts().sort_index()
    
    layout = dict(
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            x=0,
            y=1.3,
            orientation='h',
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=8,
            ),
        ),
        margin=dict(t=40, b=10, l=10, r=10),
        font=dict(
            family='Helvetica',
            color='#292B52',
            size=8,
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
        ),
    )
    
    traces = go.Pie(
        labels=data.index,
        values=data.values,
        hole=0.6,
        marker=dict(
            colors=['rgba(68, 180, 40, 0.4)', 'rgba(222, 79, 65, 0.4)']
        ),
        textfont=dict(
            family='Helvetica',
            color='#292B52',
            size=6
        ),
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


def bar_chart(data, name, num=10):
    data = data.value_counts().sort_values().iloc[-num:]

    layout = dict(
        hovermode='y unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=30, b=10, l=10, r=10),
        font=dict(
            family='Helvetica',
            color='#292B52',
            size=8,
        ),
        xaxis=dict(
            color='#667085',
            title=dict(
                text=name,
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
        yaxis=dict(
            type='category',
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
        hoverlabel=dict(
            bgcolor='#ffffff',
            bordercolor='#d9d9d9',
            namelength=-1,
            font=dict(
                family='Helvetica',
                color='#292B52',
                size=6
            ),
        ),
        bargap=0.5
    )

    traces = go.Bar(
        y=data.index,
        x=data.values,
        name=name,
        orientation='h',
        marker=dict(
            color='rgba(243, 158, 30, 0.1)',
            line=dict(
                color='rgb(243, 158, 30)',
                width=1,
            )
        ),
        hovertemplate='%{x}'
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
