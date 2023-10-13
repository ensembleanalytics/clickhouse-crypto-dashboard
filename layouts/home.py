from dash import html, dcc

from utils.frontend import page_header, section_header

home_layout = html.Div(
    children=[
        
        page_header('Overview'),
        
        html.Div(
            children=[
                
                dcc.Store(
                    id='total-value-locked-storage',
                    storage_type='session'
                ),
                
                html.Div(
                    children=[
    
                        html.Div(
                            children=[
                                
                                section_header('Total Value Locked'),
                            ],
                            className='row'
                        ),
                        
                        html.Div(
                            children=[
    
                                html.Div(
                                    children=[
            
                                        html.Button(
                                            children=['All'],
                                            id='all-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['DEX'],
                                            id='dex-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['Derivatives'],
                                            id='derivatives-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['Lending'],
                                            id='lending-total-value-locked',
                                        ),
        
                                    ],
                                    className='row',
                                    style={'margin-bottom': '1vw'}
                                ),
    
                                dcc.Loading(
                                    children=[
            
                                        html.Div(
                                            id='total-value-locked-table-container',
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
                                'display': 'inline-block',
                                'vertical-align': 'top',
                                'width': '43.5vw',
                            }
                        ),
    
                        html.Div(
                            children=[
    
                                html.Div(
                                    children=[
            
                                        html.Button(
                                            children=['1d'],
                                            id='1d-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['7d'],
                                            id='7d-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['1m'],
                                            id='1m-total-value-locked',
                                        ),
            
                                        html.Button(
                                            children=['3m'],
                                            id='3m-total-value-locked',
                                        ),
        
                                    ],
                                    className='row'
                                ),
    
                                dcc.Loading(
                                    children=[
            
                                        html.Div(
                                            id='total-value-locked-figure-container',
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
                                'display': 'inline-block',
                                'vertical-align': 'top',
                                'width': '43.5vw',
                                'margin-left': '2vw',
                            }
                        ),
                    
                    ],
                    style={
                        'padding': '1vw 1vw 1vw 1vw',
                        'height': '23vw',
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
            children=[
            
                html.Div(
                    children=[
                        
                        section_header('Top Performing Pools'),
    
                        dcc.Loading(
                            children=[
            
                                html.Div(
                                    id='top-pools-table-container',
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