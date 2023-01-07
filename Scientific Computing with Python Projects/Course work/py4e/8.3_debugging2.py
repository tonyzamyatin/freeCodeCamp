# Exercise 3: Rewrite the guardian code in the above example without
# two if statements. Instead, use a compound logical expression using
# the or logical operator with a single if statement.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()

count = 0

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if  len(words) < 3 or words[0] != 'From' : continue
    print(words[2])
