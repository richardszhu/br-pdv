"""
Must install MatPlotLib to function
Installation instructions: https://matplotlib.org/users/installing.html
"""

import matplotlib.pyplot as plt
from portfolio import *
from matplotlib.widgets import TextBox

english_attrs = {"exchangeAcronym": "Exchange", "issFtse1Industry": "Industry",
                 "issFtse3Sector": "Sector",  "assetType": "Asset Type"}

def vis_pie(p, attr):
    """
    p is a Portfolio instance
    attr is the same attr that gets passed into get_counts
    """
    counts = p.get_counts(attr)

    fig1, ax1 = plt.subplots()
    ax1.pie(list(counts.values()),
            explode=[0] * len(counts),
            labels=tuple(counts),
            autopct='%1.1f%%',
            shadow=False,
            startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    ax1.set_title("Diversity of Portfolio: {} of Investments".format(attr_to_english(attr)))
    ax1.legend(["{0}: ${1}.00".format(key, counts[key]) for key in list(counts.keys())], title="Value",)
    plt.show()

def attr_to_english(attr):
    return english_attrs.get(attr, attr.capitalize())

def submit(input_string):
    tpa_list = input_string.split(", ")
    ticker_list = tpa_list[0].split()
    price_list = list(map(int, tpa_list[1].split()))
    req_attr = tpa_list[2]
    vis_pie(Portfolio(ticker_list, price_list), req_attr)

axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'Ticker', initial='BLK GOOGL RKUNY BABA, 1200 100 400 500, country')
text_box.on_submit(submit)
plt.show()
