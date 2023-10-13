from dash import html, dcc

from utils.frontend import page_header, section_header

def derivatives_layout(protocol):
    
    if protocol == 'Pods Finance':
        return pods_finance_overview
    
    elif protocol == 'Synthetix':
        return synthetix_overview
    
    else:
        return html.Div(
            
            children=[
                
                page_header(protocol + ' Overview'),
                
                html.Div(
                    children=[
                        
                        html.Div(
                            children=[
                                
                                section_header(protocol + ' Data'),
                                
                                dcc.Loading(
                                    children=[
                                        
                                        html.Div(
                                            id='protocol-data',
                                            style={
                                                'display': 'block',
                                                'width': '100%',
                                                'height': '33vw',
                                            }
                                        )
                                    
                                    ],
                                    color='rgba(128, 60, 138, 0.2)',
                                ),
                            
                            ],
                            style={
                                'padding': '1vw 1vw 1vw 1vw',
                                'height': '33vw',
                            }
                        ),
                    ],
                    
                    className='card',
                    
                    style={
                        'display': 'block',
                        'margin': '1vw 3.5vw 1vw 3.5vw',
                    }
                ),
            ]
        )


synthetix_overview = html.Div(
    
    children=[
        
        page_header('Synthetix Overview'),
    
        html.Div(
            children=[
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Exchanges'),
                            
                                dcc.Loading(
                                    children=[
                                    
                                        html.Div(
                                            id='synthetix-exchanges-table',
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
                    className='card'
                ),
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Top Pairs'),
                            
                                dcc.Loading(
                                    children=[
                                        html.Div(
                                            id='synthetix-top-pairs-figure',
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
    
    ]
)


pods_finance_overview = html.Div(
        
    children=[
        
        page_header('Pods Finance Overview'),
    
        html.Div(
            children=[
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Pools'),
                            
                                dcc.Loading(
                                    children=[
                                    
                                        html.Div(
                                            id='pods-pools-table',
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
                    className='card'
                ),
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Options'),
                            
                                dcc.Loading(
                                    children=[
                                        html.Div(
                                            id='pods-options-table',
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
    
        html.Div(
            children=[
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Top Pool Assets'),
                            
                                dcc.Loading(
                                    children=[
                                    
                                        html.Div(
                                            id='pods-pool-assets-figure',
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
                    className='card'
                ),
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Top Option Assets'),
                            
                                dcc.Loading(
                                    children=[
                                        html.Div(
                                            id='pods-option-assets-figure',
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
    
        html.Div(
            children=[
    
                html.Div(
                    children=[
            
                        html.Div(
                            children=[
                    
                                section_header('Option Network'),
                    
                                dcc.Loading(
                                    children=[
                            
                                        html.Div(
                                            id='pods-option-network-figure',
                                            style={
                                                'display': 'block',
                                                'width': '19.75vw',
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
                    className='card'
                ),
    
                html.Div(
                    children=[
            
                        html.Div(
                            children=[
                    
                                section_header('Option Exercise Type'),
                    
                                dcc.Loading(
                                    children=[
                            
                                        html.Div(
                                            id='pods-exercise-type-figure',
                                            style={
                                                'display': 'block',
                                                'width': '19.75vw',
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
                
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Option Type'),
                            
                                dcc.Loading(
                                    children=[
                                    
                                        html.Div(
                                            id='pods-option-type-figure',
                                            style={
                                                'display': 'block',
                                                'width': '19.75vw',
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
            
                html.Div(
                    children=[
                    
                        html.Div(
                            children=[
                            
                                section_header('Option Action'),
                            
                                dcc.Loading(
                                    children=[
                                        html.Div(
                                            id='pods-option-action-figure',
                                            style={
                                                'display': 'block',
                                                'width': '19.75vw',
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
    ]
)