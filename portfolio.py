"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.

Made by Richard Zhu, Riley Dyer, Shreyash Sridhar, and David Zhu
Utilizing BlackRock's Security Data API
"""
import requests
from operator import itemgetter

class Portfolio():
    """
    Instance vars:
        params - passed into the API requests
        p - a json of the portfolio
        p_stocks - the list of stocks in the portfolio, and which ones are
        values - list of worth of corresponding stock is in the portfolio
     """

    def __init__(self, tickers_list, values=[]):
        """
        tickers_list is a list of strings, each string being a ticker

        Takes list of tickers and converts it into a string that can be passed into the API
        Example of passable string: "ticker:AAPL,ticker:MSFT,ticker:RKUNY"
        """
        if values:
            self.values = values
        else:
            self.values = [1 for _ in tickers_list]
        self.tickers_list, self.values = [list(x) for x in zip(*sorted(zip(tickers_list, self.values), key=itemgetter(0)))]

        self.params = los_to_brparams(self.tickers_list)

        portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/security-data", params={'identifiers': self.params})
        self.p = portfolioAnalysisRequest.json  # get as json object
        self.p_stocks = (self.p)()['resultMap']["SECURITY"][:len(tickers_list)] # cut off to take care of "duplicate" stocks that share the same ticker

    def get_counts(self, attr):
        """
        Returns dictionary: {Security Attribute: Count}

        Security attribute is stuff like:
        country, currency, exchangeAcronym, issFtse1Industry, issFtse3Sector, assetType
        All attributes: https://www.blackrock.com/tools/api-tester/hackathon?apiType=securityData
        """

        a_counts = {}
        for i in range(len(self.p_stocks)):
            if attr not in p_stocks[i]

            c = self.p_stocks[i].get(attr, "No {}".format(attr))
            a_counts[c] = self.values[i] + a_counts.get(c, 0)
        return a_counts


def alphabetize(tickers_list, values):
    tickers_list.sort

def los_to_brparams(los):
    params = ''
    for ticker in los:
        params += "ticker:{},".format(ticker.upper()) #tickers have to be uppercase
    return params[:-1]  # cut off the last comma

print (Portfolio(['SPY', 'RKUNY'], [300, 500]).get_counts("assetType"))
