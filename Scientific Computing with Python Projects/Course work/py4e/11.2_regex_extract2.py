#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the x from each of the lines using a regular expression
#and the findall() method. Compute the average of the xs and
#print out the average as an integer.

import re

fname = input("Enter the file name: ")

try:
    fhand = open(fname, 'r')
except:
    print("The file could not be opened: ", fname )
    quit()

numlist = list()
for line in fhand:
    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9]+)', line)
    if len(num) > 0:
        for x in num:
            x = float(x)
        numlist.append(x)

avg = int(sum(numlist)/len(numlist))

print(avg)

