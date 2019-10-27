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

def get_counts(attr_string):
    """
    returns dictionary, (Attribute, Count)
    """
    a_counts = {}
    for stock in p_stocks:
        c = stock[attr_string]
        a_counts[c] = 1 + a_counts.get(c, 0)
    return a_counts

print(get_counts("country"))
