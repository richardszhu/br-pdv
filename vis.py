"""
Must install MatPlotLib to function
Installation instructions: https://matplotlib.org/users/installing.html
"""

import matplotlib.pyplot as plt
from portfolio import *

def vis_pie(p, attr):
    """
    p is a Portfolio instance
    attr is the same attr that gets passed into get_counts
    """
    counts = p.get_counts(attr)

    fig1, ax1 = plt.subplots()
    ax1.pie(list(counts.values()), explode=[0] * len(counts), labels=tuple(counts), autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Diversity of Portfolio: {} of Investments".format(attr_to_english(attr)))
    ax1.legend (["{0}: ${1}.00".format(key, counts[key]) for key in list(counts.keys())],title="Value")
    plt.show()



english_attrs = {"exchangeAcronym" : "Exchange", "issFtse1Industry" : "Industry", "issFtse3Sector" : "Sector" ,  "assetType": "Asset Type"}
def attr_to_english(attr):
    return english_attrs.get(attr, attr.capitalize())

#vis_pie(Portfolio(["aapl", 'MsFt', 'RKUNY'], [1000, 500, 1200]), "country")
