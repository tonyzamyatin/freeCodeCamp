fname=input("Enter a file: ")
fhand=open(fname)
count=0
for line in fhand:
    if not line.startswith("From "): continue
    words=line.split()
    try:
        print(words[1])
        count=count+1
    except:
        continue
print("There were ", count, "lines in the file with From as the first word")

