# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

import socket

url = input("Enter a url: ")
try:
    host = url.split('/')[2]
    # print(host)
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
except:
    print('Error: url is incorrect or does not exist.')
    exit()

received = b''
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    received += data

doc = received.decode()
pos = doc.find('\r\n\r\n')

print(doc[pos+2:])