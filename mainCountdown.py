import string
import random

"""with open('wordlist.txt','r') as f:"""

print ("Are you ready to play?")

def id_generator(size=9, chars=string.ascii_uppercase):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(size))

s = id_generator()    

print (s)


f = open('wordlist.txt', 'r')
for line in f:
    s =  ''.join(random.sample(s, len(s)))
    for word in line.split():
        if word not in s:
            continue
        else: 
            print(word)