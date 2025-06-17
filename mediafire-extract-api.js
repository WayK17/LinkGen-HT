const axios = require("axios");
const cheerio = require("cheerio");

// Caché simple en memoria (limitado en serverless, pero útil para la misma ejecución)
const cache = new Map();

/**
 * Extrae la información de una URL de MediaFire.
 * @param {string} mediafireURL La URL del archivo de MediaFire.
 * @returns {Promise<object>} Un objeto con directLink, fileName y fileSize.
 * @throws {Error} Si la extracción falla o la URL no es válida.
 */
async function extractMediafireData(mediafireURL) {
    try {
        // Timeout en la solicitud para mayor robustez (10 segundos)
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
        // Manejo de errores de Axios más específico
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

// Función principal para Vercel
module.exports = async (req, res) => {
    // Configurar CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    // Manejar preflight requests
    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    // Solo permitir GET requests
    if (req.method !== 'GET') {
        return res.status(405).json({ error: 'Método no permitido' });
    }

    const mediafireURL = req.query.url;

    if (!mediafireURL) {
        return res.status(400).json({ error: 'El parámetro URL es requerido' });
    }
    
    if (!mediafireURL.startsWith("https://www.mediafire.com/file/")) {
        return res.status(400).json({ error: 'Enlace de MediaFire inválido' });
    }

    // Verificar si el resultado ya está en el caché
    if (cache.has(mediafireURL)) {
        console.log(`[Cache] HIT para: ${mediafireURL}`);
        return res.json(cache.get(mediafireURL));
    }

    console.log(`[Cache] MISS para: ${mediafireURL}`);

    try {
        const data = await extractMediafireData(mediafireURL);

        const responsePayload = {
            ...data,
            mediafireURL,
            credit: 'Developer: @labani'
        };

        // Guardar el resultado en el caché antes de enviarlo
        cache.set(mediafireURL, responsePayload);

        res.json(responsePayload);

    } catch (error) {
        // Devuelve el error específico capturado en la función de extracción
        res.status(500).json({ error: 'Error del servidor.', details: error.toString() });
    }
};