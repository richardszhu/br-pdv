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
        values - list of worth of corresponding stock is in the portfolio
     """

    def __init__(self, tickers_list, values=[]):
        """
        tickers_list is a list of strings, each string being a ticker
        """
        # take list of tickers and convert into a string that can be passed into the API
        # end result example: "ticker:AAPL,ticker:MSFT,ticker:RKUNY"
        if values:
            self.values = values
        else:
            self.values = [1 for _ in tickers_list]

        self.values = values
        self.params = los_to_brparams(tickers_list)

        portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/security-data", params={'identifiers': self.params})
        self.p = portfolioAnalysisRequest.json  # get as json object
        self.p_stocks = (self.p)()['resultMap']["SECURITY"][:len(tickers_list)] # cut off to take care of "duplicate" stocks that share the same ticker

    def get_counts(self, attr_string):
        """
        returns dictionary: {Security Attribute: Count}
        Security attribute is stuff like country, currency, etc
        country, currency, exchangeAcronym, issFtse1Industry, issFtse3Sector, assetType
        """

        a_counts = {}
        for i in range(len(self.p_stocks)):
            c = self.p_stocks[i][attr_string]
            a_counts[c] = self.values[i] + a_counts.get(c, 0)
        return a_counts



def los_to_brparams(los):
    params = ''
    for ticker in los:
        params += "ticker:{},".format(ticker.upper()) #tickers have to be uppercase
    return params[:-1]  # cut off the last comma
