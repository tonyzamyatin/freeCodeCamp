import re
exp=[]
regex=input("Enter a regular expression: ")
fhand=open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    try:
        x=re.findall(regex,line)
    except:
        print("Error: regular expression is incorrect")
        exit()
    exp.append(x)
count=len(exp)
print("mbox.txt had ", count, "lines that matched ", regex)

