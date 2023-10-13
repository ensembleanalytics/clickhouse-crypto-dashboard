import dash
# import dash_auth
from dash import html, dcc, Input, Output, State
from flask import Flask

import callbacks.pairs as pairs_callbacks
import callbacks.exchanges as exchanges_callbacks
import callbacks.blockchains as blockchains_callbacks
import callbacks.derivatives as derivatives_callbacks
import callbacks.lending as lending_callbacks
import callbacks.data as data_callbacks
import callbacks.home as home_callbacks

import utils.frontend as frontend
import utils.backend as backend
# import utils.users as users
import utils.database as database

# App set-up
server = Flask(__name__)

app = dash.Dash(
    name=__name__,
    server=server,
    title='Timeflow Crypto',
    update_title=None,
    suppress_callback_exceptions=True,
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

application = app.server

# App log-in
# auth = dash_auth.BasicAuth(
#     app=app,
#     username_password_list=users.login
# )

# App layout
app.layout = html.Div(
    children=[

        # Updates
        dcc.Interval(
            id='interval',
            interval=60 * 60 * 1000,
            n_intervals=0,
        ),

        # Navbar
        html.Div(
            children=[

                html.Img(
                    src='/assets/timeflow-logo.png',
                    style={
                        'padding': '0.75vw 0vw 0.75vw 3.5vw',
                        'width': '5vw',
                        'display': 'inline-block',
                        'vertical-align': 'top'
                    }
                ),
    
                html.A(
                    children='Home',
                    id='home-tab',
                    className='navbar-item',
                    href='/Home/'
                ),
                
                html.A(
                    children='Analytics',
                    id='analytics-tab',
                    className='navbar-item',
                ),
                
                frontend.menu(
                    tables=database.tables,
                    section='Analytics',
                    style={'margin-left': '14.5vw'}
                ),

                html.A(
                    children='Blockchains',
                    id='blockchains-tab',
                    className='navbar-item',
                ),
    
                frontend.menu(
                    tables=database.tables,
                    section='Blockchains',
                    style={'margin-left': '19.5vw'}
                ),
    
                html.A(
                    children='Data',
                    id='data-tab',
                    className='navbar-item',
                    href='/Home/Data'
                ),

                html.A(
                    children='Queries',
                    id='queries-tab',
                    className='navbar-item',
                    href='/Home/Queries'
                ),
    
                html.Div(
                    children=html.Img(
                        src='/assets/icon/power.svg',
                        className='navbar-icon',
                    ),
                    className='navbar-icon-container',
                    style={'margin-left': '52vw'}
                ),
    
                html.Div(
                    children=html.Img(
                        src='/assets/icon/setting.svg',
                        className='navbar-icon',
                    ),
                    className='navbar-icon-container',
                ),
    
                html.A(
                    children='Login',
                    className='login-button',
                ),
                
            ],
            style={
                'display': 'flex',
                'background': 'linear-gradient(107.56deg, #22264C 0%, #4A406E 50.52%, #885E80 100%)',
                'margin': '0',
                'padding': '0'
            }
        ),

        # Location
        html.Div(
            children=[

                dcc.Location(
                    id='location',
                    refresh=False
                ),

                 html.Div(
                     id='url',
                     className='url',
                 ),

            ],
            style={
                'display': 'flex',
                'background': 'white',
                'margin': '0',
                'padding': '0'
            }
        ),

        # Contents
        html.Div(
            id='contents'
        ),

    ]
)


@app.callback(
    [Output('url', 'children'),
     Output('contents', 'children')],
    [Input('location', 'pathname')],
)
def switch_tab(pathname):
    return backend.switch_tab(pathname)


@app.callback(
    Output('total-value-locked-storage', 'data'),
    [Input('location', 'pathname')],
)
def update_total_value_locked_data(_):
    return home_callbacks.update_total_value_locked_data()


@app.callback(
     Output('total-value-locked-figure-container', 'children'),
    [Input('total-value-locked-storage', 'data'),
     Input('total-value-locked-table', 'data'),
     Input('1d-total-value-locked', 'n_clicks'),
     Input('7d-total-value-locked', 'n_clicks'),
     Input('1m-total-value-locked', 'n_clicks'),
     Input('3m-total-value-locked', 'n_clicks')],
)
def update_total_value_locked_figure(data, table, _, __, ___, ____):
    return home_callbacks.update_total_value_locked_figure(data, table)


@app.callback(
     Output('total-value-locked-table-container', 'children'),
    [Input('total-value-locked-storage', 'data'),
     Input('all-total-value-locked', 'n_clicks'),
     Input('dex-total-value-locked', 'n_clicks'),
     Input('derivatives-total-value-locked', 'n_clicks'),
     Input('lending-total-value-locked', 'n_clicks')]
)
def update_total_value_locked_table(data, _, __, ___, ____):
    return home_callbacks.update_total_value_locked_table(data)


@app.callback(
    Output('top-pools-table-container', 'children'),
    [Input('location', 'pathname')],
)
def update_top_pools_table(_):
    return home_callbacks.update_top_pools_table()


@app.callback(
    [Output('top-pairs-by-volume-table-container', 'children'),
     Output('total-volume-figure-container', 'children')],
    [Input('location', 'pathname')],
)
def update_top_pairs_by_volume_tables_and_graphs(pathname):
    return exchanges_callbacks.update_top_pairs_by_volume_tables_and_graphs(pathname)


@app.callback(
    [Output('top-pairs-by-liquidity-table-container', 'children'),
     Output('total-liquidity-figure-container', 'children')],
    [Input('location', 'pathname')],
)
def update_top_pairs_by_liquidity_tables_and_graphs(pathname):
    return exchanges_callbacks.update_top_pairs_by_liquidity_tables_and_graphs(pathname)


@app.callback(
    [Output('pair-transactions-table-container', 'children'),
     Output('pair-transactions-figure-container', 'children')],
    [Input('location', 'pathname')],
)
def update_selected_pair_transactions_table_and_graph(pathname):
    return pairs_callbacks.update_selected_pair_transactions_table_and_graph(pathname)


@app.callback(
     Output('pair-transactions-figure', 'figure'),
    [Input('pair-transactions-value', 'n_clicks'),
     Input('pair-transactions-count', 'n_clicks')],
    [State('pair-transactions-figure', 'figure')]
)
def update_selected_pair_transactions_graph(_, __, figure):
    return pairs_callbacks.update_selected_pair_transactions_graph(figure)


@app.callback(
    Output('pair-volume-figure-container', 'children'),
    [Input('location', 'pathname')]
)
def update_selected_pair_volume_graph(pathname):
    return pairs_callbacks.update_selected_pair_volume_graph(pathname)


@app.callback(
     Output('pair-liquidity-figure-container', 'children'),
    [Input('location', 'pathname')]
)
def update_selected_pair_liquidity_graph(pathname):
    return pairs_callbacks.update_selected_pair_liquidity_graph(pathname)


@app.callback(
    Output('pair-prices-figure-container', 'children'),
    [Input('location', 'pathname')]
)
def update_selected_pair_price_evolution_graph(pathname):
    return pairs_callbacks.update_selected_pair_price_evolution_graph(pathname)


@app.callback(
    Output('protocol-data', 'children'),
    [Input('location', 'pathname')]
)
def update_derivatives_data(pathname):
    return derivatives_callbacks.update_derivatives_data(pathname)


@app.callback(
    [Output('pods-pools-table', 'children'),
     Output('pods-pool-assets-figure', 'children')],
    [Input('location', 'pathname')]
)
def update_pods_finance_pools_table_and_graphs(_):
    return derivatives_callbacks.update_pods_finance_pools_table_and_graphs()


@app.callback(
    [Output('pods-options-table', 'children'),
     Output('pods-option-assets-figure', 'children'),
     Output('pods-option-network-figure', 'children'),
     Output('pods-exercise-type-figure', 'children'),
     Output('pods-option-type-figure', 'children'),
     Output('pods-option-action-figure', 'children')],
    [Input('location', 'pathname')]
)
def update_pods_finance_options_table_and_graphs(_):
    return derivatives_callbacks.update_pods_finance_options_table_and_graphs()


@app.callback(
    [Output('synthetix-exchanges-table', 'children'),
     Output('synthetix-top-pairs-figure', 'children')],
    [Input('location', 'pathname')]
)
def update_synthetix_options_table_and_graphs(_):
    return derivatives_callbacks.update_synthetix_options_table_and_graphs()


@app.callback(
     Output('block-numbers', 'children'),
    [Input('location', 'pathname'),
     Input('1d-block-numbers', 'n_clicks'),
     Input('7d-block-numbers', 'n_clicks'),
     Input('1m-block-numbers', 'n_clicks'),
     Input('3m-block-numbers', 'n_clicks')],
)
def update_block_numbers_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_block_numbers_graph(pathname)


@app.callback(
     Output('block-counts', 'children'),
    [Input('location', 'pathname'),
     Input('1m-block-counts', 'n_clicks'),
     Input('6m-block-counts', 'n_clicks'),
     Input('1y-block-counts', 'n_clicks'),
     Input('2y-block-counts', 'n_clicks')],
)
def update_block_counts_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_block_counts_graph(pathname)


@app.callback(
     Output('block-sizes', 'children'),
    [Input('location', 'pathname'),
     Input('1d-block-sizes', 'n_clicks'),
     Input('7d-block-sizes', 'n_clicks'),
     Input('1m-block-sizes', 'n_clicks'),
     Input('3m-block-sizes', 'n_clicks')],
)
def update_block_sizes_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_block_sizes_graph(pathname)


@app.callback(
     Output('daily-block-sizes', 'children'),
    [Input('location', 'pathname'),
     Input('1m-daily-block-sizes', 'n_clicks'),
     Input('6m-daily-block-sizes', 'n_clicks'),
     Input('1y-daily-block-sizes', 'n_clicks'),
     Input('2y-daily-block-sizes', 'n_clicks')],
)
def update_daily_block_sizes_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_daily_block_sizes_graph(pathname)


@app.callback(
     Output('cumulative-transactions', 'children'),
    [Input('location', 'pathname'),
     Input('1d-cumulative-transactions', 'n_clicks'),
     Input('7d-cumulative-transactions', 'n_clicks'),
     Input('1m-cumulative-transactions', 'n_clicks'),
     Input('3m-cumulative-transactions', 'n_clicks')],
)
def update_cumulative_transactions_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_cumulative_transactions_graph(pathname)


@app.callback(
     Output('daily-transactions', 'children'),
    [Input('location', 'pathname'),
     Input('1m-daily-transactions', 'n_clicks'),
     Input('6m-daily-transactions', 'n_clicks'),
     Input('1y-daily-transactions', 'n_clicks'),
     Input('2y-daily-transactions', 'n_clicks')],
)
def update_daily_transactions_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_daily_transactions_graph(pathname)


@app.callback(
     Output('gas-limit', 'children'),
    [Input('location', 'pathname'),
     Input('1m-gas-limit', 'n_clicks'),
     Input('6m-gas-limit', 'n_clicks'),
     Input('1y-gas-limit', 'n_clicks'),
     Input('2y-gas-limit', 'n_clicks')],
)
def update_gas_limit_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_gas_limit_graph(pathname)


@app.callback(
     Output('gas-used', 'children'),
    [Input('location', 'pathname'),
     Input('1m-gas-used', 'n_clicks'),
     Input('6m-gas-used', 'n_clicks'),
     Input('1y-gas-used', 'n_clicks'),
     Input('2y-gas-used', 'n_clicks')],
)
def update_gas_used_graph(pathname, _, __, ___, ____):
    return blockchains_callbacks.update_gas_used_graph(pathname)


@app.callback(
    [Output('data-table-dropdown-1', 'options'),
     Output('data-table-dropdown-1', 'value')],
    [Input('location', 'pathname')],
)
def update_data_table_dropdown_1(_):
    return data_callbacks.update_data_table_dropdown_1()


@app.callback(
    [Output('data-table-dropdown-2', 'options'),
     Output('data-table-dropdown-2', 'value')],
    [Input('data-table-dropdown-1', 'value')],
)
def update_data_table_dropdown_2(category):
    return data_callbacks.update_data_table_dropdown_2(category)


@app.callback(
    [Output('data-table-dropdown-3', 'options'),
     Output('data-table-dropdown-3', 'value')],
    [Input('data-table-dropdown-1', 'value'),
     Input('data-table-dropdown-2', 'value')],
)
def update_data_table_dropdown_3(category, protocol):
    return data_callbacks.update_data_table_dropdown_3(category, protocol)


@app.callback(
    [Output('data-table-header', 'children'),
     Output('data-table-container', 'children'),
     Output('data-storage', 'data')],
    [Input('data-table-dropdown-2', 'value'),
     Input('data-table-dropdown-3', 'value'),
     Input('data-window-input', 'value'),
     Input('data-window-dropdown', 'value')],
)
def update_data_table(protocol, table, interval, units):
    return data_callbacks.update_data_table(protocol, table, interval, units)


@app.callback(
    [Output('data-figure-dropdown-1', 'options'),
     Output('data-figure-dropdown-1', 'value')],
    [Input('data-storage', 'data')]
)
def update_data_figure_dropdown_1(data):
    return data_callbacks.update_data_figure_dropdown_1(data)


@app.callback(
    [Output('data-figure-dropdown-2', 'options'),
     Output('data-figure-dropdown-2', 'value')],
    [Input('data-figure-dropdown-1', 'value')],
    [State('data-storage', 'data')]
)
def update_data_figure_dropdown_2(graph, data):
    return data_callbacks.update_data_figure_dropdown_2(graph, data)


@app.callback(
    [Output('data-figure-dropdown-3', 'options'),
     Output('data-figure-dropdown-3', 'value')],
    [Input('data-figure-dropdown-1', 'value')]
)
def update_data_figure_dropdown_3(graph):
    return data_callbacks.update_data_figure_dropdown_3(graph)


@app.callback(
    Output('data-figure-container', 'children'),
    [Input('data-figure-dropdown-1', 'value'),
     Input('data-figure-dropdown-2', 'value'),
     Input('data-figure-dropdown-3', 'value')],
    [State('data-storage', 'data')],
)
def update_data_figure(graph, column, aggregation, data):
    return data_callbacks.update_data_figure(graph, column, aggregation, data)


if __name__ == '__main__':
    application.run(debug=False, host='127.0.0.1')
