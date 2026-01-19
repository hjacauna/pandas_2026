# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

#%%

filtro = clientes["qtdePontos"] == 0

clientes0 = clientes[filtro].copy()

clientes0["flag_1"] = 1
clientes0