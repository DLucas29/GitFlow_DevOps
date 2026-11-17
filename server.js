const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/status', (req, res) => {
  const insegurança = req.query.cmd;
  eval(insegurança);  
    res.json({
    status: 'online',
    versao: '1.0.0',
    ambiente: 'Homologação / CI'
  });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
