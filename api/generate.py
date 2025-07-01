# ===============================================================
#  IMPORTS COMPLETOS Y CORREGIDOS
# ===============================================================
from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs, quote
from re import findall, match, search
from json import loads
from lxml.etree import HTML
from cloudscraper import create_scraper
from hashlib import sha256
from http.cookiejar import MozillaCookieJar
from os import path as ospath
from requests import Session, post, get
from requests.adapters import HTTPAdapter
from time import sleep
from urllib3.util.retry import Retry
from uuid import uuid4
from base64 import b64decode, b64encode
import asyncio
from playwright.async_api import async_playwright
import os # Necesario para leer las variables de entorno
import base64

# ===============================================================
#  PIEZAS AUXILIARES NECESARIAS
# ===============================================================
class DirectDownloadLinkException(Exception):
    pass

class Config:
    FILELION_API = ""
    STREAMWISH_API = ""

PASSWORD_ERROR_MESSAGE = "Este enlace está protegido por contraseña. Por favor, usa el formato: {0}::contraseña"
user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0")

# Definimos las funciones que faltaban
def speed_string_to_bytes(size_string):
    size_string = str(size_string).lower()
    if 'kb' in size_string: return float(size_string.replace('kb','').strip()) * 1024
    elif 'mb' in size_string: return float(size_string.replace('mb','').strip()) * 1024 * 1024
    elif 'gb' in size_string: return float(size_string.replace('gb','').strip()) * 1024 * 1024 * 1024
    elif 'tb' in size_string: return float(size_string.replace('tb','').strip()) * 1024 * 1024 * 1024 * 1024
    return 0


def is_share_link(link: str):
    return bool(match(r'https?:\/\/.+\.gdtot\.\S+|https?:\/\/(filepress|filebee|appdrive|driveapp|gdflix|driveseed|driveace|drivepro)\.\S+', link))


# ===============================================================
#  INICIO DEL CÓDIGO COMPLETO DE SCRAPERS
# ===============================================================
from cloudscraper import create_scraper
from re import search
from json import loads
import time
import random


def fireload(url):
    """
    Versión mejorada basada en tu código original con técnicas anti-detección avanzadas
    """
    
    # Crear scraper con configuración anti-detección mejorada
    with create_scraper(
        browser={
            'browser': 'chrome',
            'platform': 'windows',
            'mobile': False,
            'desktop': True  # Añadido
        },
        delay=random.uniform(1, 3),  # Delay aleatorio
        debug=False,
        interpreter='js2py'  # Motor más stealth
    ) as session:
        try:
            # === DISFRAZ ULTRA-REALISTA (MEJORADO) ===
            
            # Versión de Chrome aleatoria y reciente
            chrome_versions = ['120.0.6099.109', '120.0.6099.129', '120.0.6099.144', '119.0.6045.199']
            chrome_version = random.choice(chrome_versions)
            
            # Headers mejorados con técnicas anti-detección
            session.headers.update({
                # Headers básicos mejorados
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                
                # Headers de seguridad modernos (CLAVE PARA FIRELOAD)
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                
                # Headers Chrome modernos (anti-detección)
                'sec-ch-ua': f'"Not_A Brand";v="8", "Chromium";v="{chrome_version.split(".")[0]}", "Google Chrome";v="{chrome_version.split(".")[0]}"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"15.0.0"',
                
                # Headers adicionales
                'Connection': 'keep-alive',
                'DNT': '1',
                
                # User-Agent ultra-realista
                'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
            })
            
            # === COMPORTAMIENTO HUMANO SIMULADO ===
            
            print("FIRELOAD/ENHANCED: Simulando llegada desde Google...")
            
            # Establecer referrer orgánico desde Google
            try:
                # Visita rápida a Google para establecer cookies realistas
                session.get("https://www.google.com", timeout=10)
                filename = url.split('/')[-1].split('.')[0]
                session.headers['Referer'] = f'https://www.google.com/search?q=fireload+{filename}'
                print("FIRELOAD/ENHANCED: Referrer orgánico establecido")
            except:
                session.headers['Referer'] = 'https://www.google.com/'
            
            # Cookies realistas de tracking
            timestamp = int(time.time())
            session.cookies.set('_ga', f'GA1.2.{random.randint(1000000000, 9999999999)}.{timestamp}')
            session.cookies.set('_gid', f'GA1.2.{random.randint(1000000000, 9999999999)}.{timestamp}')
            session.cookies.set('_fbp', f'fb.1.{timestamp}.{random.randint(1000000000, 9999999999)}')
            
            # Delay humano antes de la solicitud principal
            human_delay = random.uniform(2, 5)
            print(f"FIRELOAD/ENHANCED: Pausa humana de {human_delay:.1f}s...")
            time.sleep(human_delay)
            
            # === SOLICITUD PRINCIPAL CON REINTENTOS INTELIGENTES ===
            
            print("FIRELOAD/ENHANCED: Obteniendo la página con disfraz mejorado...")
            
            response = None
            max_attempts = 3
            
            for attempt in range(max_attempts):
                try:
                    response = session.get(url, timeout=25)
                    
                    if response.status_code == 200:
                        # Verificar que no sea una página señuelo
                        if len(response.text) < 2000:
                            print(f"FIRELOAD/ENHANCED: Intento {attempt + 1} - Página señuelo detectada")
                            if attempt < max_attempts - 1:
                                # Cambiar User-Agent y reintentar
                                new_chrome = random.choice([v for v in chrome_versions if v != chrome_version])
                                session.headers['User-Agent'] = session.headers['User-Agent'].replace(chrome_version, new_chrome)
                                chrome_version = new_chrome
                                time.sleep(random.uniform(5, 10))
                                continue
                        break
                        
                    elif response.status_code == 403:
                        print(f"FIRELOAD/ENHANCED: Intento {attempt + 1} - Bloqueado (403)")
                        if attempt < max_attempts - 1:
                            # Estrategia más agresiva: cambiar todo el perfil
                            new_chrome = random.choice([v for v in chrome_versions if v != chrome_version])
                            session.headers.update({
                                'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{new_chrome} Safari/537.36',
                                'sec-ch-ua': f'"Not_A Brand";v="8", "Chromium";v="{new_chrome.split(".")[0]}", "Google Chrome";v="{new_chrome.split(".")[0]}"'
                            })
                            time.sleep(random.uniform(8, 15))
                            
                    elif response.status_code == 429:
                        print(f"FIRELOAD/ENHANCED: Rate limit - Esperando...")
                        time.sleep(random.uniform(15, 25))
                        
                except Exception as e:
                    print(f"FIRELOAD/ENHANCED: Error en intento {attempt + 1}: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(random.uniform(5, 10))

            if not response or response.status_code != 200:
                raise DirectDownloadLinkException(f"Error después de {max_attempts} intentos. Código: {response.status_code if response else 'Sin respuesta'}")

            # === DETECCIÓN DE PÁGINA SEÑUELO ===
            
            # Verificaciones múltiples para detectar engaño
            is_decoy = False
            decoy_indicators = [
                len(response.text) < 3000,  # Página muy corta
                'window.Fl' not in response.text,  # Sin datos de descarga
                response.text.count('<script') < 3,  # Muy pocos scripts
                'noindex,nofollow' in response.text and 'dlink' not in response.text  # Solo metadatos
            ]
            
            if sum(decoy_indicators) >= 2:
                is_decoy = True
                print("FIRELOAD/ENHANCED: ⚠️  PÁGINA SEÑUELO DETECTADA")
                
                # Mostrar análisis de la página
                html_preview = response.text[:1500].replace('\n', '\\n')
                print(f"FIRELOAD/ENHANCED: HTML recibido:\n{html_preview}")
                
                # Intentar estrategia de recuperación
                print("FIRELOAD/ENHANCED: Intentando estrategia de recuperación...")
                
                # Cambiar completamente el perfil del navegador
                session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'sec-ch-ua-platform': '"macOS"',
                    'Accept-Language': 'en-GB,en;q=0.9'
                })
                
                time.sleep(random.uniform(10, 15))
                
                # Segundo intento con perfil diferente
                recovery_response = session.get(url, timeout=25)
                if recovery_response.status_code == 200 and len(recovery_response.text) > 3000:
                    response = recovery_response
                    is_decoy = False
                    print("FIRELOAD/ENHANCED: ✅ Recuperación exitosa!")

            if is_decoy:
                raise DirectDownloadLinkException("Fireload está sirviendo página señuelo. Posible detección de bot o IP bloqueada temporalmente.")

            # === BÚSQUEDA MEJORADA DEL BLOQUE DE DATOS ===
            
            print("FIRELOAD/ENHANCED: Buscando bloque de datos con patrones múltiples...")
            
            # Patrones expandidos (tu patrón original + alternativas)
            search_patterns = [
                r'(?s)window\.Fl\s*=\s*({.*?});',  # Tu patrón original
                r'(?s)window\[\'Fl\'\]\s*=\s*({.*?});',
                r'(?s)window\["Fl"\]\s*=\s*({.*?});',
                r'(?s)var\s+Fl\s*=\s*({.*?});',
                r'(?s)let\s+Fl\s*=\s*({.*?});',
                r'(?s)const\s+Fl\s*=\s*({.*?});',
                r'(?s)Fl\s*=\s*({.*?});',
                # Patrones de emergencia para dlink directo
                r'(?s)"dlink"\s*:\s*"([^"]+)"',
                r'(?s)\'dlink\'\s*:\s*\'([^\']+)\'',
            ]
            
            json_data = None
            intermediate_link = None
            
            for i, pattern in enumerate(search_patterns):
                match = search(pattern, response.text)
                if match:
                    print(f"FIRELOAD/ENHANCED: ✅ Patrón {i+1} funcionó!")
                    
                    try:
                        if i < 7:  # Patrones de objeto completo
                            json_data = loads(match.group(1))
                            intermediate_link = json_data.get("dlink")
                        else:  # Patrones de dlink directo
                            intermediate_link = match.group(1)
                        
                        if intermediate_link:
                            break
                            
                    except Exception as e:
                        print(f"FIRELOAD/ENHANCED: Error procesando patrón {i+1}: {e}")
                        continue

            if not intermediate_link:
                # Tu mensaje de error original mejorado
                html_preview = response.text[:2000].replace('\n', '\\n')
                print(f"FIRELOAD/ENHANCED: --- ANÁLISIS COMPLETO DE HTML ---\n{html_preview}\n--- FIN ANÁLISIS ---")
                
                # Análisis adicional
                script_count = response.text.count('<script')
                if script_count == 0:
                    error_detail = "Página sin JavaScript - definitivamente señuelo"
                elif 'captcha' in response.text.lower():
                    error_detail = "CAPTCHA detectado en la página"
                elif 'blocked' in response.text.lower():
                    error_detail = "Mensaje de bloqueo detectado"
                else:
                    error_detail = f"Estructura desconocida (scripts: {script_count})"
                
                raise DirectDownloadLinkException(f"No se pudo encontrar el bloque 'window.Fl'. {error_detail}. Revisa el análisis HTML en los logs.")
            
            print(f"FIRELOAD/ENHANCED: ✅ Enlace intermedio encontrado: {intermediate_link}")

            # === CAPTURA DE REDIRECCIÓN MEJORADA ===
            
            # Simular pausa humana antes del "clic"
            click_delay = random.uniform(1, 3)
            print(f"FIRELOAD/ENHANCED: Simulando clic humano (pausa {click_delay:.1f}s)...")
            time.sleep(click_delay)
            
            # Headers para simular clic en descarga
            session.headers.update({
                'Referer': url,
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1'
            })
            
            print("FIRELOAD/ENHANCED: Capturando la redirección final...")
            final_response = session.get(intermediate_link, allow_redirects=False, timeout=20)

            if final_response.status_code in [301, 302, 307, 308]:
                direct_link = final_response.headers.get('Location')
                if direct_link:
                    print(f"FIRELOAD/ENHANCED: 🎉 ¡VICTORIA TOTAL! Enlace final: {direct_link}")
                    return direct_link
                else:
                    raise DirectDownloadLinkException("Redirección sin header Location")
            
            elif final_response.status_code == 200:
                # Verificar si es descarga directa
                content_type = final_response.headers.get('content-type', '').lower()
                if 'video' in content_type or 'octet-stream' in content_type:
                    print(f"FIRELOAD/ENHANCED: 🎉 Descarga directa: {intermediate_link}")
                    return intermediate_link
            
            raise DirectDownloadLinkException(f"Respuesta inesperada: {final_response.status_code}")

        except DirectDownloadLinkException:
            raise
        except Exception as e:
            error_message = f"Error crítico: {type(e).__name__} - {e}"
            print(f"FIRELOAD/ENHANCED: {error_message}")
            raise DirectDownloadLinkException(error_message)

# Función de testing mejorada
def test_fireload_enhanced():
    """Prueba el método mejorado con diagnóstico avanzado"""
    test_url = "https://www.fireload.com/9b0c659426249190/Dragon_Ball_(1986)_-_S00E01_-_El_Cuerpo_de_Bomberos.mkv"
    
    print("🚀 INICIANDO PRUEBA CON MÉTODO MEJORADO")
    print("=" * 60)
    
    try:
        start = time.time()
        result = fireload(test_url)
        end = time.time()
        
        print("=" * 60)
        print("🎉 ¡ÉXITO COMPLETO!")
        print(f"⏱️  Tiempo: {end-start:.2f}s")
        print(f"🔗 Enlace: {result}")
        print("=" * 60)
        return result
        
    except Exception as e:
        print("=" * 60)
        print("❌ FALLÓ LA PRUEBA")
        print(f"❌ Error: {e}")
        
        # Diagnóstico específico
        if "señuelo" in str(e).lower():
            print("🔍 DIAGNÓSTICO: Fireload detectó el bot y envió página falsa")
            print("💡 SOLUCIÓN: Necesitamos técnicas más avanzadas o cambiar IP")
        elif "captcha" in str(e).lower():
            print("🔍 DIAGNÓSTICO: CAPTCHA activado")
        elif "403" in str(e) or "blocked" in str(e).lower():
            print("🔍 DIAGNÓSTICO: IP o User-Agent bloqueado")
        else:
            print("🔍 DIAGNÓSTICO: Error técnico o cambio en Fireload")
        
        print("=" * 60)
        return None

# Para probar:
# result = test_fireload_enhanced()





def get_captcha_token(session, params):
    recaptcha_api = "https://www.google.com/recaptcha/api2"
    res = session.get(f"{recaptcha_api}/anchor", params=params)
    anchor_html = HTML(res.text)
    if not (anchor_token := anchor_html.xpath('//input[@id="recaptcha-token"]/@value')):
        return None
    params["c"] = anchor_token[0]
    params["reason"] = "q"
    res = session.post(f"{recaptcha_api}/reload", params=params)
    if token := findall(r'"rresp","(.*?)"', res.text):
        return token[0]


def buzzheavier(url):
    """
    Generate a direct download link for buzzheavier URLs.
    @param link: URL from buzzheavier
    @return: Direct download link
    """
    pattern = r'^https?://buzzheavier\.com/[a-zA-Z0-9]+$'
    if not match(pattern, url):
        return url
    def _bhscraper(url, folder=False):
        session = Session()
        if "/download" not in url:
            url += "/download"
        url = url.strip()
        session.headers.update(
            {
                "referer": url.split("/download")[0],
                "hx-current-url": url.split("/download")[0],
                "hx-request": "true",
                "priority": "u=1, i",
            }
        )
        try:
            response = session.get(url)
            d_url = response.headers.get("Hx-Redirect")
            if not d_url:
                if not folder:
                    raise DirectDownloadLinkException(f"ERROR: Gagal mendapatkan data")
                return
            return d_url
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {str(e)}") from e

    with Session() as session:
        tree = HTML(session.get(url).text)
        if link := tree.xpath("//a[contains(@class, 'link-button') and contains(@class, 'gay-button')]/@hx-get"):
            return _bhscraper("https://buzzheavier.com" + link[0])
        elif folders := tree.xpath("//tbody[@id='tbody']/tr"):
            details = {"contents": [], "title": "", "total_size": 0}
            for data in folders:
                try:
                    filename = data.xpath(".//a")[0].text.strip()
                    _id = data.xpath(".//a")[0].attrib.get("href", "").strip()
                    size = data.xpath(".//td[@class='text-center']/text()")[0].strip()
                    url = _bhscraper(f"https://buzzheavier.com{_id}", True)
                    item = {
                        "path": "",
                        "filename": filename,
                        "url": url,
                        }            
                    details["contents"].append(item) 
                    size = speed_string_to_bytes(size)
                    details["total_size"] += size
                except:
                    continue
            details["title"] = tree.xpath("//span/text()")[0].strip()
            return details
        else:
            raise DirectDownloadLinkException("ERROR: No download link found")


def fuckingfast_dl(url):
    """
    Generate a direct download link for fuckingfast.co URLs.
    @param url: URL from fuckingfast.co
    @return: Direct download link
    """
    url = url.strip()

    try:
        response = get(url)
        content = response.text
        pattern = r'window\.open\((["\'])(https://fuckingfast\.co/dl/[^"\']+)\1'
        match = search(pattern, content)

        if not match:
            raise DirectDownloadLinkException(
                "ERROR: Could not find download link in page"
            )

        direct_url = match.group(2)
        return direct_url

    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {str(e)}") from e


def lulacloud(url):
    """
    Generate a direct download link for www.lulacloud.com URLs.
    @param url: URL from www.lulacloud.com
    @return: Direct download link
    """
    try:
        res = post(url, headers={"Referer": url}, allow_redirects=False)
        return res.headers["location"]
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {str(e)}") from e


def devuploads(url):
    """
    Generate a direct download link for devuploads.com URLs.
    @param url: URL from devuploads.com
    @return: Direct download link
    """
    with Session() as session:
        res = session.get(url)
        html = HTML(res.text)
        if not html.xpath("//input[@name]"):
            raise DirectDownloadLinkException("ERROR: Unable to find link data")
        data = {i.get("name"): i.get("value") for i in html.xpath("//input[@name]")}
        res = session.post("https://gujjukhabar.in/", data=data)
        html = HTML(res.text)
        if not html.xpath("//input[@name]"):
            raise DirectDownloadLinkException("ERROR: Unable to find link data")
        data = {i.get("name"): i.get("value") for i in html.xpath("//input[@name]")}
        resp = session.get(
            "https://du2.devuploads.com/dlhash.php",
            headers={
                "Origin": "https://gujjukhabar.in",
                "Referer": "https://gujjukhabar.in/",
            },
        )
        if not resp.text:
            raise DirectDownloadLinkException("ERROR: Unable to find ipp value")
        data["ipp"] = resp.text.strip()
        if not data.get("rand"):
            raise DirectDownloadLinkException("ERROR: Unable to find rand value")
        randpost = session.post(
            "https://devuploads.com/token/token.php",
            data={"rand": data["rand"], "msg": ""},
            headers={
                "Origin": "https://gujjukhabar.in",
                "Referer": "https://gujjukhabar.in/",
            },
        )
        if not randpost:
            raise DirectDownloadLinkException("ERROR: Unable to find xd value")
        data["xd"] = randpost.text.strip()
        res = session.post(url, data=data)
        html = HTML(res.text)
        if not html.xpath("//input[@name='orilink']/@value"):
            raise DirectDownloadLinkException("ERROR: Unable to find Direct Link")
        direct_link = html.xpath("//input[@name='orilink']/@value")
        return direct_link[0]

def uploadhaven(url):
    """
    Generate a direct download link for uploadhaven.com URLs.
    @param url: URL from uploadhaven.com
    @return: Direct download link
    """
    try:
        res = get(url,headers={'Referer':'http://steamunlocked.net/'})
        html = HTML(res.text)
        if not html.xpath('//form[@method="POST"]//input'):
            raise DirectDownloadLinkException("ERROR: Unable to find link data")        
        data = {i.get("name"): i.get("value") for i in html.xpath('//form[@method="POST"]//input')}
        sleep(15)
        res = post(url, data=data, headers={'Referer': url}, cookies=res.cookies)
        html = HTML(res.text)
        if not html.xpath('//div[@class="alert alert-success mb-0"]//a'):
            raise DirectDownloadLinkException("ERROR: Unable to find link data")
        a = html.xpath('//div[@class="alert alert-success mb-0"]//a')[0]
        return a.get('href')
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {str(e)}") from e

def mediafile(url):
    """
    Generate a direct download link for mediafile.cc URLs.
    @param url: URL from mediafile.cc
    @return: Direct download link
    """
    try:
        res = get(url, allow_redirects=True)
        match = search(r"href='([^']+)'", res.text)
        if not match:
            raise DirectDownloadLinkException("ERROR: Unable to find link data")        
        download_url = match.group(1)
        sleep(60)
        res = get(download_url, headers={'Referer': url}, cookies=res.cookies)
        postvalue = search(r'showFileInformation(.*);', res.text)
        if not postvalue:
            raise DirectDownloadLinkException("ERROR: Unable to find post value")       
        postid = postvalue.group(1).replace('(','').replace(')','')
        response = post('https://mediafile.cc/account/ajax/file_details',data={"u": postid}, headers={"X-Requested-With": "XMLHttpRequest"})
        html = response.json()['html']
        return [i for i in findall(r'https://[^\s"\']+', html) if 'download_token' in i][1]
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {str(e)}") from e

def mediafire(url, session=None):
    if "/folder/" in url:
        return mediafireFolder(url)
    if "::" in url:
        _password = url.split("::")[-1]
        url = url.split("::")[-2]
    else:
        _password = ""
    if final_link := findall(
        r"https?:\/\/download\d+\.mediafire\.com\/\S+\/\S+\/\S+", url
    ):
        return final_link[0]

    def _repair_download(url, session):
        try:
            html = HTML(session.get(url).text)
            if new_link := html.xpath('//a[@id="continue-btn"]/@href'):
                return mediafire(f"https://mediafire.com/{new_link[0]}")
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e

    if session is None:
        session = create_scraper()
        parsed_url = urlparse(url)
        url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
    try:
        html = HTML(session.get(url).text)
    except Exception as e:
        session.close()
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if error := html.xpath('//p[@class="notranslate"]/text()'):
        session.close()
        raise DirectDownloadLinkException(f"ERROR: {error[0]}")
    if html.xpath("//div[@class='passwordPrompt']"):
        if not _password:
            session.close()
            raise DirectDownloadLinkException(
                f"ERROR: {PASSWORD_ERROR_MESSAGE}".format(url)
            )
        try:
            html = HTML(session.post(url, data={"downloadp": _password}).text)
        except Exception as e:
            session.close()
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if html.xpath("//div[@class='passwordPrompt']"):
            session.close()
            raise DirectDownloadLinkException("ERROR: Wrong password.")
    if not (final_link := html.xpath('//a[@aria-label="Download file"]/@href')):
        if repair_link := html.xpath("//a[@class='retry']/@href"):
            return _repair_download(repair_link[0], session)
        raise DirectDownloadLinkException(
            "ERROR: No links found in this page Try Again"
        )
    if final_link[0].startswith("//"):
        final_url = f"https://{final_link[0][2:]}"
        if _password:
            final_url += f"::{_password}"
        return mediafire(final_url, session)
    session.close()
    return final_link[0]


def osdn(url):
    with create_scraper() as session:
        try:
            html = HTML(session.get(url).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if not (direct_link := html.xapth('//a[@class="mirror_link"]/@href')):
            raise DirectDownloadLinkException("ERROR: Direct link not found")
        return f"https://osdn.net{direct_link[0]}"


def yandex_disk(url: str) -> str:
    """Yandex.Disk direct link generator
    Based on https://github.com/wldhx/yadisk-direct"""
    try:
        link = findall(r"\b(https?://(yadi\.sk|disk\.yandex\.(com|ru))\S+)", url)[0][0]
    except IndexError:
        return "No Yandex.Disk links found\n"
    api = "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}"
    try:
        return get(api.format(link)).json()["href"]
    except KeyError as e:
        raise DirectDownloadLinkException(
            "ERROR: File not found/Download limit reached"
        ) from e


def github(url):
    """GitHub direct links generator"""
    try:
        findall(r"\bhttps?://.*github\.com.*releases\S+", url)[0]
    except IndexError as e:
        raise DirectDownloadLinkException("No GitHub Releases links found") from e
    with create_scraper() as session:
        _res = session.get(url, stream=True, allow_redirects=False)
        if "location" in _res.headers:
            return _res.headers["location"]
        raise DirectDownloadLinkException("ERROR: Can't extract the link")


def hxfile(url):
    if not ospath.isfile("hxfile.txt"):
        raise DirectDownloadLinkException("ERROR: hxfile.txt (cookies) Not Found!")
    try:
        jar = MozillaCookieJar()
        jar.load("hxfile.txt")
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    cookies = {cookie.name: cookie.value for cookie in jar}
    try:
        if url.strip().endswith(".html"):
            url = url[:-5]
        file_code = url.split("/")[-1]
        html = HTML(
            post(
                url,
                data={"op": "download2", "id": file_code},
                cookies=cookies,
            ).text
        )
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if direct_link := html.xpath("//a[@class='btn btn-dow']/@href"):
        header = [f"Referer: {url}"]
        return direct_link[0], header
    raise DirectDownloadLinkException("ERROR: Direct download link not found")


def onedrive(link):
    """Onedrive direct link generator
    By https://github.com/junedkh"""
    with create_scraper() as session:
        try:
            link = session.get(link).url
            parsed_link = urlparse(link)
            link_data = parse_qs(parsed_link.query)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if not link_data:
            raise DirectDownloadLinkException("ERROR: Unable to find link_data")
        folder_id = link_data.get("resid")
        if not folder_id:
            raise DirectDownloadLinkException("ERROR: folder id not found")
        folder_id = folder_id[0]
        authkey = link_data.get("authkey")
        if not authkey:
            raise DirectDownloadLinkException("ERROR: authkey not found")
        authkey = authkey[0]
        boundary = uuid4()
        headers = {"content-type": f"multipart/form-data;boundary={boundary}"}
        data = f"--{boundary}\r\nContent-Disposition: form-data;name=data\r\nPrefer: Migration=EnableRedirect;FailOnMigratedFiles\r\nX-HTTP-Method-Override: GET\r\nContent-Type: application/json\r\n\r\n--{boundary}--"
        try:
            resp = session.get(
                f'https://api.onedrive.com/v1.0/drives/{folder_id.split("!", 1)[0]}/items/{folder_id}?$select=id,@content.downloadUrl&ump=1&authKey={authkey}',
                headers=headers,
                data=data,
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if "@content.downloadUrl" not in resp:
        raise DirectDownloadLinkException("ERROR: Direct link not found")
    return resp["@content.downloadUrl"]


def pixeldrain(url):
    try:
        url = url.rstrip("/")
        code = url.split("/")[-1].split("?", 1)[0]
        response = get("https://pd.cybar.xyz/", allow_redirects=True)
        return response.url + code
    except Exception as e:
        raise DirectDownloadLinkException("ERROR: Direct link not found")


def streamtape(url):
    splitted_url = url.split("/")
    _id = splitted_url[4] if len(splitted_url) >= 6 else splitted_url[-1]
    try:
        html = HTML(get(url).text)
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    script = html.xpath(
        "//script[contains(text(),'ideoooolink')]/text()"
    ) or html.xpath("//script[contains(text(),'ideoolink')]/text()")
    if not script:
        raise DirectDownloadLinkException("ERROR: requeries script not found")
    if not (link := findall(r"(&expires\S+)'", script[0])):
        raise DirectDownloadLinkException("ERROR: Download link not found")
    return f"https://streamtape.com/get_video?id={_id}{link[-1]}"


def racaty(url):
    with create_scraper() as session:
        try:
            url = session.get(url).url
            json_data = {"op": "download2", "id": url.split("/")[-1]}
            html = HTML(session.post(url, data=json_data).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if direct_link := html.xpath("//a[@id='uniqueExpirylink']/@href"):
        return direct_link[0]
    else:
        raise DirectDownloadLinkException("ERROR: Direct link not found")


def fichier(link):
    """1Fichier direct link generator
    Based on https://github.com/Maujar
    """
    regex = r"^([http:\/\/|https:\/\/]+)?.*1fichier\.com\/\?.+"
    gan = match(regex, link)
    if not gan:
        raise DirectDownloadLinkException("ERROR: The link you entered is wrong!")
    if "::" in link:
        pswd = link.split("::")[-1]
        url = link.split("::")[-2]
    else:
        pswd = None
        url = link
    cget = create_scraper().request
    try:
        if pswd is None:
            req = cget("post", url)
        else:
            pw = {"pass": pswd}
            req = cget("post", url, data=pw)
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if req.status_code == 404:
        raise DirectDownloadLinkException(
            "ERROR: File not found/The link you entered is wrong!"
        )
    html = HTML(req.text)
    if dl_url := html.xpath('//a[@class="ok btn-general btn-orange"]/@href'):
        return dl_url[0]
    if not (ct_warn := html.xpath('//div[@class="ct_warn"]')):
        raise DirectDownloadLinkException(
            "ERROR: Error trying to generate Direct Link from 1fichier!"
        )
    if len(ct_warn) == 3:
        str_2 = ct_warn[-1].text
        if "you must wait" in str_2.lower():
            if numbers := [int(word) for word in str_2.split() if word.isdigit()]:
                raise DirectDownloadLinkException(
                    f"ERROR: 1fichier is on a limit. Please wait {numbers[0]} minute."
                )
            else:
                raise DirectDownloadLinkException(
                    "ERROR: 1fichier is on a limit. Please wait a few minutes/hour."
                )
        elif "protect access" in str_2.lower():
            raise DirectDownloadLinkException(
                f"ERROR:\n{PASSWORD_ERROR_MESSAGE.format(link)}"
            )
        else:
            raise DirectDownloadLinkException(
                "ERROR: Failed to generate Direct Link from 1fichier!"
            )
    elif len(ct_warn) == 4:
        str_1 = ct_warn[-2].text
        str_3 = ct_warn[-1].text
        if "you must wait" in str_1.lower():
            if numbers := [int(word) for word in str_1.split() if word.isdigit()]:
                raise DirectDownloadLinkException(
                    f"ERROR: 1fichier is on a limit. Please wait {numbers[0]} minute."
                )
            else:
                raise DirectDownloadLinkException(
                    "ERROR: 1fichier is on a limit. Please wait a few minutes/hour."
                )
        elif "bad password" in str_3.lower():
            raise DirectDownloadLinkException(
                "ERROR: The password you entered is wrong!"
            )
    raise DirectDownloadLinkException(
        "ERROR: Error trying to generate Direct Link from 1fichier!"
    )


def solidfiles(url):
    """Solidfiles direct link generator
    Based on https://github.com/Xonshiz/SolidFiles-Downloader
    By https://github.com/Jusidama18"""
    with create_scraper() as session:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
            }
            pageSource = session.get(url, headers=headers).text
            mainOptions = str(
                search(r"viewerOptions\'\,\ (.*?)\)\;", pageSource).group(1)
            )
            return loads(mainOptions)["downloadUrl"]
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e


def krakenfiles(url):
    with Session() as session:
        try:
            _res = session.get(url)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        html = HTML(_res.text)
        if post_url := html.xpath('//form[@id="dl-form"]/@action'):
            post_url = f"https://krakenfiles.com{post_url[0]}"
        else:
            raise DirectDownloadLinkException("ERROR: Unable to find post link.")
        if token := html.xpath('//input[@id="dl-token"]/@value'):
            data = {"token": token[0]}
        else:
            raise DirectDownloadLinkException("ERROR: Unable to find token for post.")
        try:
            _json = session.post(post_url, data=data).json()
        except Exception as e:
            raise DirectDownloadLinkException(
                f"ERROR: {e.__class__.__name__} While send post request"
            ) from e
    if _json["status"] != "ok":
        raise DirectDownloadLinkException(
            "ERROR: Unable to find download after post request"
        )
    return _json["url"]


def uploadee(url):
    with create_scraper() as session:
        try:
            html = HTML(session.get(url).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if link := html.xpath("//a[@id='d_l']/@href"):
        return link[0]
    else:
        raise DirectDownloadLinkException("ERROR: Direct Link not found")


def terabox(url):
    if "/file/" in url:
        return url
    api_url = f"https://wdzone-terabox-api.vercel.app/api?url={quote(url)}"
    try:
        with Session() as session:
            req = session.get(api_url, headers={"User-Agent": user_agent}).json()
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e

    details = {"contents": [], "title": "", "total_size": 0}
    if "✅ Status" in req:
        for data in req["📜 Extracted Info"]:
            item = {
                "path": "",
                "filename": data["📂 Title"],
                "url": data["🔽 Direct Download Link"],
                }       
            details["contents"].append(item)
            size = (data["📏 Size"]).replace(" ", "")
            size = speed_string_to_bytes(size)
            details["total_size"] += size
        details["title"] = req["📜 Extracted Info"][0]["📂 Title"]
        if len(details["contents"]) == 1:
            return details["contents"][0]["url"]
        return details
    else:
        raise DirectDownloadLinkException("ERROR: File not found!")


def filepress(url):
    with create_scraper() as session:
        try:
            url = session.get(url).url
            raw = urlparse(url)
            json_data = {
                "id": raw.path.split("/")[-1],
                "method": "publicDownlaod",
            }
            api = f"{raw.scheme}://{raw.hostname}/api/file/downlaod/"
            res2 = session.post(
                api,
                headers={"Referer": f"{raw.scheme}://{raw.hostname}"},
                json=json_data,
            ).json()
            json_data2 = {
                "id": res2["data"],
                "method": "publicUserDownlaod",
            }
            api2 = "https://new2.filepress.store/api/file/downlaod2/"
            res = session.post(
                api2,
                headers={"Referer": f"{raw.scheme}://{raw.hostname}"},
                json=json_data2,
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if "data" not in res:
        raise DirectDownloadLinkException(f'ERROR: {res["statusText"]}')
    return f'https://drive.google.com/uc?id={res["data"]}&export=download'


def gdtot(url):
    cget = create_scraper().request
    try:
        res = cget("GET", f'https://gdtot.pro/file/{url.split("/")[-1]}')
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    token_url = HTML(res.text).xpath(
        "//a[contains(@class,'inline-flex items-center justify-center')]/@href"
    )
    if not token_url:
        try:
            url = cget("GET", url).url
            p_url = urlparse(url)
            res = cget(
                "GET", f"{p_url.scheme}://{p_url.hostname}/ddl/{url.split('/')[-1]}"
            )
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if (
            drive_link := findall(r"myDl\('(.*?)'\)", res.text)
        ) and "drive.google.com" in drive_link[0]:
            return drive_link[0]
        else:
            raise DirectDownloadLinkException(
                "ERROR: Drive Link not found, Try in your broswer"
            )
    token_url = token_url[0]
    try:
        token_page = cget("GET", token_url)
    except Exception as e:
        raise DirectDownloadLinkException(
            f"ERROR: {e.__class__.__name__} with {token_url}"
        ) from e
    path = findall(r'\("(.*?)"\)', token_page.text)
    if not path:
        raise DirectDownloadLinkException("ERROR: Cannot bypass this")
    path = path[0]
    raw = urlparse(token_url)
    final_url = f"{raw.scheme}://{raw.hostname}{path}"
    return sharer_scraper(final_url)


def sharer_scraper(url):
    cget = create_scraper().request
    try:
        url = cget("GET", url).url
        raw = urlparse(url)
        header = {
            "useragent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10"
        }
        res = cget("GET", url, headers=header)
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    key = findall(r'"key",\s+"(.*?)"', res.text)
    if not key:
        raise DirectDownloadLinkException("ERROR: Key not found!")
    key = key[0]
    if not HTML(res.text).xpath("//button[@id='drc']"):
        raise DirectDownloadLinkException(
            "ERROR: This link don't have direct download button"
        )
    boundary = uuid4()
    headers = {
        "Content-Type": f"multipart/form-data; boundary=----WebKitFormBoundary{boundary}",
        "x-token": raw.hostname,
        "useragent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10",
    }

    data = (
        f'------WebKitFormBoundary{boundary}\r\nContent-Disposition: form-data; name="action"\r\n\r\ndirect\r\n'
        f'------WebKitFormBoundary{boundary}\r\nContent-Disposition: form-data; name="key"\r\n\r\n{key}\r\n'
        f'------WebKitFormBoundary{boundary}\r\nContent-Disposition: form-data; name="action_token"\r\n\r\n\r\n'
        f"------WebKitFormBoundary{boundary}--\r\n"
    )
    try:
        res = cget("POST", url, cookies=res.cookies, headers=headers, data=data).json()
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if "url" not in res:
        raise DirectDownloadLinkException(
            "ERROR: Drive Link not found, Try in your broswer"
        )
    if "drive.google.com" in res["url"] or "drive.usercontent.google.com" in res["url"]:
        return res["url"]
    try:
        res = cget("GET", res["url"])
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if (drive_link := HTML(res.text).xpath("//a[contains(@class,'btn')]/@href")) and (
        "drive.google.com" in drive_link[0]
        or "drive.usercontent.google.com" in drive_link[0]
    ):
        return drive_link[0]
    else:
        raise DirectDownloadLinkException(
            "ERROR: Drive Link not found, Try in your broswer"
        )


def wetransfer(url):
    with create_scraper() as session:
        try:
            url = session.get(url).url
            splited_url = url.split("/")
            json_data = {"security_hash": splited_url[-1], "intent": "entire_transfer"}
            res = session.post(
                f"https://wetransfer.com/api/v4/transfers/{splited_url[-2]}/download",
                json=json_data,
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if "direct_link" in res:
        return res["direct_link"]
    elif "message" in res:
        raise DirectDownloadLinkException(f"ERROR: {res['message']}")
    elif "error" in res:
        raise DirectDownloadLinkException(f"ERROR: {res['error']}")
    else:
        raise DirectDownloadLinkException("ERROR: cannot find direct link")


def akmfiles(url):
    with create_scraper() as session:
        try:
            html = HTML(
                session.post(
                    url,
                    data={"op": "download2", "id": url.split("/")[-1]},
                ).text
            )
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if direct_link := html.xpath("//a[contains(@class,'btn btn-dow')]/@href"):
        return direct_link[0]
    else:
        raise DirectDownloadLinkException("ERROR: Direct link not found")


def shrdsk(url):
    with create_scraper() as session:
        try:
            _json = session.get(
                f'https://us-central1-affiliate2apk.cloudfunctions.net/get_data?shortid={url.split("/")[-1]}',
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if "download_data" not in _json:
            raise DirectDownloadLinkException("ERROR: Download data not found")
        try:
            _res = session.get(
                f"https://shrdsk.me/download/{_json['download_data']}",
                allow_redirects=False,
            )
            if "Location" in _res.headers:
                return _res.headers["Location"]
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    raise DirectDownloadLinkException("ERROR: cannot find direct link in headers")


def linkBox(url: str):
    parsed_url = urlparse(url)
    try:
        shareToken = parsed_url.path.split("/")[-1]
    except:
        raise DirectDownloadLinkException("ERROR: invalid URL")

    details = {"contents": [], "title": "", "total_size": 0}

    def __singleItem(session, itemId):
        try:
            _json = session.get(
                "https://www.linkbox.to/api/file/detail",
                params={"itemId": itemId},
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        data = _json["data"]
        if not data:
            if "msg" in _json:
                raise DirectDownloadLinkException(f"ERROR: {_json['msg']}")
            raise DirectDownloadLinkException("ERROR: data not found")
        itemInfo = data["itemInfo"]
        if not itemInfo:
            raise DirectDownloadLinkException("ERROR: itemInfo not found")
        filename = itemInfo["name"]
        sub_type = itemInfo.get("sub_type")
        if sub_type and not filename.strip().endswith(sub_type):
            filename += f".{sub_type}"
        if not details["title"]:
            details["title"] = filename
        item = {
            "path": "",
            "filename": filename,
            "url": itemInfo["url"],
        }
        if "size" in itemInfo:
            size = itemInfo["size"]
            if isinstance(size, str) and size.isdigit():
                size = float(size)
            details["total_size"] += size
        details["contents"].append(item)

    def __fetch_links(session, _id=0, folderPath=""):
        params = {
            "shareToken": shareToken,
            "pageSize": 1000,
            "pid": _id,
        }
        try:
            _json = session.get(
                "https://www.linkbox.to/api/file/share_out_list",
                params=params,
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        data = _json["data"]
        if not data:
            if "msg" in _json:
                raise DirectDownloadLinkException(f"ERROR: {_json['msg']}")
            raise DirectDownloadLinkException("ERROR: data not found")
        try:
            if data["shareType"] == "singleItem":
                return __singleItem(session, data["itemId"])
        except:
            pass
        if not details["title"]:
            details["title"] = data["dirName"]
        contents = data["list"]
        if not contents:
            return None
        for content in contents:
            if content["type"] == "dir" and "url" not in content:
                if not folderPath:
                    newFolderPath = ospath.join(details["title"], content["name"])
                else:
                    newFolderPath = ospath.join(folderPath, content["name"])
                if not details["title"]:
                    details["title"] = content["name"]
                __fetch_links(session, content["id"], newFolderPath)
            elif "url" in content:
                if not folderPath:
                    folderPath = details["title"]
                filename = content["name"]
                if (
                    sub_type := content.get("sub_type")
                ) and not filename.strip().endswith(sub_type):
                    filename += f".{sub_type}"
                item = {
                    "path": ospath.join(folderPath),
                    "filename": filename,
                    "url": content["url"],
                }
                if "size" in content:
                    size = content["size"]
                    if isinstance(size, str) and size.isdigit():
                        size = float(size)
                    details["total_size"] += size
                details["contents"].append(item)

    try:
        with Session() as session:
            __fetch_links(session)
    except DirectDownloadLinkException as e:
        raise e
    return details


def gofile(url):
    try:
        if "::" in url:
            _password = url.split("::")[-1]
            _password = sha256(_password.encode("utf-8")).hexdigest()
            url = url.split("::")[-2]
        else:
            _password = ""
        _id = url.split("/")[-1]
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}")

    def __get_token(session):
        headers = {
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "*/*",
            "Connection": "keep-alive",
        }
        __url = "https://api.gofile.io/accounts"
        try:
            __res = session.post(__url, headers=headers).json()
            if __res["status"] != "ok":
                raise DirectDownloadLinkException("ERROR: Failed to get token.")
            return __res["data"]["token"]
        except Exception as e:
            raise e

    def __fetch_links(session, _id, folderPath=""):
        _url = f"https://api.gofile.io/contents/{_id}?wt=4fd6sg89d7s6&cache=true"
        headers = {
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Authorization": "Bearer" + " " + token,
        }
        if _password:
            _url += f"&password={_password}"
        try:
            _json = session.get(_url, headers=headers).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}")
        if _json["status"] in "error-passwordRequired":
            raise DirectDownloadLinkException(
                f"ERROR:\n{PASSWORD_ERROR_MESSAGE.format(url)}"
            )
        if _json["status"] in "error-passwordWrong":
            raise DirectDownloadLinkException("ERROR: This password is wrong !")
        if _json["status"] in "error-notFound":
            raise DirectDownloadLinkException(
                "ERROR: File not found on gofile's server"
            )
        if _json["status"] in "error-notPublic":
            raise DirectDownloadLinkException("ERROR: This folder is not public")

        data = _json["data"]

        if not details["title"]:
            details["title"] = data["name"] if data["type"] == "folder" else _id

        contents = data["children"]
        for content in contents.values():
            if content["type"] == "folder":
                if not content["public"]:
                    continue
                if not folderPath:
                    newFolderPath = ospath.join(details["title"], content["name"])
                else:
                    newFolderPath = ospath.join(folderPath, content["name"])
                __fetch_links(session, content["id"], newFolderPath)
            else:
                if not folderPath:
                    folderPath = details["title"]
                item = {
                    "path": ospath.join(folderPath),
                    "filename": content["name"],
                    "url": content["link"],
                }
                if "size" in content:
                    size = content["size"]
                    if isinstance(size, str) and size.isdigit():
                        size = float(size)
                    details["total_size"] += size
                details["contents"].append(item)

    details = {"contents": [], "title": "", "total_size": 0}
    with Session() as session:
        try:
            token = __get_token(session)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}")
        details["header"] = [f"Cookie: accountToken={token}"]
        try:
            __fetch_links(session, _id)
        except Exception as e:
            raise DirectDownloadLinkException(e)

    if len(details["contents"]) == 1:
        return (details["contents"][0]["url"], details["header"])
    return details


def mediafireFolder(url):
    if "::" in url:
        _password = url.split("::")[-1]
        url = url.split("::")[-2]
    else:
        _password = ""
    try:
        raw = url.split("/", 4)[-1]
        folderkey = raw.split("/", 1)[0]
        folderkey = folderkey.split(",")
    except:
        raise DirectDownloadLinkException("ERROR: Could not parse ")
    if len(folderkey) == 1:
        folderkey = folderkey[0]
    details = {"contents": [], "title": "", "total_size": 0, "header": ""}

    session = create_scraper()
    adapter = HTTPAdapter(
        max_retries=Retry(total=10, read=10, connect=10, backoff_factor=0.3)
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session = create_scraper(
        browser={"browser": "firefox", "platform": "windows", "mobile": False},
        delay=10,
        sess=session,
    )
    folder_infos = []

    def __get_info(folderkey):
        try:
            if isinstance(folderkey, list):
                folderkey = ",".join(folderkey)
            _json = session.post(
                "https://www.mediafire.com/api/1.5/folder/get_info.php",
                data={
                    "recursive": "yes",
                    "folder_key": folderkey,
                    "response_format": "json",
                },
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(
                f"ERROR: {e.__class__.__name__} While getting info"
            )
        _res = _json["response"]
        if "folder_infos" in _res:
            folder_infos.extend(_res["folder_infos"])
        elif "folder_info" in _res:
            folder_infos.append(_res["folder_info"])
        elif "message" in _res:
            raise DirectDownloadLinkException(f"ERROR: {_res['message']}")
        else:
            raise DirectDownloadLinkException("ERROR: something went wrong!")

    try:
        __get_info(folderkey)
    except Exception as e:
        raise DirectDownloadLinkException(e)

    details["title"] = folder_infos[0]["name"]

    def __scraper(url):
        session = create_scraper()
        parsed_url = urlparse(url)
        url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

        def __repair_download(url):
            try:
                html = HTML(session.get(url).text)
                if new_link := html.xpath('//a[@id="continue-btn"]/@href'):
                    return __scraper(f"https://mediafire.com/{new_link[0]}")
            except:
                return None

        try:
            html = HTML(session.get(url).text)
        except:
            return None
        if html.xpath("//div[@class='passwordPrompt']"):
            if not _password:
                raise DirectDownloadLinkException(
                    f"ERROR: {PASSWORD_ERROR_MESSAGE}".format(url)
                )
            try:
                html = HTML(session.post(url, data={"downloadp": _password}).text)
            except:
                return None
            if html.xpath("//div[@class='passwordPrompt']"):
                return None
        if final_link := html.xpath('//a[@aria-label="Download file"]/@href'):
            if final_link[0].startswith("//"):
                return __scraper(f"https://{final_link[0][2:]}")
            return final_link[0]
        if repair_link := html.xpath("//a[@class='retry']/@href"):
            return __repair_download(repair_link[0])

    def __get_content(folderKey, folderPath="", content_type="folders"):
        try:
            params = {
                "content_type": content_type,
                "folder_key": folderKey,
                "response_format": "json",
            }
            _json = session.get(
                "https://www.mediafire.com/api/1.5/folder/get_content.php",
                params=params,
            ).json()
        except Exception as e:
            raise DirectDownloadLinkException(
                f"ERROR: {e.__class__.__name__} While getting content"
            )
        _res = _json["response"]
        if "message" in _res:
            raise DirectDownloadLinkException(f"ERROR: {_res['message']}")
        _folder_content = _res["folder_content"]
        if content_type == "folders":
            folders = _folder_content["folders"]
            for folder in folders:
                if folderPath:
                    newFolderPath = ospath.join(folderPath, folder["name"])
                else:
                    newFolderPath = ospath.join(folder["name"])
                __get_content(folder["folderkey"], newFolderPath)
            __get_content(folderKey, folderPath, "files")
        else:
            files = _folder_content["files"]
            for file in files:
                item = {}
                if not (_url := __scraper(file["links"]["normal_download"])):
                    continue
                item["filename"] = file["filename"]
                if not folderPath:
                    folderPath = details["title"]
                item["path"] = ospath.join(folderPath)
                item["url"] = _url
                if "size" in file:
                    size = file["size"]
                    if isinstance(size, str) and size.isdigit():
                        size = float(size)
                    details["total_size"] += size
                details["contents"].append(item)

    try:
        for folder in folder_infos:
            __get_content(folder["folderkey"], folder["name"])
    except Exception as e:
        raise DirectDownloadLinkException(e)
    finally:
        session.close()
    if len(details["contents"]) == 1:
        return (details["contents"][0]["url"], [details["header"]])
    return details


def cf_bypass(url):
    "DO NOT ABUSE THIS"
    try:
        data = {"cmd": "request.get", "url": url, "maxTimeout": 60000}
        _json = post(
            "https://cf.jmdkh.eu.org/v1",
            headers={"Content-Type": "application/json"},
            json=data,
        ).json()
        if _json["status"] == "ok":
            return _json["solution"]["response"]
    except Exception as e:
        e
    raise DirectDownloadLinkException("ERROR: Con't bypass cloudflare")


def send_cm_file(url, file_id=None):
    if "::" in url:
        _password = url.split("::")[-1]
        url = url.split("::")[-2]
    else:
        _password = ""
    _passwordNeed = False
    with create_scraper() as session:
        if file_id is None:
            try:
                html = HTML(session.get(url).text)
            except Exception as e:
                raise DirectDownloadLinkException(
                    f"ERROR: {e.__class__.__name__}"
                ) from e
            if html.xpath("//input[@name='password']"):
                _passwordNeed = True
            if not (file_id := html.xpath("//input[@name='id']/@value")):
                raise DirectDownloadLinkException("ERROR: file_id not found")
        try:
            data = {"op": "download2", "id": file_id}
            if _password and _passwordNeed:
                data["password"] = _password
            _res = session.post("https://send.cm/", data=data, allow_redirects=False)
            if "Location" in _res.headers:
                return (_res.headers["Location"], ["Referer: https://send.cm/"])
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if _passwordNeed:
            raise DirectDownloadLinkException(
                f"ERROR:\n{PASSWORD_ERROR_MESSAGE.format(url)}"
            )
        raise DirectDownloadLinkException("ERROR: Direct link not found")


def send_cm(url):
    if "/d/" in url:
        return send_cm_file(url)
    elif "/s/" not in url:
        file_id = url.split("/")[-1]
        return send_cm_file(url, file_id)
    splitted_url = url.split("/")
    details = {
        "contents": [],
        "title": "",
        "total_size": 0,
        "header": "Referer: https://send.cm/",
    }
    if len(splitted_url) == 5:
        url += "/"
        splitted_url = url.split("/")
    if len(splitted_url) >= 7:
        details["title"] = splitted_url[5]
    else:
        details["title"] = splitted_url[-1]
    session = Session()

    def __collectFolders(html):
        folders = []
        folders_urls = html.xpath("//h6/a/@href")
        folders_names = html.xpath("//h6/a/text()")
        for folders_url, folders_name in zip(folders_urls, folders_names):
            folders.append(
                {
                    "folder_link": folders_url.strip(),
                    "folder_name": folders_name.strip(),
                }
            )
        return folders

    def __getFile_link(file_id):
        try:
            _res = session.post(
                "https://send.cm/",
                data={"op": "download2", "id": file_id},
                allow_redirects=False,
            )
            if "Location" in _res.headers:
                return _res.headers["Location"]
        except:
            pass

    def __getFiles(html):
        files = []
        hrefs = html.xpath('//tr[@class="selectable"]//a/@href')
        file_names = html.xpath('//tr[@class="selectable"]//a/text()')
        sizes = html.xpath('//tr[@class="selectable"]//span/text()')
        for href, file_name, size_text in zip(hrefs, file_names, sizes):
            files.append(
                {
                    "file_id": href.split("/")[-1],
                    "file_name": file_name.strip(),
                    "size": speed_string_to_bytes(size_text.strip()),
                }
            )
        return files

    def __writeContents(html_text, folderPath=""):
        folders = __collectFolders(html_text)
        for folder in folders:
            _html = HTML(cf_bypass(folder["folder_link"]))
            __writeContents(_html, ospath.join(folderPath, folder["folder_name"]))
        files = __getFiles(html_text)
        for file in files:
            if not (link := __getFile_link(file["file_id"])):
                continue
            item = {"url": link, "filename": file["filename"], "path": folderPath}
            details["total_size"] += file["size"]
            details["contents"].append(item)

    try:
        mainHtml = HTML(cf_bypass(url))
    except DirectDownloadLinkException as e:
        raise e
    except Exception as e:
        raise DirectDownloadLinkException(
            f"ERROR: {e.__class__.__name__} While getting mainHtml"
        )

    try:
        __writeContents(mainHtml, details["title"])
    except DirectDownloadLinkException as e:
        raise e
    except Exception as e:
        raise DirectDownloadLinkException(
            f"ERROR: {e.__class__.__name__} While writing Contents"
        )
    finally:
        session.close()
    if len(details["contents"]) == 1:
        return (details["contents"][0]["url"], [details["header"]])
    return details


def doods(url):
    if "/e/" in url:
        url = url.replace("/e/", "/d/")
    parsed_url = urlparse(url)
    with create_scraper() as session:
        try:
            html = HTML(session.get(url).text)
        except Exception as e:
            raise DirectDownloadLinkException(
                f"ERROR: {e.__class__.__name__} While fetching token link"
            ) from e
        if not (link := html.xpath("//div[@class='download-content']//a/@href")):
            raise DirectDownloadLinkException(
                "ERROR: Token Link not found or maybe not allow to download! open in browser."
            )
        link = f"{parsed_url.scheme}://{parsed_url.hostname}{link[0]}"
        sleep(2)
        try:
            _res = session.get(link)
        except Exception as e:
            raise DirectDownloadLinkException(
                f"ERROR: {e.__class__.__name__} While fetching download link"
            ) from e
    if not (link := search(r"window\.open\('(\S+)'", _res.text)):
        raise DirectDownloadLinkException("ERROR: Download link not found try again")
    return (link.group(1), [f"Referer: {parsed_url.scheme}://{parsed_url.hostname}/"])


def easyupload(url):
    if "::" in url:
        _password = url.split("::")[-1]
        url = url.split("::")[-2]
    else:
        _password = ""
    file_id = url.split("/")[-1]
    with create_scraper() as session:
        try:
            _res = session.get(url)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}")
        first_page_html = HTML(_res.text)
        if (
            first_page_html.xpath("//h6[contains(text(),'Password Protected')]")
            and not _password
        ):
            raise DirectDownloadLinkException(
                f"ERROR:\n{PASSWORD_ERROR_MESSAGE.format(url)}"
            )
        if not (
            match := search(
                r"https://eu(?:[1-9][0-9]?|100)\.easyupload\.io/action\.php", _res.text
            )
        ):
            raise DirectDownloadLinkException(
                "ERROR: Failed to get server for EasyUpload Link"
            )
        action_url = match.group()
        session.headers.update({"referer": "https://easyupload.io/"})
        recaptcha_params = {
            "k": "6LfWajMdAAAAAGLXz_nxz2tHnuqa-abQqC97DIZ3",
            "ar": "1",
            "co": "aHR0cHM6Ly9lYXN5dXBsb2FkLmlvOjQ0Mw..",
            "hl": "en",
            "v": "0hCdE87LyjzAkFO5Ff-v7Hj1",
            "size": "invisible",
            "cb": "c3o1vbaxbmwe",
        }
        if not (captcha_token := get_captcha_token(session, recaptcha_params)):
            raise DirectDownloadLinkException("ERROR: Captcha token not found")
        try:
            data = {
                "type": "download-token",
                "url": file_id,
                "value": _password,
                "captchatoken": captcha_token,
                "method": "regular",
            }
            json_resp = session.post(url=action_url, data=data).json()
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if "download_link" in json_resp:
        return json_resp["download_link"]
    elif "data" in json_resp:
        raise DirectDownloadLinkException(
            f"ERROR: Failed to generate direct link due to {json_resp['data']}"
        )
    raise DirectDownloadLinkException(
        "ERROR: Failed to generate direct link from EasyUpload."
    )


def filelions_and_streamwish(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    scheme = parsed_url.scheme
    if any(
        x in hostname
        for x in [
            "filelions.co",
            "filelions.live",
            "filelions.to",
            "filelions.site",
            "cabecabean.lol",
            "filelions.online",
            "mycloudz.cc",
        ]
    ):
        apiKey = Config.FILELION_API
        apiUrl = "https://vidhideapi.com"
    elif any(
        x in hostname
        for x in [
            "embedwish.com",
            "kissmovies.net",
            "kitabmarkaz.xyz",
            "wishfast.top",
            "streamwish.to",
        ]
    ):
        apiKey = Config.STREAMWISH_API
        apiUrl = "https://api.streamwish.com"
    if not apiKey:
        raise DirectDownloadLinkException(
            f"ERROR: API is not provided get it from {scheme}://{hostname}"
        )
    file_code = url.split("/")[-1]
    quality = ""
    if bool(file_code.strip().endswith(("_o", "_h", "_n", "_l"))):
        spited_file_code = file_code.rsplit("_", 1)
        quality = spited_file_code[1]
        file_code = spited_file_code[0]
    url = f"{scheme}://{hostname}/{file_code}"
    try:
        _res = get(
            f"{apiUrl}/api/file/direct_link",
            params={"key": apiKey, "file_code": file_code, "hls": "1"},
        ).json()
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if _res["status"] != 200:
        raise DirectDownloadLinkException(f"ERROR: {_res['msg']}")
    result = _res["result"]
    if not result["versions"]:
        raise DirectDownloadLinkException("ERROR: File Not Found")
    error = "\nProvide a quality to download the video\nAvailable Quality:"
    for version in result["versions"]:
        if quality == version["name"]:
            return version["url"]
        elif version["name"] == "l":
            error += "\nLow"
        elif version["name"] == "n":
            error += "\nNormal"
        elif version["name"] == "o":
            error += "\nOriginal"
        elif version["name"] == "h":
            error += "\nHD"
        error += f" <code>{url}_{version['name']}</code>"
    raise DirectDownloadLinkException(f"ERROR: {error}")


def streamvid(url: str):
    file_code = url.split("/")[-1]
    parsed_url = urlparse(url)
    url = f"{parsed_url.scheme}://{parsed_url.hostname}/d/{file_code}"
    quality_defined = bool(url.strip().endswith(("_o", "_h", "_n", "_l")))
    with create_scraper() as session:
        try:
            html = HTML(session.get(url).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if quality_defined:
            data = {}
            if not (inputs := html.xpath('//form[@id="F1"]//input')):
                raise DirectDownloadLinkException("ERROR: No inputs found")
            for i in inputs:
                if key := i.get("name"):
                    data[key] = i.get("value")
            try:
                html = HTML(session.post(url, data=data).text)
            except Exception as e:
                raise DirectDownloadLinkException(
                    f"ERROR: {e.__class__.__name__}"
                ) from e
            if not (
                script := html.xpath(
                    '//script[contains(text(),"document.location.href")]/text()'
                )
            ):
                if error := html.xpath(
                    '//div[@class="alert alert-danger"][1]/text()[2]'
                ):
                    raise DirectDownloadLinkException(f"ERROR: {error[0]}")
                raise DirectDownloadLinkException(
                    "ERROR: direct link script not found!"
                )
            if directLink := findall(r'document\.location\.href="(.*)"', script[0]):
                return directLink[0]
            raise DirectDownloadLinkException(
                "ERROR: direct link not found! in the script"
            )
        elif (qualities_urls := html.xpath('//div[@id="dl_versions"]/a/@href')) and (
            qualities := html.xpath('//div[@id="dl_versions"]/a/text()[2]')
        ):
            error = "\nProvide a quality to download the video\nAvailable Quality:"
            for quality_url, quality in zip(qualities_urls, qualities):
                error += f"\n{quality.strip()} <code>{quality_url}</code>"
            raise DirectDownloadLinkException(f"ERROR: {error}")
        elif error := html.xpath('//div[@class="not-found-text"]/text()'):
            raise DirectDownloadLinkException(f"ERROR: {error[0]}")
        raise DirectDownloadLinkException("ERROR: Something went wrong")


def streamhub(url):
    file_code = url.split("/")[-1]
    parsed_url = urlparse(url)
    url = f"{parsed_url.scheme}://{parsed_url.hostname}/d/{file_code}"
    with create_scraper() as session:
        try:
            html = HTML(session.get(url).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if not (inputs := html.xpath('//form[@name="F1"]//input')):
            raise DirectDownloadLinkException("ERROR: No inputs found")
        data = {}
        for i in inputs:
            if key := i.get("name"):
                data[key] = i.get("value")
        session.headers.update({"referer": url})
        sleep(1)
        try:
            html = HTML(session.post(url, data=data).text)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
        if directLink := html.xpath(
            '//a[@class="btn btn-primary btn-go downloadbtn"]/@href'
        ):
            return directLink[0]
        if error := html.xpath('//div[@class="alert alert-danger"]/text()[2]'):
            raise DirectDownloadLinkException(f"ERROR: {error[0]}")
        raise DirectDownloadLinkException("ERROR: direct link not found!")


def pcloud(url):
    with create_scraper() as session:
        try:
            res = session.get(url)
        except Exception as e:
            raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    if link := findall(r".downloadlink.:..(https:.*)..", res.text):
        return link[0].replace(r"\/", "/")
    raise DirectDownloadLinkException("ERROR: Direct link not found")


def tmpsend(url):
    parsed_url = urlparse(url)
    if any(x in parsed_url.path for x in ["thank-you", "download"]):
        query_params = parse_qs(parsed_url.query)
        if file_id := query_params.get("d"):
            file_id = file_id[0]
    elif not (file_id := parsed_url.path.strip("/")):
        raise DirectDownloadLinkException("ERROR: Invalid URL format")
    referer_url = f"https://tmpsend.com/thank-you?d={file_id}"
    header = [f"Referer: {referer_url}"]
    download_link = f"https://tmpsend.com/download?d={file_id}"
    return download_link, header


def qiwi(url):
    """qiwi.gg link generator
    based on https://github.com/aenulrofik"""
    file_id = url.split("/")[-1]
    try:
        res = get(url).text
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    tree = HTML(res)
    if name := tree.xpath('//h1[@class="page_TextHeading__VsM7r"]/text()'):
        ext = name[0].split(".")[-1]
        return f"https://spyderrock.com/{file_id}.{ext}"
    else:
        raise DirectDownloadLinkException("ERROR: File not found")


def mp4upload(url):
    with Session() as session:
        try:
            url = url.replace("embed-", "")
            req = session.get(url).text
            tree = HTML(req)
            inputs = tree.xpath("//input")
            header = ["Referer: https://www.mp4upload.com/"]
            data = {input.get("name"): input.get("value") for input in inputs}
            if not data:
                raise DirectDownloadLinkException("ERROR: File Not Found!")
            post = session.post(
                url,
                data=data,
                headers={
                    "User-Agent": user_agent,
                    "Referer": "https://www.mp4upload.com/",
                },
            ).text
            tree = HTML(post)
            inputs = tree.xpath('//form[@name="F1"]//input')
            data = {
                input.get("name"): input.get("value").replace(" ", "")
                for input in inputs
            }
            if not data:
                raise DirectDownloadLinkException("ERROR: File Not Found!")
            data["referer"] = url
            direct_link = session.post(url, data=data).url
            return direct_link, header
        except:
            raise DirectDownloadLinkException("ERROR: File Not Found!")


def berkasdrive(url):
    """berkasdrive.com link generator
    by https://github.com/aenulrofik"""
    try:
        sesi = get(url).text
    except Exception as e:
        raise DirectDownloadLinkException(f"ERROR: {e.__class__.__name__}") from e
    html = HTML(sesi)
    if link := html.xpath("//script")[0].text.split('"')[1]:
        return b64decode(link).decode("utf-8")
    else:
        raise DirectDownloadLinkException("ERROR: File Not Found!")


def swisstransfer(link):
    matched_link = match(
        r"https://www\.swisstransfer\.com/d/([\w-]+)(?:\:\:(\w+))?", link
    )
    if not matched_link:
        raise DirectDownloadLinkException(
            f"ERROR: Invalid SwissTransfer link format {link}"
        )

    transfer_id, password = matched_link.groups()
    password = password or ""

    def encode_password(password):
        return b64encode(password.encode("utf-8")).decode("utf-8") if password else ""

    def getfile(transfer_id, password):
        url = f"https://www.swisstransfer.com/api/links/{transfer_id}"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Authorization": encode_password(password) if password else "",
            "Content-Type": "" if password else "application/json",
        }
        response = get(url, headers=headers)

        if response.status_code == 200:
            try:
                return response.json(), [f"{k}: {v}" for k, v in headers.items() if v]
            except ValueError:
                raise DirectDownloadLinkException(
                    f"ERROR: Error parsing JSON response {response.text}"
                )
        raise DirectDownloadLinkException(
            f"ERROR: Error fetching file details {response.status_code}, {response.text}"
        )

    def gettoken(password, containerUUID, fileUUID):
        url = "https://www.swisstransfer.com/api/generateDownloadToken"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json",
        }
        body = {
            "password": password,
            "containerUUID": containerUUID,
            "fileUUID": fileUUID,
        }

        response = post(url, headers=headers, json=body)

        if response.status_code == 200:
            return response.text.strip().replace('"', "")
        raise DirectDownloadLinkException(
            f"ERROR: Error generating download token {response.status_code}, {response.text}"
        )

    data, _ = getfile(transfer_id, password)
    if not data:
        return None

    try:
        container_uuid = data["data"]["containerUUID"]
        download_host = data["data"]["downloadHost"]
        files = data["data"]["container"]["files"]
        folder_name = data["data"]["container"]["message"] or "unknown"
    except (KeyError, IndexError, TypeError) as e:
        raise DirectDownloadLinkException(f"ERROR: Error parsing file details {e}")

    total_size = sum(file["fileSizeInBytes"] for file in files)

    if len(files) == 1:
        file = files[0]
        file_uuid = file["UUID"]
        token = gettoken(password, container_uuid, file_uuid)
        download_url = f"https://{download_host}/api/download/{transfer_id}/{file_uuid}?token={token}"
        return download_url, ["User-Agent:Mozilla/5.0"]

    contents = []
    for file in files:
        file_uuid = file["UUID"]
        file_name = file["fileName"]
        file_size = file["fileSizeInBytes"]

        token = gettoken(password, container_uuid, file_uuid)
        if not token:
            continue

        download_url = f"https://{download_host}/api/download/{transfer_id}/{file_uuid}?token={token}"
        contents.append({"filename": file_name, "path": "", "url": download_url})

    return {
        "contents": contents,
        "title": folder_name,
        "total_size": total_size,
        "header": "User-Agent:Mozilla/5.0",
    }

# ... y así sucesivamente para TODAS las funciones.

# ===============================================================
#  FUNCIÓN DESPACHADORA PRINCIPAL (COMPLETA)
# ===============================================================
def direct_link_generator(link):
    """direct links generator"""
    domain = urlparse(link).hostname
    if not domain:
        raise DirectDownloadLinkException("ERROR: Invalid URL")
    elif "yadi.sk" in link or "disk.yandex." in link:
        return yandex_disk(link)
    elif "buzzheavier.com" in domain:
        return buzzheavier(link)
    elif "devuploads" in domain:
        return devuploads(link)
    elif "lulacloud.com" in domain:
        return lulacloud(link)
    elif "uploadhaven" in domain:
        return uploadhaven(link)
    elif "fuckingfast.co" in domain:
        return fuckingfast_dl(link)
    elif "mediafile.cc" in domain:
        return mediafile(link)
    elif "mediafire.com" in domain:
        return mediafire(link)
    elif "fireload.com" in domain:
        return fireload(link)
    elif "osdn.net" in domain:
        return osdn(link)
    elif "github.com" in domain:
        return github(link)
    elif "hxfile.co" in domain:
        return hxfile(link)
    elif "1drv.ms" in domain:
        return onedrive(link)
    elif any(x in domain for x in ["pixeldrain.com", "pixeldra.in"]):
        return pixeldrain(link)
    elif "racaty" in domain:
        return racaty(link)
    elif "1fichier.com" in domain:
        return fichier(link)
    elif "solidfiles.com" in domain:
        return solidfiles(link)
    elif "krakenfiles.com" in domain:
        return krakenfiles(link)
    elif "upload.ee" in domain:
        return uploadee(link)
    elif "gofile.io" in domain:
        return gofile(link)
    elif "send.cm" in domain:
        return send_cm(link)
    elif "tmpsend.com" in domain:
        return tmpsend(link)
    elif "easyupload.io" in domain:
        return easyupload(link)
    elif "streamvid.net" in domain:
        return streamvid(link)
    elif "shrdsk.me" in domain:
        return shrdsk(link)
    elif "u.pcloud.link" in domain:
        return pcloud(link)
    elif "qiwi.gg" in domain:
        return qiwi(link)
    elif "mp4upload.com" in domain:
        return mp4upload(link)
    elif "berkasdrive.com" in domain:
        return berkasdrive(link)
    elif "swisstransfer.com" in domain:
        return swisstransfer(link)
    elif any(x in domain for x in ["akmfiles.com", "akmfls.xyz"]):
        return akmfiles(link)
    elif any(
        x in domain
        for x in [
            "dood.watch",
            "doodstream.com",
            "dood.to",
            "dood.so",
            "dood.cx",
            "dood.la",
            "dood.ws",
            "dood.sh",
            "doodstream.co",
            "dood.pm",
            "dood.wf",
            "dood.re",
            "dood.video",
            "dooood.com",
            "dood.yt",
            "doods.yt",
            "dood.stream",
            "doods.pro",
            "ds2play.com",
            "d0o0d.com",
            "ds2video.com",
            "do0od.com",
            "d000d.com",
        ]
    ):
        return doods(link)
    elif any(
        x in domain
        for x in [
            "streamtape.com",
            "streamtape.co",
            "streamtape.cc",
            "streamtape.to",
            "streamtape.net",
            "streamta.pe",
            "streamtape.xyz",
        ]
    ):
        return streamtape(link)
    elif any(x in domain for x in ["wetransfer.com", "we.tl"]):
        return wetransfer(link)
    elif any(
        x in domain
        for x in [
            "terabox.com",
            "nephobox.com",
            "4funbox.com",
            "mirrobox.com",
            "momerybox.com",
            "teraboxapp.com",
            "1024tera.com",
            "terabox.app",
            "gibibox.com",
            "goaibox.com",
            "terasharelink.com",
            "teraboxlink.com",
            "freeterabox.com",
            "1024terabox.com",
            "teraboxshare.com",
            "terafileshare.com",
            "terabox.club",
        ]
    ):
        return terabox(link)
    elif any(
        x in domain
        for x in [
            "filelions.co",
            "filelions.site",
            "filelions.live",
            "filelions.to",
            "mycloudz.cc",
            "cabecabean.lol",
            "filelions.online",
            "embedwish.com",
            "kitabmarkaz.xyz",
            "wishfast.top",
            "streamwish.to",
            "kissmovies.net",
        ]
    ):
        return filelions_and_streamwish(link)
    elif any(x in domain for x in ["streamhub.ink", "streamhub.to"]):
        return streamhub(link)
    elif any(
        x in domain
        for x in [
            "linkbox.to",
            "lbx.to",
            "teltobx.net",
            "telbx.net",
        ]
    ):
        return linkBox(link)
    elif is_share_link(link):
        if "gdtot" in domain:
            return gdtot(link)
        elif "filepress" in domain:
            return filepress(link)
        else:
            return sharer_scraper(link)
    elif any(
        x in domain
        for x in [
            "anonfiles.com",
            "zippyshare.com",
            "letsupload.io",
            "hotfile.io",
            "bayfiles.com",
            "megaupload.nz",
            "letsupload.cc",
            "filechan.org",
            "myfile.is",
            "vshare.is",
            "rapidshare.nu",
            "lolabits.se",
            "openload.cc",
            "share-online.is",
            "upvid.cc",
            "uptobox.com",
            "uptobox.fr",
        ]
    ):
        raise DirectDownloadLinkException(f"ERROR: R.I.P {domain}")
    else:
        raise DirectDownloadLinkException(f"No Direct link function found for {link}")
# ===============================================================
#  MANEJADOR DE VERCEL (VERSIÓN FINAL Y CORREGIDA)
# ===============================================================
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Manejar preflight OPTIONS primero
        if self.command == 'OPTIONS':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            return

        try:
            query_components = parse_qs(urlparse(self.path).query)
            url_to_process = query_components.get('url', [None])[0]

            if not url_to_process:
                self.send_json_response({"error": "Parámetro 'url' no encontrado."}, 400)
                return

            result = direct_link_generator(url_to_process)
            self.send_json_response(result, 200)

        except DirectDownloadLinkException as e:
            self.send_json_response({"error": str(e)}, 400)

        except Exception as e:
            error_payload = {
                "error": "Error Interno del Servidor",
                "details": f"Tipo: {type(e).__name__}, Mensaje: {str(e)}"
            }
            self.send_json_response(error_payload, 500)

    def send_json_response(self, data, status_code):
        """Método auxiliar para enviar respuestas JSON correctamente"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        json_data = json.dumps(data, default=str, ensure_ascii=False)
        self.wfile.write(json_data.encode('utf-8'))

    def do_OPTIONS(self):
        """Manejar solicitudes OPTIONS para CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()