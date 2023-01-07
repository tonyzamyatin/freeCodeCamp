fname=input("Enter the file name: ")
if fname=="na na boo boo":
    print("NA NA BOO BOO TO YOU - You have  been punk'd!")
    exit()
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
sum=0
count=0
for line in fhand:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=int(line.find(":"))
    spamc=float(line[pos+1:])
    sum=sum+spamc
    count=count+1
if count != 0:
    avg_spam=sum/count
else:
    avg_spam=0
print("Average spam confidence: ", avg_spam)
