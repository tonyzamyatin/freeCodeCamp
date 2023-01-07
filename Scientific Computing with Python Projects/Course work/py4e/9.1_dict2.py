#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary
import string
fhand = open('words.txt')

words = dict()

for line in fhand:
    line = line.rstrip()
    #the following code would make the programm no longer case and punctuation sensetive.
    #line.translate(line.maketrans('','',string.punctuation))
    #line = line.lower()
    wordlist = line.split()
    for word in wordlist:
        if word not in words:
            words[word] = ''

print(words)