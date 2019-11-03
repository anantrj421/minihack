var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.set('view engine','ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:true}));
app.get('/',function(req,res){
  res.render('home');
});
app.get('/dlogin',function(req,res){
  //Send Doctor Login
  res.render('doclogin');
});
app.get('/plogin',function(req,res){
  res.render('patlogin');
});
app.get('/doctor',function(req,res){
  res.render('doctor');
});
app.get('/patient',function(req,res){
  res.render('patient');
});
app.post('/dlog',function(req,res){
    res.redirect('/doctor');
});
app.post('/plog',function(req,res){
    res.redirect('/patient')
});
app.get('/medi',function(req,res){
    res.render('meddos');
});
app.get('/medshop',function(req,res){
    res.render('medstore');
});
app.listen(3000, function(){
    console.log("started");
});
