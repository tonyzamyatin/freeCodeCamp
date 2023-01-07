def chop(t):
    del t[0]
    del t[-1]

rdmlist=[1,2,3,4,5,6,7,8,9]
chop(rdmlist)
print(rdmlist)