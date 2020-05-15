from bsedata.bse import BSE
b = BSE()
import pandas as pd
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)

HUL = b.getQuote('500696')
print(HUL)

import quandl
quandl.ApiConfig.api_key = 'C6-GSBLMUnNx8rDK9-PW'

HUL1 = quandl.get("BSE/BOM500696")

HUL1.head()

HUL1.describe()

HUL_df = pd.DataFrame.from_dict(HUL,orient = 'index')
HUL_df

keys = ['buy','sell']

buy_order = pd.DataFrame.from_dict(HUL['buy'],orient='index')
sell_orders = pd.DataFrame.from_dict(HUL['sell'],orient='index')
