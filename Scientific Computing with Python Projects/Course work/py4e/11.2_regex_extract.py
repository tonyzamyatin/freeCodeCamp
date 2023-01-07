import re
numbers = []
fname = input("Enter a file: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()
for line in fhand:
    line = line.rstrip()
    x = re.findall("^New Revision: ([0-9]+)",line)
    if len(x) != 0:
        num = int(x[0])
        numbers.append(num)

average = int(sum(numbers) / len(numbers))
print(average)
