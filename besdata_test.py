from bsedata.bse import BSE
b = BSE()
import pandas as pd
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)
import time
import multiprocessing

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)


df = pd.read_csv("StockDataFetchScrips - Sheet1.csv")
df.columns
 df = df.drop(df.index[0])
df.head()
df['BSE Scrip'] = df['BSE Scrip'].astype(int)
df['BSE Scrip'] = df['BSE Scrip'].astype(str)

def LiveMarket():
    conditions = True
    for ticker in df['BSE Scrip']:
        print("Scraping BSE Website for Live prices")
        LiveStock[ticker] = list(b.getQuote(ticker))

        





HUL = b.getQuote('500696')
print(HUL)


HUL_df = pd.DataFrame.from_dict(HUL,orient = 'index')
HUL_df


'''buy_orders = pd.DataFrame.from_dict(HUL['buy'],orient='index')
buy_orders.columns = ['buyPrice','buyQty']
sell_orders = pd.DataFrame.from_dict(HUL['sell'],orient='index')
sell_orders.columns = ['SellPrice','SellQty']

HUL_orderbook = buy_orders.append(sell_orders)

frame = [buy_orders,sell_orders]

HUL_orderbook_concat = pd.concat(frame)
'''
