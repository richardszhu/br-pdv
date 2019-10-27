import requests
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/security-data", params= {'identifiers' :"ticker:AAPL,ticker:MSFT,ticker:RKUNY"})
#make a way to pass in tickers
x = portfolioAnalysisRequest.text # get in text string format
portfolio = portfolioAnalysisRequest.json # get as json object
p_stocks = portfolio()['resultMap']["SECURITY"]

list_of_countries = [stock["country"] for stock in p_stocks]
country_count = {}
for c in list_of_countries:
    country_count[c] = 1 + country_count.get(c, 0)
#print(y())
print(country_count)
