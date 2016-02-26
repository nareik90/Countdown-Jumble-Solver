from random import randint
import time
import string


#with open('wordlist.txt','r') as f:
#open the .txt files
f = open('wordList.txt', 'r')
v = open ('vouls.txt', 'r')
c= open ('cons.txt', 'r')

# This method takes 4 random strings from a .txt file containing all the vouls
# and 5 random strings from a .txt file containg constanents. The strings are joined and organised 
# alphabetically.
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

#This method was to originaly compare the unorganised strings but decided to go with 
#the solved method instead.
#def compare(ch, text): 
 #   numAppears = 0
  #  for t in text:
   #     if t == ch:
    #        numAppears += 1
    #return numAppears

#simple method that compares two strings when they are arranged alphabetically
#if there are more than 2 matching characters the unordered word is aded to the solution[] list.
def solved(jumbleSort):
    solution = []
    for line in f:
        for word in line.split():
            sort = ''.join(sorted(word))
            if sort in jumbleSort:
            	if(len(word) > 2):
                    solution.append(word)
                   
            else:
        	    continue
    return solution

start_time = time.time()


temprompt = None

if (temprompt == None):

    var = input("Would You like to jumble some letters, Yes?: ")

    if ('yes' in var):
        mixer = jumbler()
        done = solved(mixer)
        print('All possible solutions')
        print(done)
        temprompt
        print("Solved in %s seconds" % (time.time() - start_time))

if(temprompt):
    if ('If you already have the letters lets solve it: Yes' in var):
        solved(mixer)

