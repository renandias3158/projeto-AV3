import pickle
import numpy as np


with open('modelo_dt.pkl', 'rb') as f:
    modelo = pickle.load(f)

def prever(dados):
    entrada = np.array([dados])
    resultado = modelo.predict(entrada)
    return resultado[0]
