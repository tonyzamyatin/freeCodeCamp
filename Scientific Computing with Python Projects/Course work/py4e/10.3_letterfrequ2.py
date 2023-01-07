#Exercise 3: Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies.

from typing import Counter


alphabet = 'abcdefghijklmnopqrstuvwxyz'

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("The file could not be opened: ", fname )
    quit()

text = fhand.read()

frequ_dct = dict()

for char in text.lower():
    if char in alphabet:
        frequ_dct[char] = frequ_dct.get(char, 0 ) + 1
    
frequ_lst = sorted(((v, k) for (k, v) in  frequ_dct.items()),reverse=True)

for v, k in frequ_lst:
    print(k, v)