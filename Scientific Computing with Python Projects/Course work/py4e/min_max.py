numbers = []
while True:
    userinp=input("Enter a number: ")
    if userinp == "done":
        print("Smallest: ", min(numbers), " ,Largest: ", max(numbers))
        break
    try:
        number=int(userinp)
    except:
        print("Invalid input")
    numbers.append(number)
    