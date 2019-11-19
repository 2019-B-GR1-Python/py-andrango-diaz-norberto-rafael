# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:59:50 2019

@author: USRBET
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numero = np.array((1,2,3,4))

serie_A = pd.Series(lista_numeros)
serie_B = pd.Series(tupla_numeros)
serie_C = pd.Series(np_numeros)

serie_D = pd.Series([
        True,
        False,
        12,
        12.12,
        "Rafael",
        None,
        (),
        [],
        {"nombre":"Rafael"}
        
        
        ])

serie_D[3]

lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]

serie_ciudad = pd.Series(lista_ciudades, index = ["A", "C", "L", "Q"])
serie_ciudad["Q"]
serie_ciudad[3]


valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil": 10000,
        "Cuenca": 7000,
        "Quito": 8000,
        "Loja": 3000
        }


serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad["Ibarra"] 
serie_valor_ciudad[0] 
ciudades_menores_5000 = serie_valor_ciudad < 5000
s5 = serie_valor_ciudad[ciudades_menores_5000]
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"]-50

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)


rsquare = np.sqrt(serie_valor_ciudad)
rsin = np.sin(serie_valor_ciudad)


ciudades_uno = pd.Series({
        "Montañita":300,
        "Guayaquil":10000,
        "Quito":2000
        })

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil":10000
        })

ciudades_uno["Loja"] = 0
ciudades_dos["Montañita"] = 0
ciudades_dos["Quito"] = 0


print(ciudades_uno+ciudades_dos)

ciudad_add = ciudades_uno.add(ciudades_dos)
ciudad_concat = pd.concat([ciudades_uno, ciudades_dos])
ciudad_concat_v = pd.concat([ciudades_uno, ciudades_dos], verify_integrity = True)
ciudad_append = ciudades_uno.append(ciudades_dos)

