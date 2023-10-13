from dash import html, dcc

from utils.frontend import page_header

data_layout = html.Div(
    children=[
    
        page_header('Data'),
        
        html.Div(
            children=[
                
                html.Div(
                    children=[
                        
                        dcc.Dropdown(
                            id='data-table-dropdown-1',
                            multi=False,
                            searchable=False,
                            clearable=False
                        ),

                    ],
                    style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'width': '10vw'
                    }
                ),
    
                html.Div(
                    children=[
    
                        dcc.Dropdown(
                            id='data-table-dropdown-2',
                            multi=False,
                            searchable=True,
                            clearable=False
                        ),

                    ],
                    style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'width': '10vw',
                        'margin-left': '1vw'
                    }
                ),
    
                html.Div(
                    children=[
        
                        dcc.Dropdown(
                            id='data-table-dropdown-3',
                            multi=False,
                            searchable=False,
                            clearable=False
                        ),

                    ],
                    style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'width': '10vw',
                        'margin-left': '1vw'
                    }
                ),
    
                html.Div(
                    children=[

                        dcc.Input(
                            id='data-window-input',
                            type='number',
                            min=1,
                            value=5,
                            debounce=True,
                            style={'width': '8vw'}
                        ),

                    ],
                    style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '0vw 1vw 0vw 44vw'
                    }
                ),
    
                html.Div(
                    children=[
                
                        dcc.Dropdown(
                            id='data-window-dropdown',
                            options=[
                                {'value': 'seconds', 'label': 'Seconds'},
                                {'value': 'minutes', 'label': 'Minutes'},
                                {'value': 'hours', 'label': 'Hours'},
                                {'value': 'days', 'label': 'Days'},
                                {'value': 'months', 'label': 'Months'},
                                {'value': 'years', 'label': 'Years'},
                            ],
                            value='days',
                            multi=False,
                            searchable=False,
                            clearable=False
                        ),

                    ],
                    style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'width': '8vw',
                    }
                ),
                
            ],
            className='row',
            style={
                'margin': '1vw 3.5vw 1vw 3.5vw',
            }
        ),
    
        html.Div(
            children=[
            
                html.Div(
                    children=[
                    
                        html.Div(
                            id='data-table-header'
                        ),
                        
                        dcc.Loading(
                            children=[
                            
                                html.Div(
                                    id='data-table-container',
                                    style={
                                        'display': 'block',
                                        'width': '100%',
                                        'height': '33vw',
                                    }
                                )
                        
                            ],
                            color='rgba(128, 60, 138, 0.2)',
                        ),
    
                        dcc.Store(
                            id='data-storage',
                            storage_type='session'
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
                'margin': '1vw 3.5vw 0vw 3.5vw',
            }
        ),
        
        html.Div(
            children=html.Img(
                src='/assets/icon/connection.png',
                style={
                    'margin-left': '46.5vw',
                    'height': '2.5vw',
                }
            ),
            style={
                'width': '100%',
                'display': 'block',
                'height': '2.5vw',
                'margin': '0vw 3.5vw 0vw 3.5vw',
            }
        ),
        
        html.Div(
            children=[
            
                html.Div(
                    children=[
    
                        html.Div(
                            children=[
                                
                                html.Div(
                                    children=[
                    
                                        dcc.Dropdown(
                                            id='data-figure-dropdown-1',
                                            multi=False,
                                            searchable=False,
                                            clearable=False
                                        ),
                
                                    ],
                                    style={
                                        'display': 'inline-block',
                                        'vertical-align': 'middle',
                                        'width': '10vw'
                                    }
                                ),
            
                                html.Div(
                                    children=[
                    
                                        dcc.Dropdown(
                                            id='data-figure-dropdown-2',
                                            multi=False,
                                            searchable=False,
                                            clearable=False
                                        ),
                
                                    ],
                                    style={
                                        'display': 'inline-block',
                                        'vertical-align': 'middle',
                                        'width': '10vw',
                                        'margin-left': '1vw'
                                    }
                                ),
    
                                html.Div(
                                    children=[
            
                                        dcc.Dropdown(
                                            id='data-figure-dropdown-3',
                                            multi=False,
                                            searchable=False,
                                            clearable=False
                                        ),
        
                                    ],
                                    style={
                                        'display': 'inline-block',
                                        'vertical-align': 'middle',
                                        'width': '10vw',
                                        'margin-left': '1vw'
                                    }
                                ),
        
                            ],
                            className='row',
                        ),
                        
                        dcc.Loading(
                            children=[
                            
                                html.Div(
                                    id='data-figure-container',
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
                'margin': '0vw 3.5vw 1vw 3.5vw',
            }
        ),
    
    ]
)