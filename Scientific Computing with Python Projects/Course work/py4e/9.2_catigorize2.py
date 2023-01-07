#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).
fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()
days = list()
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split(' ')
    if  len(words) < 3 or words[0] != 'From':
        continue
    days.append(words[2])

for day in days:
        counts[day] = counts.get(day, 0 ) + 1

print(counts)