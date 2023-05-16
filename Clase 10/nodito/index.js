// Para usar el proyecto es necesario Node
// Para utilizarlo npm install
const express = require('express');
const nunjucks = require('nunjucks');
const app = express();
app.use(express.static('public'));
nunjucks.configure('views', { autoescape: true, express: app });

app.get('/', function(req, res) {
    res.render('index.html',{titulo:"Home",th1 : "El gran título del mundo"});
});

app.get('/hola', function(req, res) {
    res.send("Hola Mundo Cruel")
});


app.listen(8080)