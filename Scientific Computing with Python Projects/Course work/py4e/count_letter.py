word = input("Enter text: ")
x = input("Enter letter to count for: ")
def count(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count =count + 1
    print(count)

fruit="Pinapple"
ps = fruit.count("p")
print(ps)
