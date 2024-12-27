import os
from flask import Flask
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env si existe
load_dotenv()

app = Flask(__name__)

# Obtener el puerto de la variable de entorno, con un valor por defecto de 8080
port = int(os.getenv("PORT", 8080))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)

