words=dict()
fname=input("Enter a file: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit()
for line in fhand:
    line = line.split()
    for word in line:
        if word not in words:
            words[word]=""
print(words)
