# Imagen base liviana de Python
FROM python:3.11-slim

# Evita prompts en instalación
ENV DEBIAN_FRONTEND=noninteractive

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar primero requirements.txt (mejor cacheo)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

# Exponer el puerto que usará Flask
EXPOSE 5000

# Comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]