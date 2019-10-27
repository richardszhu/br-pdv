import requests
"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""


class Portfolio():
    """docstring for Portfolio.
        Instance vars:
        params - passed into the API requests
        p - a json of the portfolio
        p_stocks - the list of stocks in the portfolio, and which ones are
        num_tickers - len(tickers)
     """

    def __init__(self, tickers_list):
        """
        tickers is a list of strings, each string being a ticker

        """
        # take list of tickers and convert into a string that can be passed into the API
        # end result example: "ticker:AAPL,ticker:MSFT,ticker:RKUNY"
        self.num_tickers = len(tickers_list)
        self.params = los_to_brparams(tickers_list)

        portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/security-data", params={'identifiers': self.params})
        self.p = portfolioAnalysisRequest.json  # get as json object
        self.p_stocks = (self.p)()['resultMap']["SECURITY"][:self.num_tickers] # cut off to take care of "duplicate" stocks that share the same ticker

    def get_counts(self, attr_string):
        """
        returns dictionary: {Security Attribute: Count}
        Security attribute is stuff like country, currency, etc
        country, currency, exchangeAcronym, issFtse1Industry, issFtse3Sector, assetType
        """

        a_counts = {}
        for stock in self.p_stocks:
            c = stock[attr_string]
            a_counts[c] = 1 + a_counts.get(c, 0)
        return a_counts


def los_to_brparams(los):
    params = ''
    for ticker in los:
        params += "ticker:{},".format(ticker.upper()) #tickers have to be uppercase
    return params[:-1]  # cut off the last comma
