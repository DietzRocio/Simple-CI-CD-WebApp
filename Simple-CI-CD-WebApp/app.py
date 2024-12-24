import os
from flask import Flask

app = Flask(__name__)

# Aquí puedes verificar si la variable de entorno PORT está definida
port = os.getenv("PORT", 8080)  # Se usa 8080 como valor por defecto si no está configurado.

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)  # Usamos el puerto obtenido de la variable de entorno.

