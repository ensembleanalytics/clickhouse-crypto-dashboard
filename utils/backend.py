import dash

from layouts.exchanges import exchanges_layout
from layouts.derivatives import derivatives_layout
from layouts.lending import lending_layout
from layouts.pairs import pair_layout
from layouts.blockchains import blockchains_layout
from layouts.data import data_layout
from layouts.home import home_layout

from utils.frontend import url_item, page_header

def switch_tab(pathname):
    if pathname == '/' or pathname == '/Home/':
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
            ],
            home_layout
        ]
    
    elif pathname.endswith('Pair'):
        
        protocol = pathname.split(sep='/')[-2].replace('-', ' ')
        pair = pathname.split(sep='/')[-1].strip('-Pair')
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Analytics / DEX / ', href=None, active=False),
                url_item(text=protocol + ' / ', href='/Home/Analytics/DEX/' + protocol, active=False),
                url_item(text=pair, href='/Home/Analytics/DEX/' + pair, active=True),
            ],
            pair_layout(pair)
        ]
    
    elif 'DEX' in pathname:
        
        protocol = pathname.split(sep='/')[-1].replace('-', ' ')
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Analytics / DEX / ', href=None, active=False),
                url_item(text=protocol, href='/Home/Analytics/DEX/' + protocol, active=True)
            ],
            exchanges_layout(protocol)
        ]
    
    elif 'Derivatives' in pathname:
        
        protocol = pathname.split(sep='/')[-1].replace('-', ' ')
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Analytics / Derivatives / ', href=None, active=False),
                url_item(text=protocol, href='/Home/Analytics/Derivatives/' + protocol, active=True)
            ],
            derivatives_layout(protocol)
        ]

    elif 'Lending' in pathname:
    
        protocol = pathname.split(sep='/')[-1].replace('-', ' ')
    
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Analytics / Lending / ', href=None, active=False),
                url_item(text=protocol, href='/Home/Analytics/Lending/' + protocol, active=True)
            ],
            lending_layout(protocol)
        ]
    
    elif 'Data' in pathname:
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Data', href='/Home/Data', active=True)
            ],
            data_layout
        ]
    
    elif 'Networks' in pathname:
        
        protocol = pathname.split(sep='/')[-1].replace('-', ' ')
        
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Blockchains / Networks / ', href=None, active=False),
                url_item(text=protocol, href='/Home/Blockchains/Networks/' + protocol, active=True)
            ],
            blockchains_layout(protocol)
        ]

    elif 'Queries' in pathname:
    
        return [
            [
                url_item(text='Home', href='/Home/', active=False),
                url_item(text=' / Queries', href='/Home/Queries', active=True)
            ],
            page_header('Queries')
        ]
    
    else:
        raise dash.exceptions.PreventUpdate