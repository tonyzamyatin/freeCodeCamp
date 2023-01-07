# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request, urllib.parse, urllib.error

url = input("Enter a url: ")
doc = ''

try:
    fhand = urllib.request.urlopen(url)
except:
    
    print('Error: url is incorrect or does not exist.')
    exit()

for line in fhand:
    doc += line.decode()

print(doc[:3001],'\nCharacter count: ', len(doc))

