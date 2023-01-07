# Exercise 3: Use urllib to replicate the previous exercise of (1) retrievingthe document
# from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number
# of characters in the document. Don’t worry about the headers for this exercise, simply
# show the first 3000 characters of the document contents.

# Search for link values within URL input

import urllib.request

url = input("Enter url: ")
content=urllib.request.urlopen(url).read()
content=content.decode()
print(content[:3000])
print(len(content))
