import matplotlib.pyplot as plt
from portfolio import *

def vis_pie(p, attr):
    """
    p is a Portfolio instance
    attr is the same attr that gets passed into get_counts
    """
    counts = p.get_counts(attr)

    tup = tuple(counts)
    explode = [0] * len(counts)

    fig1, ax1 = plt.subplots()
    ax1.pie(list(counts.values()), explode=explode, labels=tup, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


vis_pie(Portfolio(["aapl", 'MsFt', 'RKUNY']), "country")
