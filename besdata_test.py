from bsedata.bse import BSE
b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)

HUL = b.getQuote('500696')
print(HUL)

import quandl
quandl.ApiConfig.api_key = 'C6-GSBLMUnNx8rDK9-PW'

mydata = quandl.get("BSE/BOM500696", start_date="2020-1-1", end_date="2020-04-31", authtoken="C6-GSBLMUnNx8rDK9-PW")

HUL1 = quandl.get("BSE/BOM500696")

HUL1.head()

HUL1.describe()
