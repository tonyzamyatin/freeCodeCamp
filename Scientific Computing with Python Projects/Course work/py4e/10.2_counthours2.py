#Exercise 2: This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()
hours = list()
counts = dict()

for line in fhand:
    line.rstrip()
    words = line.split()
    if  len(words) != 7 or words[0] != 'From':
        continue
    time = words[5].split(':')
    hours.append(time[0])

for hour in hours:
        counts[hour] = counts.get(hour, 0 ) + 1

lst = list()
for k, v in list(counts.items()):
    lst.append((k, v))
lst.sort()
for k, v in lst:
    print(k, v)