import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


JAN = 1
FEB = 2
MAR = 3
APR = 4
MAY = 5
JUN = 6
JUL = 7
AUG = 8
SEP = 9
OCT = 10
NOV = 11
DEC = 12

SPRING = 0
SUMMER = 1
AUTUMN = 2
WINTER = 3

season_to_id = {
    "spring": 0,
    "summer": 1,
    "autumn": 2,
    "winter": 3,
}

SEED = 20


ndays_big = 31
ndays_small = 30
ndays_feb = 28

D_month_ndays = {
    JAN: ndays_big,
    FEB: ndays_feb,
    MAR: ndays_big,
    APR: ndays_small,
    MAY: ndays_big,
    JUN: ndays_small,
    JUL: ndays_big,
    AUG: ndays_big, 
    SEP: ndays_small,
    OCT: ndays_big,
    NOV: ndays_small,
    DEC: ndays_big,
}

L_month_day = []
for month in (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC,):
    #L = [[month, i] for i in range(1, n_days_in(month)+1)]
    L = [[month, i] for i in range(1, D_month_ndays[month]+1)]
    L_month_day.extend(L)

X = np.array(L_month_day)

