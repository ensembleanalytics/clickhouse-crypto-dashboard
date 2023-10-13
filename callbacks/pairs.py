import dash

from queries.pairs import transactions, prices, volume, liquidity

def update_selected_pair_transactions_table_and_graph(pathname):
    return transactions(
        protocol=str(pathname).split(sep='/')[-2],
        pair=str(pathname).split(sep='/')[-1].strip('-Pair')
    )


def update_selected_pair_volume_graph(pathname):
    return volume(
        protocol=str(pathname).split(sep='/')[-2],
        pair=str(pathname).split(sep='/')[-1].strip('-Pair')
    )


def update_selected_pair_liquidity_graph(pathname):
    return liquidity(
        protocol=str(pathname).split(sep='/')[-2],
        pair=str(pathname).split(sep='/')[-1].strip('-Pair')
    )


def update_selected_pair_price_evolution_graph(pathname):
    return prices(
        protocol=str(pathname).split(sep='/')[-2],
        pair=str(pathname).split(sep='/')[-1].strip('-Pair')
    )
    

def update_selected_pair_transactions_graph(figure):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    if 'pair-transactions-count.n_clicks' in changed_id:
        
        for i in range(len(figure['data'])):
            if figure['data'][i]['text'] == ['count']:
                figure['data'][i]['visible'] = True
                figure['data'][i]['showlegend'] = True
            else:
                figure['data'][i]['visible'] = False
                figure['data'][i]['showlegend'] = False
        
        figure['layout']['yaxis']['tickformat'] = ',.0f'
        figure['layout']['yaxis']['title']['text'] = 'Count'
        
        return figure

    else:
    
        for i in range(len(figure['data'])):
            if figure['data'][i]['text'] == ['value']:
                figure['data'][i]['visible'] = True
                figure['data'][i]['showlegend'] = True
            else:
                figure['data'][i]['visible'] = False
                figure['data'][i]['showlegend'] = False
    
        figure['layout']['yaxis']['tickformat'] = '$,.0f'
        figure['layout']['yaxis']['title']['text'] = 'Value'
        
        return figure
