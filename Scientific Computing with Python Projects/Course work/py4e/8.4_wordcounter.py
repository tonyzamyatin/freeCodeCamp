try:
    inp = input("Enter file: ")
    fhand=open(inp)
except:
    print("File cannot be opened")
    exit()
uniquewords = []
for line in fhand:
    words=line.split()
    for word in words:
        word=word.lower()
        if word not in uniquewords:
            uniquewords.append(word)
print(uniquewords)


