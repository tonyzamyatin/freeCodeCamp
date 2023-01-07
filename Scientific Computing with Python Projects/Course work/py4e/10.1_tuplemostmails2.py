#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the 
#number of messages from each person using a dictionary

#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.

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

lst = sorted(((v ,k) for (k, v) in counts.items()), reverse=True)

# lst = list()
# for k, v in list(counts.items()):
#     lst.append((v, k))
# lst.sort(reverse=True)
for v, k in lst[:1]:
    print(k, v)