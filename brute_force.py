import http.client
import urllib.parse

host = input("Insert the host/IP: ")
port = input("Insert the port(default:80): ")
url = input("Insert the url: ")

values = {"username": "admin", "password": "password"}

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', url)
    response = connection.getresponse()
    print('Server response: ', response.status)

    mod_url = url + "/?username=" + values["username"] + "&password=" + values["password"]
    print(mod_url)
    #connection.request('POST', mod_url)

    connection.close()
except ConnectionRefusedError:
    print('Connection failed')