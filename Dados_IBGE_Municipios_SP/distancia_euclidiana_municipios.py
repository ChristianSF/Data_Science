# -*- coding: utf-8 -*-
"""Distancia_Euclidiana_Municipios

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WqPi3ESWmJMPpSHxyLmVPB409PF5JZYI
"""

import pandas as pd
import numpy as np
import folium

def Calcula_Distancia_Euc_Area(data, cidade):
  matriz_area = np.zeros((645,645), dtype=np.float64)

  for i in range(data.shape[0]):
    for j in range(data.shape[0]):
      matriz_area[i][j] = np.sqrt(np.sum(np.power(data[i] - data[j], 2)))

  dados_matriz_area = pd.DataFrame(matriz_area)

  indice = dados[dados['nome_munic'] == cidade].index
  print(dados_matriz_area.loc[indice[0]].sort_values(ascending=True))

def Calcula_Distancia_Euc_Pop(data, cidade):
  matriz_pop = np.zeros((645,645), dtype=np.float64)
  for i in range(data.shape[0]):
    for j in range(data.shape[0]):
      matriz_pop[i][j] = np.sqrt(np.sum(np.power(data[i] - data[j], 2)))

  dados_matriz_pop = pd.DataFrame(matriz_pop)

  indice = dados[dados['nome_munic'] == cidade].index
  print(dados_matriz_pop.loc[indice[0]].sort_values(ascending=True))

def Gera_Mapa(data):
  mapa = folium.Map(location=[-23.5489, -46.6388])

  for _, dados in dados.iterrows():
    fl.Marker(
        location=[dados['latitude'], dados['longitude']],
        icon=fl.Icon(icon="cloud"),
        popup=dados['nome_munic'],
    ).add_to(mapa)