from dash import html, dcc

from utils.frontend import page_header, section_header

def blockchains_layout(protocol):
	return html.Div(
		children=[
			
			page_header(protocol + ' Overview'),
			
			# Block numbers
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Blocks'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1d'],
												id='1d-block-numbers',
											),
											
											html.Button(
												children=['7d'],
												id='7d-block-numbers',
											),
											
											html.Button(
												children=['1m'],
												id='1m-block-numbers',
											),
											
											html.Button(
												children=['3m'],
												id='3m-block-numbers',
											),
											
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='block-numbers',
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
						className='card'
					),
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Daily Block Count'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1m'],
												id='1m-block-counts',
											),
											
											html.Button(
												children=['6m'],
												id='6m-block-counts',
											),
											
											html.Button(
												children=['1y'],
												id='1y-block-counts',
											),
											
											html.Button(
												children=['2y'],
												id='2y-block-counts',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='block-counts',
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
						style={
							'margin-left': '2vw'
						}
					),
				],
				style={
					'display': 'flex',
					'margin': '1vw 3.5vw 1vw 3.5vw',
					'padding': '0',
				}
			),
			
			# Block sizes
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Block Sizes'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1d'],
												id='1d-block-sizes',
											),
											
											html.Button(
												children=['7d'],
												id='7d-block-sizes',
											),
											
											html.Button(
												children=['1m'],
												id='1m-block-sizes',
											),
											
											html.Button(
												children=['3m'],
												id='3m-block-sizes',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='block-sizes',
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
						className='card'
					),
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Daily Average Block Size'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1m'],
												id='1m-daily-block-sizes',
											),
											
											html.Button(
												children=['6m'],
												id='6m-daily-block-sizes',
											),
											
											html.Button(
												children=['1y'],
												id='1y-daily-block-sizes',
											),
											
											html.Button(
												children=['2y'],
												id='2y-daily-block-sizes',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='daily-block-sizes',
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
						style={
							'margin-left': '2vw'
						}
					),
				],
				style={
					'display': 'flex',
					'margin': '1vw 3.5vw 1vw 3.5vw',
					'padding': '0',
				}
			),
			
			# Transactions
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Cumulative Transaction Count'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1d'],
												id='1d-cumulative-transactions',
											),
											
											html.Button(
												children=['7d'],
												id='7d-cumulative-transactions',
											),
											
											html.Button(
												children=['1m'],
												id='1m-cumulative-transactions',
											),
											
											html.Button(
												children=['3m'],
												id='3m-cumulative-transactions',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='cumulative-transactions',
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
						className='card'
					),
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Daily Transaction Count'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1m'],
												id='1m-daily-transactions',
											),
											
											html.Button(
												children=['6m'],
												id='6m-daily-transactions',
											),
											
											html.Button(
												children=['1y'],
												id='1y-daily-transactions',
											),
											
											html.Button(
												children=['2y'],
												id='2y-daily-transactions',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='daily-transactions',
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
						style={
							'margin-left': '2vw'
						}
					),
				],
				style={
					'display': 'flex',
					'margin': '1vw 3.5vw 1vw 3.5vw',
					'padding': '0',
				}
			),
			
			# Gas
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Daily Average Gas Limit'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1m'],
												id='1m-gas-limit',
											),
											
											html.Button(
												children=['6m'],
												id='6m-gas-limit',
											),
											
											html.Button(
												children=['1y'],
												id='1y-gas-limit',
											),
											
											html.Button(
												children=['2y'],
												id='2y-gas-limit',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='gas-limit',
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
						className='card'
					),

					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Daily Gas Used'),
									
									html.Div(
										children=[
											
											html.Button(
												children=['1m'],
												id='1m-gas-used',
											),
											
											html.Button(
												children=['6m'],
												id='6m-gas-used',
											),
											
											html.Button(
												children=['1y'],
												id='1y-gas-used',
											),
											
											html.Button(
												children=['2y'],
												id='2y-gas-used',
											),
										
										],
										className='row'
									),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='gas-used',
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
						style={
							'margin-left': '2vw'
						}
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