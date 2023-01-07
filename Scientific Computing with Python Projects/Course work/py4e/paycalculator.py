def computepay(x,y):
    pay_overtime = (40 * y) + (x - 40) * (y * 1.5)
    return pay_overtime
try:
    hours = input("Enter Hours: ")
    nhours = int(hours)
except:
    print("Error: Please enter a numeric input")
    exit(1)
try:
    rate = input("Enter Rate: ")
    nrate = int(rate)
except:
    print("Error: Please enter a numeric input")
    exit(1)
if nhours > 40:
    pay=computepay(nhours,nrate)
else :
    pay = nhours*nrate
print("Pay:", pay)
