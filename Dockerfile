FROM python:3.11-slim

# Instala Chromium y dependencias
RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    && apt-get clean

# Setea variables de entorno para Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="${PATH}:/usr/bin"

# Copia archivos
WORKDIR /app
COPY . /app

# Instala Python libs
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
