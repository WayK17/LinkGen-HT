const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const cors = require("cors");
const rateLimit = require('express-rate-limit');
const NodeCache = require('node-cache');
require('dotenv').config(); // Carga las variables de entorno del archivo .env

const app = express();
const port = 3000;

// --- MEJORAS IMPLEMENTADAS ---

// 1. Caché en memoria para mejorar el rendimiento (TTL de 1 hora)
// Guarda los resultados de una URL para no tener que procesarla de nuevo.
const myCache = new NodeCache({ stdTTL: 3600 });

// 2. Límite de tasa para prevenir abusos (15 peticiones por minuto por IP)
const limiter = rateLimit({
	windowMs: 1 * 60 * 1000, // 1 minuto
	max: 15,
	standardHeaders: true,
	legacyHeaders: false,
    message: { error: 'Demasiadas solicitudes, por favor intente de nuevo más tarde.' }
});

// --- LÓGICA DE SCRAPING MODULARIZADA ---

/**
 * Extrae la información de una URL de MediaFire.
 * @param {string} mediafireURL La URL del archivo de MediaFire.
 * @returns {Promise<object>} Un objeto con directLink, fileName y fileSize.
 * @throws {Error} Si la extracción falla o la URL no es válida.
 */
async function extractMediafireData(mediafireURL) {
    try {
        // 3. Timeout en la solicitud para mayor robustez (10 segundos)
        const response = await axios.get(mediafireURL, {
            headers: { 'User-Agent': 'Mozilla/5.0' },
            timeout: 10000 
        });

        const $ = cheerio.load(response.data);

        const directLink = $('#downloadButton').attr('href') || $('.download-button').attr('href');
        const fileName = $('.dl-info .filename').text().trim();
        const fileSize = $('.dl-info .file-size').text().trim();

        if (directLink && fileName) {
            return { directLink, fileName, fileSize };
        } else {
            // Si no se encuentran los elementos, es un error de scraping.
            throw new Error('No se pudo encontrar el enlace de descarga o la información del archivo.');
        }
    } catch (error) {
        // 4. Manejo de errores de Axios más específico
        if (axios.isAxiosError(error)) {
            if (error.response) {
                // El servidor de MediaFire respondió con un código de error (404, 500, etc.)
                throw new Error(`MediaFire respondió con el estado: ${error.response.status}`);
            } else if (error.code === 'ECONNABORTED') {
                // La solicitud excedió el timeout
                throw new Error('La solicitud a MediaFire tardó demasiado en responder (timeout).');
            }
        }
        // Propaga el error original o uno nuevo
        throw new Error(error.message || 'Error al procesar la solicitud a MediaFire.');
    }
}


// --- CONFIGURACIÓN DE LA APP EXPRESS ---

// Habilita CORS para todas las solicitudes
app.use(cors());

// --- ENDPOINT DE LA API MEJORADO ---

/**
 * @api {get} /api Obtiene el enlace de descarga directa de MediaFire
 * @apiName GetMediafireLink
 * @apiGroup Mediafire
 *
 * @apiParam {String} url La URL del archivo de MediaFire a procesar.
 *
 * @apiSuccess {String} directLink El enlace de descarga directa.
 * @apiSuccess {String} fileName El nombre del archivo.
 * @apiSuccess {String} fileSize El tamaño del archivo.
 * @apiSuccess {String} mediafireURL La URL original solicitada.
 * @apiSuccess {String} credit El crédito del desarrollador.
 */
app.get('/api', limiter, async (req, res) => {
  const mediafireURL = req.query.url;

  if (!mediafireURL) {
    return res.status(400).json({ error: 'El parámetro URL es requerido' });
  }
  if (!mediafireURL.startsWith("https://www.mediafire.com/file/")) {
    return res.status(400).json({ error: 'Enlace de MediaFire inválido' });
  }

  // Verificar si el resultado ya está en el caché
  if (myCache.has(mediafireURL)) {
    console.log(`[Cache] HIT para: ${mediafireURL}`);
    return res.json(myCache.get(mediafireURL));
  }
  
  console.log(`[Cache] MISS para: ${mediafireURL}`);

  try {
    const data = await extractMediafireData(mediafireURL);
    
    const responsePayload = {
        ...data,
        mediafireURL,
        // 5. Usar variable de entorno para el crédito
        credit: process.env.DEVELOPER_CREDIT || 'Developer: @labani'
    };
    
    // Guardar el resultado en el caché antes de enviarlo
    myCache.set(mediafireURL, responsePayload);

    res.json(responsePayload);

  } catch (error) {
    // Devuelve el error específico capturado en la función de extracción
    res.status(500).json({ error: 'Error del servidor.', details: error.toString() });
  }
});

// Manejar rutas no encontradas
app.use((req, res) => {
  res.status(404).json({ error: 'Ruta no encontrada' });
});

// Iniciar servidor
app.listen(port, () => {
  console.log(`MediaFire API (Mejorada) escuchando en http://localhost:${port}`);
});

// Exportar para Vercel
module.exports = app;
