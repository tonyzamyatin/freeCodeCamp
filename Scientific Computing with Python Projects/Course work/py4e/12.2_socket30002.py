#Exercise 2: Change your socket program so that it counts the number
#of characters it has received and stops displaying any text after it has
#shown 3000 characters. The program should retrieve the entire document 
#and count the total number of characters and display the count
#of the number of characters at the end of the document.

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

doc = ''
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    for char in data.decode():
        count = count + 1
        doc = doc + str(char)
        if not count > 3000:
            print(char, end='')
print('\nCharacter count:', count)

mysock.close()

    