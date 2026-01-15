#%%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Definimos um User-Agent para simular um navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fazemos a requisição usando o requests
response = requests.get(url, headers=headers)

# Passamos o texto da resposta (HTML) para o pandas
dfs = pd.read_html(response.text)

# Exemplo: A tabela principal das UFs geralmente é a primeira ou segunda
df_brasil = dfs[1] 
df_brasil

df_brasil.to_csv("unidades_federativas_brasil.csv", index=False,sep=";")