# Exercise 5: (Advanced) Change the socket program so that it onlyshowsdata after the 
# headers and a blank line have been received. Remember that recv receives characters 
# (newlines and all), not lines.

import socket

url = input("Enter url: ")

try:
    host = url.split("/")[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd='GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    received = b""

    while True:
        data = mysock.recv(512)
        if len(data)<1:
            break
        received += data
    received = received.decode()
    index = received.find('\r\n\r\n')
    print(received[ :int(index)])
    print(len(received))
            
    mysock.close()
except:
    print("Error: url is incorrect or does not exist")
    exit()