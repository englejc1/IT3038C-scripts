var fs = require("fs");
var http = require("http");
var ip = require('ip');
var os = require("os");

// function that gets the system uptime in seconds and converts it to days, hours, minutes, and seconds.
function getUptime() {
    serverTime = os.uptime();
    var d = Math.floor(serverTime / (3600*24));
    var h = Math.floor(serverTime % (3600*24) / 3600);
    var m = Math.floor(serverTime % 3600 / 60);
    var s = Math.floor(serverTime % 60);
    var dreturn = d > 0 ? d + (d == 1 ? " day, " : " days, ") : "";
    var hreturn = h > 0 ? h + (h == 1 ? " hour, " : " hours, ") : "";
    var mreturn = m > 0 ? m + (m == 1 ? " minute, " : " minutes, ") : "";
    var sreturn = s > 0 ? s + (s == 1 ? " second, " : " seconds, ") : "";
    return dreturn + hreturn + mreturn + sreturn;
}
// if/else statement for website navigation
var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });            
    }
    else if(req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        totalMemory = os.totalmem();
        freeMemory = os.freemem();
        myCPUs = os.cpus().length;
        html = `
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Node JS Response</title>
                </head>
                    <body>
                        <p>Hostname: ${myHostName}</P>
                        <p>IP: ${ip.address()}</p>
                        <p>Server Uptime: ${getUptime()}</p>
                        <p>Total Memory: ${totalMemory / 1000000} MB</p>
                        <p>Free Memory: ${(freeMemory / 1000000)} MB</p>
                        <p>Number of CPUs: ${myCPUs}</p>
                    </body>
            </html>
        `
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 file not found at ${req.url}`);
    }
}).listen(3000)

console.log("Server listening on port 3000");