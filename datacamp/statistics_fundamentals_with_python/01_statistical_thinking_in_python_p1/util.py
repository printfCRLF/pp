import numpy as np 

def ecdf(data): 
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, len(x) + 1) / n
    return x, y

