#%%

import pandas as pd

idades = [32,38,30,30,31,35,25,29,31,37,27,23,36,33,39]

nomes = ["teo","maria","joão","ana","carlos","paula","rafael","bia","marcos","julia","fernando","laura","roberto","sara","bruno"]

serie_idades = pd.Series(idades)

serie_nomes = pd.Series(nomes)

serie_idades

#%%

df = pd.DataFrame()
df["Idades"] = serie_idades
df["Nomes"] = serie_nomes

df

#%%

df["Nomes"]

#%%

df.iloc[0]

#%%

df.iloc[-1]["Idades"]