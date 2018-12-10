var express = require("express");
var app = express();

var getIp = require('ipware')().get_ip;
var ip;


app.get('/',function(req,res){
	ip = getIp(req)
	console.log(ip);
	url = ""
	app.get("http://ip-api.com/json/"+ip+"?fields=country,countryCode,region,regionName,city,zip,lat,lon,timezone",function(data){
		console.log("1->",data);
		res.send(data);


	});
	
	// console.log(req.headers['x-forwarded-for']);
	console.log(req.socket.remoteAddress);
	// res.send(req.headers['x-forwarded-for']);
});



app.listen(3000,function(){
	console.log("Listening");
});