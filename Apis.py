# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:57:54 2021

@author: adria
"""

import pandas as pd;

!pip install nba_api;

#diccionario
dicc = {'a':[11,21,31],'b':[12,22,32]};

#convertimos a Dataframe el diccionario

df = pd.DataFrame(dicc);

df.head();
#llamamos API que calcula y retorna los valores
df.mean();

#REST (REpresentational  TState) APIS
#Permiten conectarse a través de Internet, usando almacenamiento externo
#algoritmos de Machine Learning, etc...
