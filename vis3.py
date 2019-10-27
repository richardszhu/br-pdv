"""
Must install MatPlotLib to function
Installation instructions: https://matplotlib.org/users/installing.html
"""

import matplotlib.pyplot as plt
from portfolio import *
from matplotlib.widgets import TextBox, Button

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
    ax1.set_title("Diversity of Portfolio: {} of Investments".format(
        attr_to_english(attr)))
    ax1.legend(["{0}: ${1}.00".format(key, counts[key]) for key in list(counts.keys())],
               title="Value",)
    plt.show()


english_attrs = {"exchangeAcronym": "Exchange", "issFtse1Industry": "Industry",
                 "issFtse3Sector": "Sector",  "assetType": "Asset Type"}

tca = [['aapl', 'baba'],[400, 200],'country']

def attr_to_english(attr):
    return english_attrs.get(attr, attr.capitalize())

def set_ticker(input_string):
    tca[0] =  input_string.split()
    #print(tca)

def set_value(input_string):
    tca[1] = [int(y) for y in input_string.split()]
    #print(tca)

def set_attri(input_string):
    tca[2] = input_string
    #print(tca)

def draw_graph(_):
    vis_pie(Portfolio(tca[0], tca[1]), tca[2])

def create_window(textread):
        fig, ax = plt.subplots()
        plt.axis('off')
        ax.text(.0,.6, textread)
        plt.show()

info_button = Button(plt.axes([0.1, 0.9, .5, 0.075]), 'Info')
attribute_button = Button(plt.axes([0.1, 0.8, .5, 0.075]), 'Attributes')

ticker_box = TextBox(plt.axes([0.1, .35, 0.8, 0.075]), "Tickers", "aapl baba")
value_box = TextBox(plt.axes([0.1, .25, 0.8, 0.075]), "Values", "400 200")
attribute_box = TextBox(plt.axes([0.1, .15, 0.8, 0.075]), "Attribute", "country")
graph_button = Button(plt.axes([0.1, 0.05, .5, 0.075]), 'Graph')

ticker_list = ticker_box.on_submit(set_ticker)
value_list = value_box.on_submit(set_value)
req_attr = attribute_box.on_submit(set_attri)

info_button.on_clicked(lambda x:create_window("\
    Portfolio Diversity Visualization Tool:\n\
    Created by Richard Zhu, David Zhu,\n\
    Riley Dyer, Shyrash Sridhar\n\
    \n Directions: Put at least two tickers\n\
    in the Tickers box, each seperated by a space\n\
    Put the correponding value of the tickers \n\
    in the Values box. Finally, put the \n\
    attribute you would like to compare\n\
    into the Attribute box"))
    
attribute_button.on_clicked(lambda x:create_window("\
    Useful Attributes:\n\
    country, currency,exchangeAcronym,\n\
    issFtse1Industry, issFtse3Sector, assetType\n\
    \nFull list at \n\
    https://www.blackrock.com/tools/api-tester/hackathon?apiType=securityData"))
graph_button.on_clicked(draw_graph)

plt.show()
