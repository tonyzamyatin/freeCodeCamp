#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dictionary has been created, 
#look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()
emails = list()
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split(' ')
    if  len(words) < 3 or words[0] != 'From':
        continue
    emails.append(words[1])

for email in emails:
        counts[email] = counts.get(email, 0 ) + 1

maxmcount = 0

for mailadr in counts:
    if maxmcount < counts[mailadr]:
        maxmcount = counts[mailadr]
        maxmailadr = mailadr

print(maxmailadr, maxmcount)