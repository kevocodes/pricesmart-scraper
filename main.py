import time
import resend
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

BROWSER_PATH = "/usr/bin/google-chrome-stable"
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")

resend.api_key = RESEND_API_KEY

OUT_OF_STOCK_TEXT = ["fuera de inventario", "agotado", "no disponible", "sin stock", "fuera de stock"]
IN_STOCK_TEXT = ["disponible", "en stock", "en inventario", "agregar a carrito", "listo para recoger"]

PRODUCT_URLS = [
    "https://www.pricesmart.com/es-sv/producto/owala-botellas-para-agua-2-unidades-710-ml-24-oz-468318/468318-0840467300561",
    "https://www.pricesmart.com/es-sv/producto/owala-botellas-para-agua-2-unidades-710-ml-24-oz-468318/468318-0840467300585",
    "https://www.pricesmart.com/es-sv/producto/owala-botellas-para-agua-2-unidades-710-ml-24-oz-468318/468318-0840467300578"
]

SEARCH_URL = "https://www.pricesmart.com/es-sv/busqueda?q=owala"

# ✅ Función de envío con Resend
def enviar_correo_resend(asunto, cuerpo):
    try:
        print(f"📤 Enviando correo: {asunto}")
        resend.Emails.send({
            "from": "delivery@resend.dev",  # Puedes usar un dominio verificado
            "to": EMAIL_TO,
            "subject": asunto,
            "html": f"<p>{cuerpo.replace(chr(10), '<br>')}</p>"
        })
        print("✅ Correo enviado correctamente con Resend.")
    except Exception as e:
        print(f"❌ Error al enviar correo con Resend: {e}")

def enviar_correo(urlProduct):
    asunto = "¡Producto Owala DISPONIBLE en PriceSmart!"
    cuerpo = f"Ya hay stock disponible: {urlProduct}"
    enviar_correo_resend(asunto, cuerpo)

def enviar_correo_busqueda(products):
    asunto = "¡Productos DISPONIBLES en PriceSmart!"
    cuerpo = "Los siguientes productos están disponibles:\n" + "\n".join([f"{name}: {url}" for name, url in products])
    enviar_correo_resend(asunto, cuerpo)

def enviar_correo_error(tipo):
    asunto = "Error al verificar stock en PriceSmart"
    cuerpo = f"Ocurrió un error al intentar verificar el stock {tipo}."
    enviar_correo_resend(asunto, cuerpo)

def check_stock(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = BROWSER_PATH

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    try:
        add_to_cart_btn = driver.find_element(By.ID, "btn-add-to-cart-pdp")
        if add_to_cart_btn.is_displayed():
            print("✅ El producto está DISPONIBLE.")
            enviar_correo(url)
        else:
            print("❌ El botón está oculto (probablemente sin stock).")
    except Exception as e:
        print("❌ No se encontró el botón 'Agregar A Carrito'.")
    driver.quit()

def check_stock_on_search_page(url):
    products_in_stock = []

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = BROWSER_PATH

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    try:
        product_elements = driver.find_element(By.CLASS_NAME, "results-listing").find_elements(By.CSS_SELECTOR, ".results-listing > div")
        if not product_elements:
            print("❌ No se encontraron productos en la página de búsqueda.")
            return
        
        for product in product_elements:
            info = product.find_element(By.CLASS_NAME, "info-wrapper")
            title = info.find_element(By.CSS_SELECTOR, ".product-card__title").get_attribute("outerText")
            status_container = info.find_element(By.CLASS_NAME, "product-card__availability--container")
            status_text = status_container.find_element(By.CSS_SELECTOR, "span").get_attribute("outerText").lower()
            product_url = info.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

            if any(text in status_text for text in IN_STOCK_TEXT):
                print(f"✅ Producto DISPONIBLE: {title} - {product_url}")
                products_in_stock.append((title, product_url))
            else:
                print(f"❌ Producto NO DISPONIBLE: {title} - {product_url}")

        if products_in_stock:
            print("\n🔔 Enviando correo con productos disponibles...")
            enviar_correo_busqueda(products_in_stock)

    except Exception as e:
        print(f"❌ Error al verificar productos: {e}")
        enviar_correo_error("en la página de búsqueda")
    finally:
        driver.quit()

def main():
    print("\n🔍 Iniciando verificación de stock en URLs específicas...")
    for PRODUCT_URL in PRODUCT_URLS:
        print(f"\n🔍 Revisando stock para: {PRODUCT_URL}")
        check_stock(PRODUCT_URL)
        time.sleep(5)

    print("\n\n🔍 Iniciando verificación de stock en la página de búsqueda...")
    check_stock_on_search_page(SEARCH_URL)

main()
