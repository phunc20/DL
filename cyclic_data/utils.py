import numpy as np
from constants import *

def cyclicize_number(number, max_, min_):
    """
    args
        number, int
            \in {min_, min_ + 1, ..., max_}
            e.g. hour => min_ = 0, max_ = 24
                 longitude => min_ = -180, max_ = 180
        max_, int
        min_, int
    return
        (x, y), tuple of float
    """
    period = max_ - min_
    theta = 2 * np.pi * (number / period)
    #theta = 2 * np.pi * ((number - min_) / period)
    x = np.cos(theta)
    y = np.sin(theta)
    return x, y

def cyclicize_series(series, max_, min_):
    """
    args
        series, pd.Series or ndarray
    """
    return list(map(lambda number: cyclicize_number(number, max_, min_), series))


def jahreszeit(month,
               day,
               semisphere,
               rule=2):
    ## We asign using the Northern semisphere first, and adjust later
    if rule > 1 :
        start = 15
        end = 14
        if [MAR,start] <= [month, day] <= [JUN,end]:
            jz = SPRING  # jz for `Jahreszeit`
        elif [JUN,start] <= [month, day] <= [SEP,end]:
            jz = SUMMER
        elif [SEP,start] <= [month, day] <= [DEC,end]:
            jz = AUTUMN
        else:
            jz = WINTER
    else:
        start = 1
        end = 31
        if [MAR,start] <= [month, day] <= [MAY,end]:
            jz = SPRING
        elif [JUN,start] <= [month, day] <= [AUG,end]:
            jz = SUMMER
        elif [SEP,start] <= [month, day] <= [NOV,end]:
            jz = AUTUMN
        else:
            jz = WINTER
    return jz if semisphere == N else D_NSeason_SSeason[jz]


def rule3(row):
    if row.latitude >= 0:
        semisphere = N
    else:
        semisphere = S
    return jahreszeit(row.month, row.day, semisphere, rule=3)

def draw_and_show(tree_clf):
    pass
#from sklearn.tree import export_graphviz
#from graphviz import Source
#from pathlib import Path
#
##out_file = Path("./tree.png")
#out_dot = "./tmp.dot"
#export_graphviz(
#    tree_clf,
#    out_file=out_dot,
#    feature_names=df_train.columns,
#    class_names=["spring", "summer", "autumn", "winter"],
#    rounded=True,
#    filled=True,
#)
#
#out_png = ".".join(out_dot.split(".")[:-1] + ["png"])
#!dot -Tpng $(out_file) -o $out_png
#from IPython.display import Image
#Image(filename="tree_cyclic.png", width=400)
##Source.from_file(out_dot)


