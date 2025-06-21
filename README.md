# 🛒 PriceSmart Stock Monitor (Scraper)

Este proyecto es un script en Python que utiliza Selenium y Docker para monitorear la disponibilidad de productos en [PriceSmart El Salvador](https://www.pricesmart.com/es-sv/) y notificar por correo electrónico cuando haya stock disponible.

---

## 🚀 Características

- Scraping automatizado en modo headless con Chromium.
- Revisión de disponibilidad desde la **página de búsqueda** o productos individuales.
- Envío de notificación por correo cuando hay productos disponibles.
- Contenedor Docker liviano y fácil de desplegar en cualquier servidor.

---

## 📦 Requisitos

- Docker instalado
- Cuenta de Gmail (o cualquier SMTP)
- Contraseña de aplicación si usas Gmail
- Archivo `.env` con tus credenciales

---

## ⚙️ Instalación y ejecución

### 1. Clona este repositorio o descarga el `.zip`

```bash
git clone https://github.com/kevocodes/pricesmart-scraper.git
cd pricesmart-scraper
```

### 2. Crea tu archivo `.env`

Copia el ejemplo:

```bash
cp .env.example .env
```

Edita `.env` con tus datos SMTP:

```env
EMAIL_USER=tucorreo@gmail.com
EMAIL_PASS=tu_app_password
EMAIL_TO=destinatario@gmail.com
```

> ℹ️ Usa una contraseña de aplicación si estás usando Gmail con 2FA.

---

### 3. Construye la imagen Docker

```bash
docker build -t pricesmart-scraper .
```

---

### 4. Ejecuta el scraper

```bash
docker run --rm --env-file .env pricesmart-scraper
```

Esto realizará el scraping y te enviará un correo si hay productos en stock.

---

## 🕒 Ejecución automática

Puedes programar este contenedor con `cron`:

```bash
*/30 * * * * docker run --rm --env-file /ruta/a/.env pricesmart-scraper
```

Esto ejecuta el scraper cada 30 minutos.

---

## 🧪 Tecnologías usadas

- Python 3.11
- Selenium
- Chromium Headless
- Docker
- Gmail SMTP

---