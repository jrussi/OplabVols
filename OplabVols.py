import requests
import os
from flask import Flask, send_file

app = Flask(__name__)

# URL da API de onde o JSON será baixado
API_URL = 'https://api.exemplo.com/dados.json'
JSON_FILE_PATH = 'data.json'

def baixar_json():
    """Função para baixar o JSON e salvar localmente."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        with open(JSON_FILE_PATH, 'w') as file:
            file.write(response.text)
        print("JSON baixado e salvo com sucesso.")
    else:
        print("Erro ao baixar JSON")

@app.route('/download-json')
def download_json():
    """Rota para download do arquivo JSON."""
    if os.path.exists(JSON_FILE_PATH):
        return send_file(JSON_FILE_PATH, as_attachment=True)
    else:
        return "Arquivo JSON não encontrado. Execute o download primeiro.", 404

# Baixa o JSON ao iniciar o servidor
baixar_json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
