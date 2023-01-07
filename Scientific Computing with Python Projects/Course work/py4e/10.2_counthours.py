emails=dict()
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
        time=words[5]
        index=time.find(":")
        hrs = time[index-2:index]
        if hrs not in emails:
            emails[hrs]=1
        else:
            emails[hrs] +=1
    except:
        continue
lst=list()
for key, val in list(emails.items()):
    lst.append((key, val))
lst.sort()

for key, val in lst:
    print(key, val)