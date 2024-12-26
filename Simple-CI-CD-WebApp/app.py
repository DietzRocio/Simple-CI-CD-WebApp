import os
from flask import Flask

app = Flask(__name__)

# Aquí puedes verificar si la variable de entorno PORT está definida
port = int(os.getenv("PORT", 8080))  # Asegúrate de que el puerto sea un entero
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)  # Usamos el puerto obtenido de la variable de entorno.

