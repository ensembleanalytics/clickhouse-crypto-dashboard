from dash import html, dcc

from utils.frontend import page_header, section_header

def exchanges_layout(exchange):
	
	return html.Div(
		
		children=[
			
			page_header(exchange + ' Overview'),
			
			# Top pairs by volume
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Top Pairs by Volume'),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='top-pairs-by-volume-table-container',
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
									
									section_header(exchange + ' Total Volume'),
									
									dcc.Loading(
										children=[
											html.Div(
												id='total-volume-figure-container',
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
			
			# Top pairs by liquidity
			html.Div(
				children=[
					
					html.Div(
						children=[
							
							html.Div(
								children=[
									
									section_header('Top Pairs by Liquidity'),
									
									dcc.Loading(
										children=[
											
											html.Div(
												id='top-pairs-by-liquidity-table-container',
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
									
									section_header(exchange + ' Total Liquidity'),
									
									dcc.Loading(
										children=[
											html.Div(
												id='total-liquidity-figure-container',
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


