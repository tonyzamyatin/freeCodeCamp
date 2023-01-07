#Exercise 5: This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the contents of your dictionary.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()
domains = list()
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split(' ')
    if  len(words) < 3 or words[0] != 'From':
        continue
    email = words[1].split('@')
    domains.append(email[1])

for domain in domains:
        counts[domain] = counts.get(domain, 0 ) + 1

print(counts)
