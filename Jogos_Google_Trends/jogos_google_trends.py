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
from datetime import datetime

from pytrends.request import TrendReq

sns.set_style("whitegrid")

pytrend = TrendReq()

"""#Jogos Eletronicos, Buscador"""

pytrend.build_payload(kw_list=['Jogos Eletrônicos'], geo='BR', timeframe='all')

jogosEle = pytrend.interest_over_time()

jogosEle.head()

jogosEle.tail()

jogosEle.shape

jogosEle['2020-01-01': '2020-10-01']

plt.figure(figsize=(20,8))
plt.plot(jogosEle['Jogos Eletrônicos'])
plt.grid(True)
plt.title("Número de Pesquisas por Ano")
plt.ylabel("Número de Pesquisas")
plt.xlabel("Data")
plt.show

jogosEle_ano = jogosEle.resample('A').sum()

jogosEle_ano

plt.plot(jogosEle_ano)

jogosEle_mes = jogosEle.groupby([lambda x: x.month]).sum()

plt.plot(jogosEle_mes)

rq = pytrend.related_queries()

rq.values()

palavras_chave = pytrend.suggestions (keyword = 'Jogos Eletrônicos') 
df1 = pd.DataFrame (palavras_chave) 
df1.drop (columns = 'mid')

"""#Video Game, Youtube"""

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

"""#Twitch, Buscador"""

pytrend.build_payload(kw_list=['Twitch'], geo='BR', timeframe='all')

twitch = pytrend.interest_over_time()

twitch.head()

twitch.tail()

plt.figure(figsize=(20,8))
plt.plot(twitch['Twitch'])
plt.grid(True)
plt.title("Número de Pesquisas por Ano, sobre 'Twitch' ")
plt.ylabel("Número de Pesquisas")
plt.xlabel("Data")
plt.show

twitch['2020-01-01': '2020-10-01']

twitch.dtypes

twitch.index

twitch.index.max()

twitch.index.min()

twitch_ano = twitch.resample('A').sum()

twitch_ano

plt.plot(twitch_ano)

twitch_mes = twitch.groupby([lambda x: x.month]).sum()

plt.plot(twitch_mes)
