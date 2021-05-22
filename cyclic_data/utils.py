import numpy as np

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

