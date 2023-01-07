#Exercise 3: Write a program to read through a mail log, build a histogram
#using a dictionary to count how many messages have come from
#each email address, and print the dictionary.

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
    if email not in counts:
        counts[email] = counts.get(email, 0 ) + 1

print(counts)