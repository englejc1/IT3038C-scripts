import socket, sys

def getHostnameByIP(h):
    try:
        hostname = str(h) 
        ip = socket.gethostbyname(hostname) 
        print (hostname +' has an IP of ' + ip)
    except:
        print("oops, there was a problem with that host. No response.")

getHostnameByIP(sys.argv[1])

