var express = require("express");
var app = express();
var port = process.env.PORT || 8000;
var request = require('request');
var getIp = require('ipware')().get_ip;
var ip;


app.get('/',function(req,resq){
	ip = getIp(req)
	console.log(ip);
	url = "http://api.ipstack.com/"+ip+"?access_key=9f28833f9b6e61f7d93deed7ff9941eb&fields=main";
	request.get(url,function(err,res,body){
		console.log("1->",res);
		resq.send(body);
	});
});



app.listen(port,function(){
	console.log("Listening to port + ",process.env.port);
});