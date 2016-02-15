import string
import random

"""with open('wordlist.txt','r') as f:"""

print ("Are you ready to play?")

def id_generator(size=9, chars=string.ascii_uppercase):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(size))


s = id_generator()    
"""jumbleSort = ''.join(sorted(s))"""
jumbleSort = ''.join(sorted("abalienation"))

print (s)
print (jumbleSort)


def compare(ch, text): 
    numAppears = 0
    for t in text:
        if t == ch:
            numAppears += 1
    return numAppears

with open('wordlist.txt','r') as f:
    for line in f:
        for word in line.split():
            dic = ''.join(sorted(word))
            matches = compare(dic, jumbleSort);
            if matches > 3:
                print (word)
            else:
            	continue
