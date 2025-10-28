import joblib
import numpy as np

modelo = joblib.load('modelo_dt.joblib')

def prever(dados):
    entrada = np.array([dados])
    resultado = modelo.predict(entrada)
    return resultado[0]
    
