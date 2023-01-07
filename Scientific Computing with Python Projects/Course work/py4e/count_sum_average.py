print('Enter numbers. Once done enter "done" and count, sum and average of those numbers will be printed')
count = 0
sum = 0
while True:
    userinp = input("Enter a number: ")
    if userinp == "done":
        avg = sum/count
        print("Count: ", count)
        print("Sum: ", sum)
        print("Average: ", avg)
        break
    try:
        number = int(userinp)
    except:
        print("Error: Invalid input. Please enter a number.")
        exit()
    count = count + 1
    sum = sum + number
