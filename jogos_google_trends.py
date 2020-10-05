# -*- coding: utf-8 -*-
"""Jogos_Google_Trends

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11LpKogRruLY82ULxMMzafF4i6eWSy2HF
"""

!pip install pytrends

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pytrends.request import TrendReq

pytrend = TrendReq()

pytrend.build_payload(kw_list=['Jogos Eletrônicos'], geo='BR', timeframe='all')

df = pytrend.interest_over_time()

df.head()

df.shape

sns.set_style("whitegrid")

plt.figure(figsize=(20,8))
plt.plot(df['Jogos Eletrônicos'])
plt.grid(True)
plt.title("Número de Pesquisas por Ano")
plt.ylabel("Número de Pesquisas")
plt.xlabel("Data")
plt.show

rq = pytrend.related_queries()

rq.values()

palavras_chave = pytrend.suggestions (keyword = 'Jogos Eletrônicos') 
df1 = pd.DataFrame (palavras_chave) 
df1.drop (columns = 'mid')

pytrend.build_payload(kw_list=['Video Game'], geo='BR', timeframe='all', gprop='youtube')

dados = pytrend.interest_over_time()

dados.head()

dados.tail()

plt.figure(figsize=(20,8))
plt.plot(dados['Video Game'])
plt.grid(True)
plt.title("Número de Pesquisas por Ano, no YouTube")
plt.ylabel("Número de Pesquisas")
plt.xlabel("Data")
plt.show

