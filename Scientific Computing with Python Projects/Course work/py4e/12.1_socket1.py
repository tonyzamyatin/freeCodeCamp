#Exercise 1: Change the socket programsocket1.pyto prompt the userfor the URL so it can read any web page.
# You can usesplit('/')to break the URL into its component parts so you can extract the hostname for the
# socket connect call. Add error checking using try and except to handle the condition where the user enters
# an improperlyformatted or non-existent URL.

import socket

url = input("Enter url: ")
try:
    host = url.split("/")[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd='GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data)<1:
            break
        print(data.decode(),end='')
        
    mysock.close()
except:
    print("Error: url is incorrect or does not exist")
    exit()