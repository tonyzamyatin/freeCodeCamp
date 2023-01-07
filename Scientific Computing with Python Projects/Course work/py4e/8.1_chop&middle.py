# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(t):
    lenght = len(t)
    del t[lenght-1]
    del t[0]
    print(t)

def middle(t):
    lenght = len(t)
    middle_list = t[1 : lenght-1]
    print(middle_list)

new_list = list()

while True:
    new_element = input("Enter whatever (enter 'done' when done): ")
    if new_element == 'done':
        break
    new_list.append(new_element)

chop(new_list)
#middle(new_list)