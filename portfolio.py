"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.

Made by Richard Zhu, Riley Dyer, Shreyash Sridhar, and David Zhu
Utilizing BlackRock's Security Data API
"""
import requests
from operator import itemgetter
from collections import defaultdict

class Portfolio():
    """
    Instance vars:
        params - passed into the API requests
        p_json - a json of the portfolio
        p_stocks - the list of stocks in the portfolio
        values - list of worth of corresponding stock is in the portfolio
    """

    def __init__(self, tickers_list, values=[]):
        """
        Args:
            tickers_list: List of ticker strings
            values: List of corresponding weights (dollars) for each ticker
        """
        
        self.values = values if values else [1] * len(tickers_list)

        #https://stackoverflow.com/a/13668413 Needed to keep order in sync with API
        self.tickers_list, self.values = [list(x) for x in zip(*sorted(zip(tickers_list, self.values), key=itemgetter(0)))]

        portfolio_analysis_request = requests.get("https://www.blackrock.com/tools/hackathon/security-data", 
            params={'identifiers': format_tickers_to_Aladdin(self.tickers_list)})

        self.p_json = portfolio_analysis_request.json
        self.p_stocks = (self.p_json)()['resultMap']["SECURITY"][:len(tickers_list)]

    
    def get_counts(self, attr):
        """
        Args:
            attr: The specific attribute we're counting values of.

        Returns:
            Dictionary - {Security Attribute: Count}
        """
        counts = defaultdict(int)
        for stock, value in zip(self.p_stocks, self.values):
            counts[stock.get(attr, "No " + attr)] += value
        return counts

        #a_counts = {}
        #for i in range(len(self.p_stocks)):
        #    c = self.p_stocks[i].get(attr, "No {}".format(attr))
        #    a_counts[c] = self.values[i] + a_counts.get(c, 0)
        #return a_counts


def format_tickers_to_Aladdin(tickers):
    """
    Args:
        tickers: A list of stock ticker strings.
    
    Returns:
        The joined string of tickers, correctly formatted to pass into the BlackRock API.
        Example of correctly formatted string: "ticker:AAPL,ticker:MSFT,ticker:RKUNY"
    """
    return ",".join(["ticker:" + t.upper() for t in tickers])
