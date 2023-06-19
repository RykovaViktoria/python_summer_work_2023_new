import numpy as np
import pandas as pd
df = pd.DataFrame([['dd', 'lala', 23],
                  [2, 'rurk', 44],
                  [3, 'rer', 2]])

su = 0
for i in df.index:
    for j in df.columns:
        if type(df.loc[i,j]) == np.int64:
            su += df.loc[i,j]
print(su)



