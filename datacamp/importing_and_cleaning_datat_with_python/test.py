from datetime import datetime 
import numpy as np
import pandas as pd

st_nicholas = datetime(2019, 12, 6)
print(st_nicholas)

data = pd.Series(['apple','banana','apple', 'banana'])
print(type(data))
print(data.str.upper())
print(type(data.str.upper()))