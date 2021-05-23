import numpy as np

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
    "spring": SPRING,
    "summer": SUMMER,
    "autumn": AUTUMN,
    "winter": WINTER,
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
for month in range(JAN, DEC+1):
    L = [[month, i] for i in range(1, D_month_ndays[month]+1)]
    L_month_day.extend(L)


granularity = 1
latitudes = range(-89, 90, granularity)  # exclude -90 and 90, which have no longitude
longitudes = range(-179, 180+1, granularity)

S = 0
N = 1
D_NSeason_SSeason = {
    SUMMER: WINTER,
    WINTER: SUMMER,
    SPRING: AUTUMN,
    AUTUMN: SPRING,
}
