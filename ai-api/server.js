const express = require('express');
const fs = require('fs');
const cors = require('cors');
const app = express();
const PORT = 3001;

// CORS middleware
app.use(cors());

// JSON dosyasını oku ve döndür
app.get('/results', (req, res) => {
  fs.readFile('../results.json', 'utf8', (err, data) => {
    if (err) {
      return res.status(500).json({ error: 'Sonuç dosyası okunamadı.' });
    }
    const parsed = JSON.parse(data);
    res.json(parsed);
  });
});

app.listen(PORT, () => {
  console.log(`API http://localhost:${PORT} adresinde çalışıyor.`);
});
