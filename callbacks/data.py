import json
import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc

from queries.data import query_data
import utils.database as database


def update_data_table_dropdown_1():
    data = database.tables['category'].unique().tolist()
    options = [{'value': x, 'label': x} for x in data]
    value = data[0]
    return [options, value]


def update_data_table_dropdown_2(category):
    data = database.tables.loc[database.tables['category'] == category, 'protocol'].unique().tolist()
    options = [{'value': x, 'label': x} for x in data]
    value = data[0]
    return [options, value]


def update_data_table_dropdown_3(category, protocol):
    data = database.tables.loc[(database.tables['category'] == category) & (database.tables['protocol'] == protocol), ['description', 'table']].drop_duplicates()
    options = [{'value': x[1][1], 'label': x[1][0]} for x in data.iterrows()]
    value = data['table'].values[0]
    return [options, value]


def update_data_table(table, protocol, interval, units):
    return query_data(table, protocol, interval, units)


def update_data_figure_dropdown_1(data):
    if data is not None:
        
        numerical, categorical, timestamp = json.loads(data[0]), json.loads(data[1]), json.loads(data[2])
        
        if numerical != [] and categorical != [] and 'timestamp' in timestamp:
            options = [
              {'value': 'Histogram', 'label': 'Histogram'},
              {'value': 'Time Series', 'label': 'Time Series'},
            ]
            value = 'Time Series'
            return [options, value]
        
        elif categorical != []:
            options = [
              {'value': 'Histogram', 'label': 'Histogram'},
            ]
            value = 'Histogram'
            return [options, value]
        
        else:
            raise dash.exceptions.PreventUpdate

    else:
        raise dash.exceptions.PreventUpdate


def update_data_figure_dropdown_2(graph, data):
    if data is not None:
        numerical, categorical, timestamp = json.loads(data[0]), json.loads(data[1]), json.loads(data[2])
        
        if graph == 'Time Series':
            options = [{'value': x, 'label': x} for x in numerical]
            value = numerical[0]
            return [options, value]
        
        elif graph == 'Histogram':
            options = [{'value': x, 'label': x} for x in categorical]
            value = categorical[0]
            return [options, value]
        
        else:
            raise dash.exceptions.PreventUpdate
    else:
        raise dash.exceptions.PreventUpdate
    

def update_data_figure_dropdown_3(graph):
    if graph == 'Time Series':
        options = [
            {'value': 'S', 'label': 'Bucketing by Second'},
            {'value': 'T', 'label': 'Bucketing by Minute'},
            {'value': 'H', 'label': 'Bucketing by Hour'},
            {'value': 'D', 'label': 'Bucketing by Day'},
            {'value': 'W', 'label': 'Bucketing by Week'},
            {'value': 'M', 'label': 'Bucketing by Month'},
        ]
        value = 'D'
        return [options, value]
    
    elif graph == 'Histogram':
        options = [
            {'value': 'Count', 'label': 'Count'},
            {'value': 'Frequency', 'label': 'Frequency'},
        ]
        value = 'Count'
        return [options, value]
    
    else:
        raise dash.exceptions.PreventUpdate

    
def update_data_figure(graph, column, aggregation, data):
    if data is not None:
        numerical, categorical = json.loads(data[0]), json.loads(data[1])
        data = pd.read_json(data[3], orient='records')
        data[numerical] = data[numerical].astype(float)
        data[categorical] = data[categorical].astype(str).apply(lambda x: ['N/A' if y == '' else y for y in x])
        
        if graph == 'Time Series':
            data = data.set_index('timestamp').resample(aggregation)[[column]].agg(['min', 'max', 'mean']).fillna(method='ffill')
            data.columns = ['min', 'max', 'avg']
            data.reset_index(inplace=True, drop=False)
    
            layout = dict(
                hovermode='x',
                plot_bgcolor='white',
                paper_bgcolor='white',
                margin=dict(t=30, b=10, l=10, r=10),
                font=dict(
                    family='Helvetica',
                    color='#292B52',
                    size=8,
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
                    title=dict(
                        font=dict(
                            family='Helvetica',
                            color='#667085',
                            size=8
                        ),
                    ),
                    minexponent=9,
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
            )
    
            traces = []
    
            traces.append(
                go.Scatter(
                    x=data['timestamp'],
                    y=data['max'],
                    showlegend=False,
                    mode='lines',
                    line=dict(
                        width=0,
                        color='rgb(243, 158, 30)',
                        shape='spline'
                    ),
                    hovertemplate='Maximum: %{y}<extra></extra>'
                )
            )
            
            traces.append(
                go.Scatter(
                    x=data['timestamp'],
                    y=data['min'],
                    showlegend=False,
                    mode='lines',
                    fill='tonexty',
                    fillcolor='rgba(243, 158, 30, 0.1)',
                    line=dict(
                        width=0,
                        color='rgb(243, 158, 30)',
                        shape='spline'
                    ),
                    hovertemplate='Minimum: %{y}<extra></extra>'
                )
            )
    
            traces.append(
                go.Scatter(
                    x=data['timestamp'],
                    y=data['avg'],
                    showlegend=False,
                    mode='lines',
                    line=dict(
                        width=2,
                        color='rgb(243, 158, 30)',
                        shape='spline',
                        dash='dot'
                    ),
                    hovertemplate='Average: %{y}<extra></extra>'
                )
            )
    
        else:
            
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
                    tickformat='%' if aggregation == 'Frequency' else '',
                    title=dict(
                        text=aggregation,
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
            
            traces = go.Histogram(
                y=data[column],
                name=aggregation,
                histnorm='probability' if aggregation == 'Frequency' else '',
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
                'height': '90%',
                'width': '100%'
            }
        )
    else:
        raise dash.exceptions.PreventUpdate
