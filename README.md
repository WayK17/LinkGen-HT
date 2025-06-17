# 🔥 API para Extraer Enlaces Directos de MediaFire

![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)
![Versión](https://img.shields.io/badge/Versi%C3%B3n-2.0.0-blue.svg)

Una API ligera y eficiente para extraer enlaces de descarga directa de MediaFire, obteniendo también el nombre y el peso del archivo. Ideal para desplegar fácilmente en Vercel.

---

## 🚀 Características Principales

* ✅ Obtiene el enlace de descarga directa de cualquier archivo de MediaFire.
* ✅ Extrae el nombre y el peso del archivo.
* ✅ Habilitado para CORS, permitiendo peticiones desde cualquier origen.
* ✅ Implementa un sistema de caché para respuestas más rápidas.
* ✅ Diseñado para ser desplegado sin esfuerzo en plataformas como Vercel.

---

## ⚙️ Uso de la API

Para utilizar la API, simplemente realiza una petición GET a la ruta `/api/mediafire`, pasando la URL del archivo de MediaFire como parámetro.

**Ejemplo usando `cURL`:**

```bash
curl "[https://tu-app.vercel.app/api/mediafire?url=](https://tu-app.vercel.app/api/mediafire?url=)<URL_DEL_ARCHIVO_MEDIAFIRE>"

Ejemplo de respuesta exitosa (JSON):
{
  "directLink": "[https://download2390.mediafire.com/](https://download2390.mediafire.com/)...",
  "fileName": "mi_archivo_genial.zip",
  "fileSize": "123.45 MB",
  "mediafireURL": "[https://www.mediafire.com/file/](https://www.mediafire.com/file/)...",
  "credit": "Developer: @WayK17"
}

💬 Comunidad
¿Tienes dudas, sugerencias o quieres estar al tanto de las actualizaciones?
➡️ Únete a nuestro canal de Telegram: Ness Cloud
👨‍💻 Créditos
 * Desarrollador original de la API: [@labani]
<!-- end list -->

