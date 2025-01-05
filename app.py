import os
from flask import Flask
from dotenv import load_dotenv

# Cargar variables de entorno si existen
load_dotenv()

app = Flask(__name__)

# Obtenemos el puerto desde la variable de entorno o usar 8080 como valor por defecto
port = int(os.getenv("PORT", 8080))

@app.route("/")
def hello_world():
    return "¡Hallo Welt!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)


