import pickle
import joblib

# 1️⃣ Carrega o modelo salvo em formato pickle
with open('modelo_dt.pkl', 'rb') as f:
    modelo = pickle.load(f)

# 2️⃣ Salva o mesmo modelo em formato joblib
joblib.dump(modelo, 'modelo_dt.joblib')

print("✅ Modelo convertido com sucesso para 'modelo_dt.joblib'")
