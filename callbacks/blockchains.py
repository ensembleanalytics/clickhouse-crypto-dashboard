import dash
import datetime
from dateutil.relativedelta import relativedelta

import queries.blockchains as queries

def update_block_numbers_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1d-block-numbers.n_clicks' in changed_id:
        return queries.block_numbers(
            protocol=protocol,
            start=today - relativedelta(days=1),
            end=today
        )

    elif '7d-block-numbers.n_clicks' in changed_id:
        return queries.block_numbers(
            protocol=protocol,
            start=today - relativedelta(days=7),
            end=today
        )

    elif '1m-block-numbers.n_clicks' in changed_id:
        return queries.block_numbers(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )

    elif '3m-block-numbers.n_clicks' in changed_id:
        return queries.block_numbers(
            protocol=protocol,
            start=today - relativedelta(months=3),
            end=today)

    else:
        return queries.block_numbers(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today)


def update_block_counts_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1m-block-counts.n_clicks' in changed_id:
        return queries.block_counts(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )
    
    elif '6m-block-counts.n_clicks' in changed_id:
        return queries.block_counts(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )
    
    elif '1y-block-counts.n_clicks' in changed_id:
        return queries.block_counts(
            protocol=protocol,
            start=today - relativedelta(years=1),
            end=today
        )
    
    elif '2y-block-counts.n_clicks' in changed_id:
        return queries.block_counts(
            protocol=protocol,
            start=today - relativedelta(years=2),
            end=today
        )
    
    else:
        return queries.block_counts(
            protocol=protocol,
            start=today - relativedelta(years=3),
            end=today
        )


def update_block_sizes_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1d-block-sizes.n_clicks' in changed_id:
        return queries.block_sizes(
            protocol=protocol,
            start=today - relativedelta(days=1),
            end=today
        )

    elif '7d-block-sizes.n_clicks' in changed_id:
        return queries.block_sizes(
            protocol=protocol,
            start=today - relativedelta(days=7),
            end=today
        )

    elif '1m-block-sizes.n_clicks' in changed_id:
        return queries.block_sizes(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )

    elif '3m-block-sizes.n_clicks' in changed_id:
        return queries.block_sizes(
            protocol=protocol,
            start=today - relativedelta(months=3),
            end=today
        )

    else:
        return queries.block_sizes(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )


def update_daily_block_sizes_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1m-daily-block-sizes.n_clicks' in changed_id:
        return queries.daily_block_sizes(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )
    
    elif '6m-daily-block-sizes.n_clicks' in changed_id:
        return queries.daily_block_sizes(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )
    
    elif '1y-daily-block-sizes.n_clicks' in changed_id:
        return queries.daily_block_sizes(
            protocol=protocol,
            start=today - relativedelta(years=1),
            end=today
        )
    
    elif '2y-daily-block-sizes.n_clicks' in changed_id:
        return queries.daily_block_sizes(
            protocol=protocol,
            start=today - relativedelta(years=2),
            end=today
        )
    
    else:
        return queries.daily_block_sizes(
            protocol=protocol,
            start=today - relativedelta(years=3),
            end=today
        )


def update_cumulative_transactions_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1d-cumulative-transactions.n_clicks' in changed_id:
        return queries.cumulative_transactions(
            protocol=protocol,
            start=today - relativedelta(days=1),
            end=today
        )
    
    elif '7d-cumulative-transactions.n_clicks' in changed_id:
        return queries.cumulative_transactions(
            protocol=protocol,
            start=today - relativedelta(days=7),
            end=today
        )
    
    elif '1m-cumulative-transactions.n_clicks' in changed_id:
        return queries.cumulative_transactions(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )
    
    elif '3m-cumulative-transactions.n_clicks' in changed_id:
        return queries.cumulative_transactions(
            protocol=protocol,
            start=today - relativedelta(months=3),
            end=today
        )
    
    else:
        return queries.cumulative_transactions(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )


def update_daily_transactions_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1m-daily-transactions.n_clicks' in changed_id:
        return queries.daily_transactions(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )
    
    elif '6m-daily-transactions.n_clicks' in changed_id:
        return queries.daily_transactions(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )
    
    elif '1y-daily-transactions.n_clicks' in changed_id:
        return queries.daily_transactions(
            protocol=protocol,
            start=today - relativedelta(years=1),
            end=today
        )
    
    elif '2y-daily-transactions.n_clicks' in changed_id:
        return queries.daily_transactions(
            protocol=protocol,
            start=today - relativedelta(years=2),
            end=today
        )
    
    else:
        return queries.daily_transactions(
            protocol=protocol,
            start=today - relativedelta(years=3),
            end=today
        )


def update_gas_limit_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1m-gas-limit.n_clicks' in changed_id:
        return queries.gas_limit(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )

    elif '6m-gas-limit.n_clicks' in changed_id:
        return queries.gas_limit(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )

    elif '1y-gas-limit.n_clicks' in changed_id:
        return queries.gas_limit(
            protocol=protocol,
            start=today - relativedelta(years=1),
            end=today
        )

    elif '2y-gas-limit.n_clicks' in changed_id:
        return queries.gas_limit(
            protocol=protocol,
            start=today - relativedelta(years=2),
            end=today
        )

    else:
        return queries.gas_limit(
            protocol=protocol,
            start=today - relativedelta(years=3),
            end=today
        )


def update_gas_used_graph(pathname):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    today = datetime.date.today()
    protocol = pathname.split(sep='/')[-1]
    
    if '1m-gas-used.n_clicks' in changed_id:
        return queries.gas_used(
            protocol=protocol,
            start=today - relativedelta(months=1),
            end=today
        )
    
    elif '6m-gas-used.n_clicks' in changed_id:
        return queries.gas_used(
            protocol=protocol,
            start=today - relativedelta(months=6),
            end=today
        )
    
    elif '1y-gas-used.n_clicks' in changed_id:
        return queries.gas_used(
            protocol=protocol,
            start=today - relativedelta(years=1),
            end=today
        )
    
    elif '2y-gas-used.n_clicks' in changed_id:
        return queries.gas_used(
            protocol=protocol,
            start=today - relativedelta(years=2),
            end=today
        )
    
    else:
        return queries.gas_used(
            protocol=protocol,
            start=today - relativedelta(years=3),
            end=today
        )
