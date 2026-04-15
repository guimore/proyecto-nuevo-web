from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Portfolio Lab</title></head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
            <h1>🚀 ¡Despliegue Exitoso, Gato!</h1>
            <p>Esta app está corriendo en un contenedor <b>Docker</b>.</p>
            <div style="background: #f4f4f4; display: inline-block; padding: 20px; border-radius: 10px;">
                <h3>Stack Técnico del Lab:</h3>
                <ul style="text-align: left;">
                    <li><b>Infraestructura:</b> Python & Flask</li>
                    <li><b>Containerización:</b> Docker</li>
                    <li><b>Orquestación:</b> Railway (PaaS)</li>
                    <li><b>Seguridad:</b> Wazuh & Suricata (Próximamente)</li>
                </ul>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Importante usar la variable PORT para que Railway asigne el puerto
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)