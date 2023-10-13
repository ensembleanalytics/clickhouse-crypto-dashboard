import plotly.graph_objects as go
from dash import html
from dash.dash_table import DataTable

def page_header(text):
    return html.Div(
        children=[
            html.Div(
                children=text,
                style={
                    'font-size': '0.9vw',
                    'line-height': '0.9vw',
                    'font-weight': '400',
                    'color': 'white',
                    'padding': '0.75vw 0.5vw 0.75vw 0.5vw',
                }
            ),
        ],
        style={
            'display': 'flex',
            'background': 'linear-gradient(90deg, #C569CF 0%, #EE609C 100%)',
            'margin': '1vw 3.5vw 1vw 3.5vw',
            'padding': '0',
            'border-radius': '0.5rem',
        }
    )


def section_header(text):
    return html.Div(
        children=[
            
            html.Div(
                children=[' '],
                style={
                    'position': 'absolute',
                    'width': '1.25vw',
                    'height': '1.25vw',
                    'border-radius': '50%',
                    'background': 'linear-gradient(263.97deg, #803C8A 16.56%, #FFCDCE 274.83%)',
                    'opacity': '0.1',
                    'display': 'inline-block',
                }
            ),
            
            html.Div(
                children=text,
                style={
                    'font-size': '0.8vw',
                    'line-height': '0.8vw',
                    'font-weight': '500',
                    'color': '#292B52',
                    'display': 'inline-block',
                    'margin': '0.25vw 0vw 1vw 1.75vw',
                }
            ),
        
        ],
        
        style={
            'display': 'flex'
        }
    )


def menu(tables, section, style):
    tables = tables[tables['section'] == section].copy()
    
    children = []
    for category in tables['category'].unique():
        children.extend([
            html.Div(
                children=[
                    html.Div(
                        children=category,
                        className='menu-title'
                    ),
                    html.Div(
                        children=[
                            menu_item(
                                text=x,
                                icon='/assets/img/' + x + '.png',
                                href='/Home/' + category + '/' + x.replace(' ', '-')
                            ) for x in tables.loc[tables['category'] == category, 'protocol'].unique()
                        ]
                    ),
                ],
                className='menu-section'
            ),
        ])
    
    return html.Div(
        children=children,
        className='navbar-menu',
        style=style
    )


def menu_item(icon, text, href=None):
    return html.A(
        href=href,
        children=[
    
            html.Img(
                src=icon,
                className='menu-icon',
                style={
                    'width': '0.9vw',
                    'height': '0.9vw',
                    'display': 'inline-block',
                    'vertical-align': 'middle',
                }
            ),
            
            html.Div(
                children=text,
                style={
                    'display': 'inline-block',
                    'vertical-align': 'middle',
                    'margin-left': '0.25vw',
                }
            )
        
        ],
        className='menu-item'
    )


def url_item(text, href=None, active=False):
    return html.A(
        href=href,
        children=text,
        className='url-item-active' if active else 'url-item',
    )


def no_data_error(top, left):
    return html.Div(
        children='No Data',
        style={
            'position': 'relative',
            'top': top,
            'left': left,
            'color': 'rgba(102, 112, 133, 0.75)',
            'font-weight': '500',
            'font-size': '0.8vw',
        }
    )


def line_chart(data, x, y, name, axistitle='', tickformat='', mode='lines'):
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
            range=[0.98 * data[y].min(), 1.02 * data[y].max()],
            color='#667085',
            title=dict(
                text=axistitle,
                font=dict(
                    family='Helvetica',
                    color='#667085',
                    size=8
                ),
            ),
            tickformat=tickformat,
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
    
    traces = go.Scatter(
        x=data[x],
        y=data[y],
        name=name,
        showlegend=False,
        mode=mode,
        fill='tozeroy',
        fillcolor='rgba(243, 158, 30, 0.1)',
        marker=dict(
            color='rgba(243, 158, 30, 0.1)',
            line=dict(
                width=1,
                color='rgb(243, 158, 30)',
            ),
        ),
        line=dict(
            width=1,
            color='rgb(243, 158, 30)',
            shape='spline'
        ),
        hovertemplate='%{y}'
    )
    
    return go.Figure(data=traces, layout=layout)


def small_table(data, columns, style, style_conditional=[], page_size=8):
    return DataTable(
        data=data,
        columns=columns,
        sort_action='native',
        page_action='native',
        page_size=page_size,
        style_table={
            'width': 'auto',
            'max-height': '19vw',
            'overflow-y': 'auto',
            'overflow-x': 'auto',
            'text-align': 'left',
            'margin-top': '0.5vw'
        },
        fixed_rows={'headers': True, 'data': 0},
        style_cell=style,
        style_data=style,
        style_cell_conditional=style_conditional,
        style_data_conditional=style_conditional,
        markdown_options={'link_target': '_self'}
    )


def large_table(data, columns, style, style_conditional=[], page_size=15):
    return DataTable(
        data=data,
        columns=columns,
        sort_action='native',
        page_action='native',
        page_size=page_size,
        style_table={
            'width': 'auto',
            'max-height': '27vw',
            'overflow-y': 'auto',
            'overflow-x': 'auto',
            'text-align': 'left',
            'margin-top': '0.5vw'
        },
        fixed_rows={'headers': True, 'data': 0},
        style_cell=style,
        style_data=style,
        style_cell_conditional=style_conditional,
        style_data_conditional=style_conditional,
        markdown_options={'link_target': '_self'}
    )
