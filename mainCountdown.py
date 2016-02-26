from random import randint
import time
import string


"""with open('wordlist.txt','r') as f:"""
f = open('wordList.txt', 'r')
v = open ('vouls.txt', 'r')
c= open ('cons.txt', 'r')
jumbleSort = ' '
jumble = ''

def jumbler():
    wordsList = []
    for i in range(0, 4):
        voul = randint(0, 4)
        v = open ('vouls.txt')
        lines=v.readlines()
        word = lines[voul]
        wordsList.insert(i, word)
     
    conWordList = []
    for x in range(5, 10):
        con = randint(0, 15)
        c = open ('cons.txt')
        conLines=c.readlines()
        word = conLines[con]
        wordsList.insert(x, word)

    wordJumble = ''.join(wordsList)  
    #print(wordJumble)
    wordJumble = ''.join(sorted(wordJumble))
    print(wordJumble)
    return wordJumble
##print (jumbleSort)

def compare(ch, text): 
    numAppears = 0
    for t in text:
        if t == ch:
            numAppears += 1
    return numAppears

def solved(jumbleSort):

    solution = []
    for line in f:
        for word in line.split():
            if word in jumbleSort:
            	if(len(word) > 2):
                    solution.append(word)
                    print('checking.....')
            else:
        	    continue
    return solution

start_time = time.time()

#anagrams = solved(jumbleSort)

##print("Result:", anagrams)
##print("Solved in %s seconds" % (time.time() - start_time))

userInput = ''
temprompt = None

if (temprompt == None):

    var = input("Would You like to jumble some letters, Yes?: ")

    if ('yes' in var):
        mixer = jumbler()
        done = solved(mixer)
        print(done)
        temprompt
        print("Solved in %s seconds" % (time.time() - start_time))

if(temprompt):
    if ('If you already have the letters lets solve it: Yes' in var):
        solved(mixer)

    #jumble = jumbler()

    #jumbleSort = ''.join(sorted(jumble))
