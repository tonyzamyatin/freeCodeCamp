import string

letters=dict()
alph = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
fname=input("Enter a file: ")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit()
for line in fhand:
    if not line.startswith("From "): continue
    line=line.rstrip()
    line=line.translate(line.maketrans('','', string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        word=list(word)
        for letter in word:
            if letter in alph:
                if letter not in letters:
                    letters[letter]=1
                else:
                    letters[letter] +=1
            else:
                continue
print(letters)
lst=list()
for key, val in list(letters.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst:
    print(val, key)