# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()   

# %%

df["pontos_100"] = df["qtdePontos"] + 100

df.head()

# %%

df["emailTwich"] = df["flEmail"] + df["flTwitch"]

df.head()

# %%
df["flEmail"] * df["flTwitch"]

# %%

df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df

# %%

df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df

# %%
df["qtdePontos"]

# %%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

# %%

import matplotlib.pyplot as plt

plt.grid(True)
plt.hist(df["logPontos"])
plt.show()