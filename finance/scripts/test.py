import yfinance as yf


# https://ranaroussi.github.io/yfinance/

# yfinance.download()


# dat = yf.Ticker("MSFT")


# # yfinance.Ticker object <MSFT>
# print(dat)



# print(dat.info)





# # HTTP Error 404: {"quoteSummary":{"result":null,"error":{"code":"Not Found","description":"Quote not found for symbol: FOOOOOOO"}}}
# # {'trailingPegRatio': None}
# dat = yf.Ticker("FOOOOOOO")
# print(dat.info)



# spy = yf.Ticker('SPY').funds_data
# spy.description
# print(spy.top_holdings)



# print(yf.Ticker('SPY').funds_data)

# rftx_ticker = yf.Ticker('RFKTX')

# # print(rftx_ticker.info)
# print(rftx_ticker.funds_data.fund_overview)
# print(rftx_ticker.funds_data.bond_ratings)
# print(rftx_ticker.funds_data.top_holdings)

# # <class 'pandas.DataFrame'>
# print(type(rftx_ticker.funds_data.top_holdings))

# top_holdings = rftx_ticker.funds_data.top_holdings
# print(top_holdings.columns)
# print(top_holdings.axes)
# print(top_holdings.index)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
# print(top_holdings.to_dict(orient='list'))
# print(top_holdings.to_dict(orient='records', index=True))
# print(top_holdings.to_dict(orient='tight', index=True))

# print(top_holdings.columns)

# List out the symbols and then get info on those as well to create a flat list.




# print(yf.Ticker('RFKTX').funds_data.top_holdings)
# print(yf.Ticker('RNPGX').funds_data.top_holdings)


# https://stackoverflow.com/questions/67040625/pandas-to-dict-data-structure-using-column-as-dictionary-index


# print(top_holdings.T.to_dict())


# holdings_by_symbol: dict = top_holdings.T.to_dict()


# for sym in holdings_by_symbol:
#     print(sym)
#     print(holdings_by_symbol[sym]['Holding Percent'])

import sys
from cffi import FFI
ffi = FFI()

# 1. Define your custom error handler
def my_error_handler(exception, exc_value, traceback):
    print(f"Handled error: {exception}", file=sys.stderr)
    # Return a safe default value to the C code
    exit(-1)


def _print_top_holdings(ticker_symbol, indent = 0):
    try:
        ticker = yf.Ticker(ticker_symbol)
        # print(ticker)
        # print(ticker.funds_data)
        # print(ticker.funds_data.top_holdings)
        top_holdings = ticker.funds_data.top_holdings

        holdings_by_symbol: dict = top_holdings.T.to_dict()
    # except Exception as e:
    #     raise e
    except Exception as e:
        return
    
    for sym in holdings_by_symbol:
        # print(sym)
        # print(holdings_by_symbol[sym]['Holding Percent'])
        print(holdings_by_symbol[sym])
        _print_top_holdings(sym, indent+1)




_print_top_holdings('RFKTX')
