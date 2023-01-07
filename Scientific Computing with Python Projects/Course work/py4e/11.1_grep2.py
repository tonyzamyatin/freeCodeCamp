#Exercise 1: Write a simple program to simulate the operation of the
#grep command on Unix. Ask the user to enter a regular expression and
#count the number of lines that matched the regular expression:

import re

regex = input('Enter a regular expression: ')
fhand = open('mbox.txt', 'r')

count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

print('mbox.txt had ', count, ' lines that matched ', regex)
