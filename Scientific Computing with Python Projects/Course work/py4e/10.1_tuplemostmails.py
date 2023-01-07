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
        email=words[1]
        index=email.find("@")
        domain = email[index: ]
        if domain not in emails:
            emails[domain]=1
        else:
            emails[domain] +=1
    except:
        continue
lst=list()
for key, val in list(emails.items()):
    lst.append((val, key))
lst.sort(reverse=True)

for key, val in lst [:1]:
    print(val, key)