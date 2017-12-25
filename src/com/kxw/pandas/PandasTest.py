
import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
df.head()
df["total"] = df["A"] + df["B"] + df["C"]
df.head()
