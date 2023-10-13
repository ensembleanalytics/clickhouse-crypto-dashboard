import pandas as pd
import dash_core_components as dcc
from dash_table import FormatTemplate
from dash_table.Format import Format, Scheme, Sign

import queries.exchanges as queries
from utils.frontend import no_data_error, line_chart, small_table

def calculate_level(data, column, days):
    data = data.set_index('timestamp').groupby(by='pair').rolling(window=days, min_periods=1).sum()
    return data.groupby(by=['pair'])[column].last()


def calculate_change(data, column, days):
    data = data.set_index(['pair', 'timestamp']).groupby(by='pair').pct_change(periods=days)
    return data.groupby(by=['pair'])[column].last()


def update_top_pairs_by_volume_tables_and_graphs(pathname):
    protocol = pathname.split(sep='/')[-1]
    data = queries.volume_data(protocol)

    if not data.empty:
        
        table = pd.DataFrame({
            'DEX': protocol,
            'Volume (1d)': calculate_level(data, column='volume', days=1),
            'Volume (7d)': calculate_level(data, column='volume', days=7),
            'Volume (1d change)': calculate_change(data, column='volume', days=1),
            'Volume (7d change)': calculate_change(data, column='volume', days=7),
        })
    
        table = table.sort_values(by='Volume (1d)', ascending=False)
        table = table.reset_index().rename(columns={'pair': 'Pair'})
        table['Pair'] = table['Pair'].apply(lambda x: '[' + x + ']' + '(/Home/DEX/' + protocol + '/' + x + '-Pair)')
        table = volume_table(table)
    
        data = data.groupby(by='timestamp')['volume'].sum().reset_index()
        data = data.sort_values(by='timestamp').reset_index(drop=True)
        figure = volume_figure(data, protocol)
    
        return [table, figure]

    else:
        return 2 * [no_data_error(top='8vw', left='20vw')]


def update_top_pairs_by_liquidity_tables_and_graphs(pathname):
    protocol = pathname.split(sep='/')[-1]
    data = queries.liquidity_data(protocol)

    if not data.empty:
    
        table = pd.DataFrame({
            'DEX': protocol,
            'Liquidity (1d)': calculate_level(data, column='liquidity', days=1),
            'Liquidity (7d)': calculate_level(data, column='liquidity', days=7),
            'Liquidity (1d change)': calculate_change(data, column='liquidity', days=1),
            'Liquidity (7d change)': calculate_change(data, column='liquidity', days=7),
        })
    
        table = table.sort_values(by='Liquidity (1d)', ascending=False)
        table = table.reset_index().rename(columns={'pair': 'Pair'})
        table['Pair'] = table['Pair'].apply(lambda x: '[' + x + ']' + '(/Home/DEX/' + protocol + '/' + x + '-Pair)')
        table = liquidity_table(table)
    
        data = data.groupby(by='timestamp')['liquidity'].sum().reset_index()
        data = data.sort_values(by='timestamp').reset_index(drop=True)
        figure = liquidity_figure(data, protocol)
    
        return [table, figure]

    else:
        return 2 * [no_data_error(top='8vw', left='20vw')]


def volume_table(data):
    money = FormatTemplate.money(0)
    percentage = Format(scheme=Scheme.percentage, precision=2, sign=Sign.positive)
    
    columns = [
        {'name': 'DEX', 'id': 'DEX', 'type': 'text'},
        {'name': 'Pair', 'id': 'Pair', 'type': 'text', 'presentation': 'markdown'},
        {'name': 'Volume (1d)', 'id': 'Volume (1d)', 'type': 'numeric', 'format': money},
        {'name': 'Volume (7d)', 'id': 'Volume (7d)', 'type': 'numeric', 'format': money},
        {'name': 'Volume (1d change)', 'id': 'Volume (1d change)', 'type': 'numeric', 'format': percentage},
        {'name': 'Volume (7d change)', 'id': 'Volume (7d change)', 'type': 'numeric', 'format': percentage},
    ]
    
    data = data.to_dict(orient='records')
    
    style = {
        'text-align': 'left',
    }
    
    style_conditional = []
    
    for x in ['Volume (1d change)', 'Volume (7d change)']:
        style_conditional.extend([
            {
                'if': {
                    'column_id': x,
                    'filter_query': '{' + x + '} < 0',
                },
                'color': '#de4f41'
            },
            {
                'if': {
                    'column_id': x,
                    'filter_query': '{' + x + '} > 0',
                },
                'color': '#44B428'
            }
        ])
    
    style_conditional.extend([
        {
            'if': {'column_id': 'DEX'},
            'width': '3vw',
            'min-width': '3vw',
            'max-width': '3vw',
        },
        {
            'if': {'column_id': 'Pair'},
            'width': '4vw',
            'min-width': '4vw',
            'max-width': '4vw',
        },
        {
            'if': {'column_id': 'Volume (1d)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        },
        {
            'if': {'column_id': 'Volume (7d)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        },
        {
            'if': {'column_id': 'Volume (1d change)'},
            'width': '6vw',
            'min-width': '6vw',
            'max-width': '6vw',
        },
        {
            'if': {'column_id': 'Volume (7d change)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        },
    ])
    
    return small_table(
        data=data,
        columns=columns,
        style=style,
        style_conditional=style_conditional
    )


def liquidity_table(data):
    money = FormatTemplate.money(0)
    percentage = Format(scheme=Scheme.percentage, precision=2, sign=Sign.positive)
    
    columns = [
        {'name': 'DEX', 'id': 'DEX', 'type': 'text'},
        {'name': 'Pair', 'id': 'Pair', 'type': 'text', 'presentation': 'markdown'},
        {'name': 'Liquidity (1d)', 'id': 'Liquidity (1d)', 'type': 'numeric', 'format': money},
        {'name': 'Liquidity (7d)', 'id': 'Liquidity (7d)', 'type': 'numeric', 'format': money},
        {'name': 'Liquidity (1d change)', 'id': 'Liquidity (1d change)', 'type': 'numeric', 'format': percentage},
        {'name': 'Liquidity (7d change)', 'id': 'Liquidity (7d change)', 'type': 'numeric', 'format': percentage},
    ]
    
    data = data.to_dict(orient='records')
    
    style = {
        'text-align': 'left',
    }
    
    style_conditional = []
    
    for x in ['Liquidity (1d change)', 'Liquidity (7d change)']:
        style_conditional.extend([
            {
                'if': {
                    'column_id': x,
                    'filter_query': '{' + x + '} < 0',
                },
                'color': '#de4f41'
            },
            {
                'if': {
                    'column_id': x,
                    'filter_query': '{' + x + '} > 0',
                },
                'color': '#44B428'
            }
        ])
    
    style_conditional.extend([
        {
            'if': {'column_id': 'DEX'},
            'width': '3vw',
            'min-width': '3vw',
            'max-width': '3vw',
        },
        {
            'if': {'column_id': 'Pair'},
            'width': '4vw',
            'min-width': '4vw',
            'max-width': '4vw',
        },
        {
            'if': {'column_id': 'Liquidity (1d)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        },
        {
            'if': {'column_id': 'Liquidity (7d)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        },
        {
            'if': {'column_id': 'Liquidity (1d change)'},
            'width': '6vw',
            'min-width': '6vw',
            'max-width': '6vw',
        },
        {
            'if': {'column_id': 'Liquidity (7d change)'},
            'width': '5vw',
            'min-width': '5vw',
            'max-width': '5vw',
        }
    ])
    
    return small_table(
        data=data,
        columns=columns,
        style=style,
        style_conditional=style_conditional
    )


def volume_figure(data, protocol):
    return dcc.Graph(
        figure=line_chart(
            data=data,
            x='timestamp',
            y='volume',
            name=protocol + ' Total Volume',
            tickformat='$,.0f'
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


def liquidity_figure(data, protocol):
    return dcc.Graph(
        figure=line_chart(
            data=data,
            x='timestamp',
            y='liquidity',
            name=protocol + ' Total Liquidity',
            tickformat='$,.0f'
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
