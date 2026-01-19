#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df


#%%

df.shape

#%%

df.info(memory_usage="deep")

#%%

df.dtypes

#%%

df.rename(columns={"QtdePontos": "QtdPontos"}, inplace=True)

#%%

df.head()

#%%

df [["IdTransacao", "IdCliente"]]

#%%

colunas = ["IdTransacao", "IdCliente"]

df[colunas]

#%%

df

#%%     

colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas] 

df.head()