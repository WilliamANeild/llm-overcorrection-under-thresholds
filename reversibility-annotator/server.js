const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3847;
const DATA_DIR = path.join(__dirname, '..', 'data', 'study3', 'raw_responses');
const PAIRS_FILE = path.join(DATA_DIR, 'reversibility_pairs_stripped.json');

const server = http.createServer((req, res) => {
  // No-cache headers for all responses
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
  res.setHeader('Pragma', 'no-cache');
  res.setHeader('Expires', '0');

  if (req.method === 'GET' && req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8'));
    return;
  }

  if (req.method === 'GET' && req.url === '/pairs') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(fs.readFileSync(PAIRS_FILE, 'utf8'));
    return;
  }

  if (req.method === 'GET' && req.url.startsWith('/load/')) {
    const rater = req.url.split('/load/')[1];
    if (rater !== 'liam' && rater !== 'troy') {
      res.writeHead(400); res.end('Invalid rater'); return;
    }
    const file = path.join(DATA_DIR, `reversibility_judgments_${rater}.json`);
    if (fs.existsSync(file)) {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(fs.readFileSync(file, 'utf8'));
    } else {
      res.writeHead(404); res.end('Not found');
    }
    return;
  }

  if (req.method === 'POST' && req.url.startsWith('/save/')) {
    const rater = req.url.split('/save/')[1];
    if (rater !== 'liam' && rater !== 'troy') {
      res.writeHead(400); res.end('Invalid rater'); return;
    }
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      const file = path.join(DATA_DIR, `reversibility_judgments_${rater}.json`);
      fs.writeFileSync(file, body, 'utf8');
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ ok: true, path: file }));
    });
    return;
  }

  res.writeHead(404); res.end('Not found');
});

server.listen(PORT, () => {
  console.log(`Reversibility annotator running at http://localhost:${PORT}`);
});
