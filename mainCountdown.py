import string
import random

"""with open('wordlist.txt','r') as f:"""

print ("Are you ready to play?")

def factorial(n):
    return n * factorial(n-1)

def id_generator(size=9, chars=string.ascii_uppercase):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(size))

s = id_generator()    

"""print (s)"""

while factorial(9):
    if s not in list:
        continue
    else:
        s = (random.sample(word, len(word)))
        list = []
        list.append(s)

print (list)

with open('wordlist.txt','r') as f:
    for line in f:
        for word in line.split():
            if word not in s:
                continue
            else: 
                print(word)