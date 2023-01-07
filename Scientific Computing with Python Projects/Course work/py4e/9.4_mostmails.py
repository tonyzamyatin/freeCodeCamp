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
        if email not in emails:
            emails[email]=1
        else:
            emails[email] +=1
    except:
        continue
largest=0
for key in emails:
    if emails[key] > largest:
        largest=emails[key]
        largestmail = key
print(largestmail, largest)