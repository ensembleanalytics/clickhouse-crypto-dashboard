import warnings
import pandas as pd
import numpy as np
from dash import dcc
from clickhouse_driver import Client
warnings.filterwarnings('ignore')

from utils.database import clickhouse, tables
from utils.frontend import no_data_error, line_chart

tables = tables[(tables['section'] == 'Blockchains') & (tables['category'] == 'Networks') & (tables['description'] == 'Blocks')].copy()

def block_numbers(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	timestamp,
	# 	toInt64(number) as numbers
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# order by
	# 	timestamp
    # ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#
	
	# dummy data
	data = pd.DataFrame({
		'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'numbers': np.arange(43200) + np.random.normal(loc=0, scale=5, size=43200),
	})

	if not data.empty:
		data = data.set_index('timestamp').resample('T').last().fillna(method='ffill').reset_index()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='timestamp',
					y='numbers',
					name='Block Number',
					tickformat='.0f'
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def block_counts(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	toStartOfDay(timestamp) as date,
	# 	count(distinct number) as counts
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# group by
	# 	toStartOfDay(timestamp)
	# order by
	# 	toStartOfDay(timestamp)
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#
    
    # dummy data
	data = pd.DataFrame({
		'date': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'counts': np.random.lognormal(sigma=1e-3, size=43200),
	})
	
	if not data.empty:
		data = data.set_index('date').resample('D').last().fillna(method='ffill').reset_index()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='date',
					y='counts',
					name='Block Count'
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def block_sizes(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	timestamp,
	# 	toInt64(size) as sizes
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# order by
	# 	timestamp
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#
    
    # dummy data
	data = pd.DataFrame({
		'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'sizes': np.random.lognormal(size=43200),
	})
	
	if not data.empty:
		data = data.set_index('timestamp').resample('T').last().fillna(value=0).reset_index()
		data['sizes'] = data['sizes'].cumsum()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='timestamp',
					y='sizes',
					name='Block Size'
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def daily_block_sizes(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	toStartOfDay(timestamp) as date,
	# 	avg(toInt64(size)) as sizes
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# group by
	# 	toStartOfDay(timestamp)
	# order by
	# 	toStartOfDay(timestamp)
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#
	
	# dummy data
	data = pd.DataFrame({
		'date': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'sizes': np.random.lognormal(sigma=1e-3, size=43200),
	})
	
	if not data.empty:
		data = data.set_index('date').resample('D').last().reset_index()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='date',
					y='sizes',
					name='Avg. Block Size'
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def cumulative_transactions(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	timestamp,
	# 	transactions
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# order by
	# 	timestamp
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	
	# dummy data
	data = pd.DataFrame({
		'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'transactions': np.cumsum(np.random.lognormal(size=43200)),
	})
	
	if not data.empty:
		# data['transactions'] = data['transactions'].apply(lambda x: len(x)).cumsum()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='timestamp',
					y='transactions',
					name='Transactions',
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def daily_transactions(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	#     timestamp,
	#     transactions
	# from
	#     %s
	# where
	#     timestamp > '%s' and timestamp < '%s'
	# order by
	#     timestamp
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#

	# dummy data
	data = pd.DataFrame({
		'timestamp': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'transactions': np.random.lognormal(sigma=1e-3, size=43200),
	})
	
	if not data.empty:
		# data['transactions'] = data['transactions'].apply(lambda x: len(x))
		data = data.set_index('timestamp').resample('D').sum().reset_index()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='timestamp',
					y='transactions',
					name='Daily Transactions',
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def gas_limit(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	toStartOfDay(timestamp) as date,
	# 	avg(toFloat64(gasLimit)) as limit
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# group by
	# 	toStartOfDay(timestamp)
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#

	# dummy data
	data = pd.DataFrame({
		'date': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'limit': np.random.lognormal(sigma=1e-3, size=43200),
	})
	
	if not data.empty:
		data = data.set_index('date').resample('D').last().reset_index()
		
		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='date',
					y='limit',
					name='Avg. Gas Limit',
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]
	
	else:
		return [no_data_error(top='7vw', left='20vw')]


def gas_used(protocol, start, end):
	
	# client = Client(
	# 	host=clickhouse['host'],
	# 	user=clickhouse['user'],
	# 	password=clickhouse['password'],
	# 	settings={'use_numpy': True}
	# )
	#
	# table = tables.loc[tables['protocol'] == protocol, 'table'].values[0]
	#
	# data = client.query_dataframe(query=
	# '''
	# select
	# 	toStartOfDay(timestamp) as date,
	# 	sum(toFloat64(gasUsed)) as used
	# from
	# 	%s
	# where
	# 	timestamp > '%s' and timestamp < '%s'
	# group by
	# 	toStartOfDay(timestamp)
	# ''' % (table, start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')))
	#

	# dummy data
	data = pd.DataFrame({
		'date': pd.date_range(start='2023-09-01', periods=43200, freq='T'),
		'used': np.random.lognormal(sigma=1e-3, size=43200),
	})
	
	if not data.empty:
		data = data.set_index('date').resample('D').last().reset_index()

		return [
			dcc.Graph(
				figure=line_chart(
					data=data,
					x='date',
					y='used',
					name='Gas Used'
				),
				config={
					'responsive': True,
					'autosizable': True,
					'displaylogo': False,
				},
				style={
					'height': '100%',
					'width': '100%'
				}
			)
		]

	else:
		return [no_data_error(top='7vw', left='20vw')]
