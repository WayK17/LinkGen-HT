const express = require("express");

const axios = require("axios");

const cheerio = require("cheerio");

const cors = require("cors");

const app = express();

const port = 3000;

// Enable CORS for all requests
app.use(cors());

// API endpoint:
// GET /api?url=<mediafire_file_url>
app.get('/api', async (req, res) => {
  const mediafireURL = req.query.url;

  if (!mediafireURL) {
    return res.status(400).json({error:'URL is required'})
  }

  if (!mediafireURL.startsWith("https://www.mediafire.com/file/")) {
    return res.status(400).json({error:'Invalid MediaFire link'})
  }

  try {
    // Retrieve MediaFire page HTML
    const response = await axios.get(mediafireURL, {
      headers: {
        'User-Agent': 'Mozilla/5.0'
      }
    });
    const $ = cheerio.load(response.data);

    // Extract direct link
    const directLink =$('#downloadButton').attr('href') ||
      $('.download-button').attr('href'); // fallback if needed

    // Extract file name and size
    const fileName = $('.dl-info .filename').text().trim();
    const fileSize = $('.dl-info .file-size').text().trim();

    if (directLink) {
      res.json({directLink, fileName, fileSize, mediafireURL, credit:'Developer: @labani'})
    } else {
      res.status(404).json({error:'Download link not found'})
    }
  } catch (error) {
    res.status(500).json({error:'Server Error!', details:error.toString()})
  }
});

// Handle invalid routes gracefully
app.use((req, res) => {
  res.status(404).json({error:'Not found'})
});

// Start server
app.listen(port, () => {
  console.log(`MediaFire API listening at http://localhost:${port}`);
});

// Export for Vercel
module.exports = app;
