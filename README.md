# 🛒 PriceSmart Stock Monitor (Scraper)

Este proyecto es un script en Python que utiliza Selenium para monitorear la disponibilidad de productos en [PriceSmart El Salvador](https://www.pricesmart.com/es-sv/) y notificar por correo electrónico cuando haya stock disponible.

---

## 🚀 Características

- Scraping automatizado en modo headless con Google Chrome.
- Revisión de disponibilidad desde la **página de búsqueda** o productos individuales.
- Envío de notificación por correo cuando hay productos disponibles.
- Compatible con ejecución manual o programada (ej. `cron`).

---

## 📦 Requisitos

- **Python 3.11 o superior**
- **Google Chrome estable**
- **ChromeDriver compatible con tu versión de Chrome**
- **Cuenta de Gmail** (o cualquier SMTP)
- **Archivo `.env` con credenciales de correo**

---

## 🛠️ Instalación

### 1. Instala Google Chrome y ChromeDriver


```bash
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
  | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable
```

---

### 2. Clona el repositorio

```bash
git clone https://github.com/kevocodes/pricesmart-scraper.git
cd pricesmart-scraper
```

---

### 3. Crea tu archivo `.env`

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus datos SMTP:

```env
EMAIL_USER=tucorreo@gmail.com
EMAIL_PASS=tu_app_password
EMAIL_TO=destinatario@gmail.com
```

> ℹ️ Usa una **contraseña de aplicación** si estás usando Gmail con verificación en dos pasos.

---

### 4. Instala las dependencias de Python

```bash
pip install -r requirements.txt
```

---

### 5. Ejecuta el script

```bash
python main.py
```

Esto realizará el scraping y enviará un correo si detecta productos disponibles.

---

## 🕒 Ejecución automática (opcional)

Puedes programar la ejecución automática con `cron`. Por ejemplo, para ejecutarlo cada 30 minutos:

```bash
crontab -e
```

Y añade:

```bash
*/30 * * * * cd /ruta/al/repositorio && /usr/bin/python3 main.py
```

---

## 🧪 Tecnologías usadas

- Python 3.11
- Selenium
- Google Chrome (headless)
- ChromeDriver
- Gmail SMTP
