
days=dict()
fname=input("Enter a file: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit()
for line in fhand:
    if not line.startswith("From "): continue
    words=line.split()
    try:
        day=words[2]
        if day not in days:
            days[day]=1
        else:
            days[day] +=1
    except:
        continue
print(days)