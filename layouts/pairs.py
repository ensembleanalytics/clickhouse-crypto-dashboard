from dash import html, dcc

from utils.frontend import page_header, section_header

def pair_layout(pair):
    return html.Div(
        children=[
            
            page_header(pair + ' Pair'),
    
            html.Div(
                children=[
                    
                    # Transactions table
                    html.Div(
                        children=[
                            
                            html.Div(
                                children=[
        
                                    section_header('Transactions Details'),
                            
                                    dcc.Loading(
                                        children=[
                                    
                                            html.Div(
                                                id='pair-transactions-table-container',
                                                style={
                                                    'display': 'block',
                                                    'width': '43.5vw',
                                                    'height': '20.5vw',
                                                }
                                            )
                                
                                        ],
                                        color='rgba(128, 60, 138, 0.2)',
                                    ),
                                    
                                ],
                                style={
                                    'padding': '1vw 1vw 1vw 1vw',
                                    'height': '22vw',
                                }
                            ),
                        ],
                        className='card',
                    ),
            
                    # Transactions figure
                    html.Div(
                        children=[
                    
                            html.Div(
                                children=[
                            
                                    section_header('Transactions Breakdown'),
    
                                    html.Div(
                                        children=[
            
                                            html.Button(
                                                children=['Value'],
                                                id='pair-transactions-value',
                                            ),
            
                                            html.Button(
                                                children=['Count'],
                                                id='pair-transactions-count',
                                            ),
        
                                        ],
                                        className='row'
                                    ),
                                    
                                    dcc.Loading(
                                        children=[
                                    
                                            html.Div(
                                                id='pair-transactions-figure-container',
                                                style={
                                                    'display': 'block',
                                                    'width': '43.5vw',
                                                    'height': '19vw',
                                                }
                                            )
                                
                                        ],
                                        color='rgba(128, 60, 138, 0.2)',
                                    ),
                        
                                ],
                                style={
                                    'padding': '1vw 1vw 1vw 1vw',
                                    'height': '22vw',
                                }
                            ),
                        ],
                        className='card',
                        style={'margin-left': '2vw'}
                    ),
                ],
                style={
                    'display': 'flex',
                    'margin': '1vw 3.5vw 1vw 3.5vw',
                    'padding': '0',
                }
            ),
            
            html.Div(
                children=[
                    
                    # Volumes
                    html.Div(
                        children=[
                    
                            html.Div(
                                children=[
                            
                                    section_header('Volume'),
                            
                                    dcc.Loading(
                                        children=[
                                    
                                            html.Div(
                                                id='pair-volume-figure-container',
                                                style={
                                                    'display': 'block',
                                                    'width': '43.5vw',
                                                    'height': '20.5vw',
                                                }
                                            )
                                
                                        ],
                                        color='rgba(128, 60, 138, 0.2)',
                                    ),
                        
                                ],
                                style={
                                    'padding': '1vw 1vw 1vw 1vw',
                                    'height': '22vw',
                                }
                            ),
                        ],
                        className='card',
                    ),
            
                    # Liquidity
                    html.Div(
                        children=[
                    
                            html.Div(
                                children=[
                            
                                    section_header('Liquidity'),
                            
                                    dcc.Loading(
                                        children=[
                                    
                                            html.Div(
                                                id='pair-liquidity-figure-container',
                                                style={
                                                    'display': 'block',
                                                    'width': '43.5vw',
                                                    'height': '20.5vw',
                                                }
                                            )
                                
                                        ],
                                        color='rgba(128, 60, 138, 0.2)',
                                    ),
                        
                                ],
                                style={
                                    'padding': '1vw 1vw 1vw 1vw',
                                    'height': '22vw',
                                }
                            ),
                        ],
                        className='card',
                        style={'margin-left': '2vw'}
                    ),
                ],
                style={
                    'display': 'flex',
                    'margin': '1vw 3.5vw 1vw 3.5vw',
                    'padding': '0',
                }
            ),
    
            # Prices
            html.Div(
                children=[
            
                    html.Div(
                        children=[
                    
                            section_header('Price'),
                    
                            dcc.Loading(
                                children=[
                            
                                    html.Div(
                                        id='pair-prices-figure-container',
                                        style={
                                            'display': 'block',
                                            'width': '100%',
                                            'height': '19vw',
                                        }
                                    )
                        
                                ],
                                color='rgba(128, 60, 138, 0.2)',
                            ),
                
                        ],
                        style={
                            'padding': '1vw 1vw 1vw 1vw',
                            'height': '22vw',
                        }
                    ),
                ],
        
                className='card',
        
                style={
                    'display': 'block',
                    'margin': '1vw 3.5vw 1vw 3.5vw',
                }
            ),
            
        ],
    )
