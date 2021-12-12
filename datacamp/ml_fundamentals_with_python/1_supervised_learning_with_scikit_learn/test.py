import pandas as pd

platform = ["car", "car", "ios", "ios"]
id = range(4)
length = [200, 10, 50, 10]

df = pd.DataFrame({"id": id,
                   "platform": platform,
                    "length": length})

print(df)
