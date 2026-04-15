# Usamos una imagen liviana de Python
FROM python:3.9-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos todos los archivos de tu PC al contenedor
COPY . .

# Instalamos las librerías del requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para arrancar la app usando gunicorn (que es para producción)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]