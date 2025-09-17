import requests
import os

API_URL = "https://genai-inference-app.stackspot.com/v1/agent/01K53XTZ9FEW05T54XPVNQ9SJ4/chat"
API_KEY = os.getenv("STACKSPOT_API_KEY")  # chave fica em variável de ambiente

def chamar_agente(mensagem: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {"input": mensagem}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("output", "⚠️ Erro ao obter resposta.")
    else:
        return f"⚠️ Erro {response.status_code}: {response.text}"
