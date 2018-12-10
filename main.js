var express = require("express");
var app = express();
var request = require("request");
var getIp = require('ipware')().get_ip;
var ip;


app.get('/',function(req,resq){
	ip = getIp(req)
	console.log(ip);
	url = ""
	request.get("http://ip-api.com/json/"+ip+"?fields=country,countryCode,region,regionName,city,zip,lat,lon,timezone",function(err,res,body){
		console.log("1->",body);
		resq.send(body);


	});
	
	// console.log(req.headers['x-forwarded-for']);
	console.log(req.socket.remoteAddress);
	// res.send(req.headers['x-forwarded-for']);
});



app.listen(3000,function(){
	console.log("Listening");
});