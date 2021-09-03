import socket, platform, os

SRV_ADDR = ''
SRV_PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s.accept()

while 1:
    try:
        data = connection.recv(1024)
    except:
        print('exception')
        continue

    if(data.decode('utf-8') == '1'):
        tosend = platform.platform() + ' ' + platform.machine()
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '2'):
        print('here line 22')
        data = connection.recv(1024)
        print('here line 23')
        try:
            filelist = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in filelist:
                tosend += "," + x
            print(tosend)
        except:
            tosend = 'Wrong path'
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '0'):
        connection.close()
        connection, address = s.accept()
