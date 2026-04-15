from flask import Flask, render_template
import os

app = Flask(__name__)

# Ruta para el Inicio (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para Nosotros
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Ruta para Galería
@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# Ruta para Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == "__main__":
    # Esto es vital para que Railway asigne el puerto correctamente
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)