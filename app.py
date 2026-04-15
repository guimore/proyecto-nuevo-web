from flask import Flask, render_template  # <--- Importante para leer el HTML
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Esto le dice a Flask: "Buscá el index.html adentro de la carpeta templates"
    return render_template('index.html')

if __name__ == "__main__":
    # Railway usa esta variable para asignar el puerto
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)