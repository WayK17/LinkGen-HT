# 🚀 LinkGen - Generador de Enlaces Directos para MediaFire

![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)
![Versión](https://img.shields.io/badge/Versi%C3%B3n-2.0.0-blue.svg)

Una herramienta web moderna y eficiente que convierte enlaces de MediaFire en enlaces de descarga directa. Cuenta con una interfaz limpia y una API potente para obtener archivos de forma rápida y sin anuncios.

---

## ✨ Características

* **Interfaz Moderna:** Diseño web intuitivo y responsive para una experiencia de usuario fluida en cualquier dispositivo.
* **Generación Instantánea:** Obtiene enlaces de descarga directa de archivos de MediaFire al instante.
* **Información del Archivo:** Extrae automáticamente el nombre y el peso del archivo.
* **API Robusta:** La API backend está habilitada para CORS, implementa caché y es fácilmente desplegable en Vercel.
* **Comunidad Activa:** Soporte y actualizaciones a través del canal de Telegram.

---

## ⚙️ Uso de la API

La API es el motor de la aplicación. Para usarla de forma independiente, realiza una petición GET a la ruta `/api/mediafire` con la URL del archivo.

**Ejemplo con `cURL`:**

```bash
curl "[https://tu-app.vercel.app/api/mediafire?url=](https://tu-app.vercel.app/api/mediafire?url=)<URL_DEL_ARCHIVO_MEDIAFIRE>"

Ejemplo de respuesta JSON:
{
  "directLink": "[https://download2390.mediafire.com/](https://download2390.mediafire.com/)...",
  "fileName": "tu_archivo.zip",
  "fileSize": "123.45 MB",
  "mediafireURL": "[https://www.mediafire.com/file/](https://www.mediafire.com/file/)...",
  "credit": "Developer: @labani"
}

💬 Comunidad y Soporte
¿Tienes dudas, sugerencias o quieres estar al tanto de las actualizaciones?
➡️ Únete al canal oficial en Telegram: Ness Cloud
👨‍💻 Desarrollo
 * Desarrollo y mejoras: Ness Cloud
 * API Base por: [@labani]
<!-- end list -->

