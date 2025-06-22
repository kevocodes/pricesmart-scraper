# 🏍️ PriceSmart Stock Monitor (Scraper)

Este proyecto es un script en Python que utiliza Selenium para monitorear la disponibilidad de productos en [PriceSmart El Salvador](https://www.pricesmart.com/es-sv/) y notificar por correo electrónico (vía Resend) cuando haya stock disponible.

---

## 🚀 Características

* Scraping automatizado en modo headless con Google Chrome.
* Revisión de disponibilidad desde la **página de búsqueda** o productos individuales.
* Envío de notificación por correo usando [Resend](https://resend.com).
* Compatible con ejecución manual o programada (ej. `cron`).

---

## 📦 Requisitos

* **Python 3.11 o superior**
* **Google Chrome estable**
* **ChromeDriver compatible con tu versión de Chrome**
* \*\*Cuenta en \*\*[**Resend**](https://resend.com) con dominio verificado o dirección autorizada
* **Archivo **\`\`** con tu clave de API de Resend y destinatario**

---

## 🛠️ Instalación

### 1. Instala Google Chrome

```bash
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
  | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable
```

> ⚠️ Asegúrate de que la versión de `chromedriver` instalada sea compatible con tu versión de Chrome.

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

Edita `.env` con tus datos de Resend:

```env
RESEND_API_KEY=tu_api_key_resend
EMAIL_TO=destinatario@tudominio.com
```

> ℹ️ Si aún no has verificado un dominio en Resend, solo puedes enviar correos a tu propio email registrado.

---

### 4. Crea un entorno virtual e instala dependencias

Instala `python3-venv` si no lo tienes:

```bash
sudo apt install python3-venv
```

Luego:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
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

Puedes programarlo con `cron`. Por ejemplo, cada 30 minutos:

```bash
crontab -e
```

Agrega esta línea:

```bash
*/30 * * * * cd /ruta/al/repositorio && /ruta/al/entorno/.venv/bin/python3 main.py
```

---

## 🤖 Tecnologías usadas

* Python 3.11
* Selenium
* Google Chrome Headless
* ChromeDriver
* [Resend](https://resend.com) (Email API)
