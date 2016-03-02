from random import randint
import time
import string


#with open('wordlist.txt','r') as f:
#open the .txt files
f = open('wordList.txt', 'r')
v = open ('vouls.txt', 'r')
c= open ('cons.txt', 'r')

wordList = []

# This method takes 4 random strings from a .txt file containing all the vouls
# and 5 random strings from a .txt file containg constanents. The strings are joined and organised 
# alphabetically.
def jumbler():
    for i in range(0, 4):
        voul = randint(0, 4)
        v = open ('vouls.txt')
        lines=v.readlines()
        word = lines[voul]
        wordsList.insert(i, word)
     
    conWordList = []
    for x in range(5, 10):
        con = randint(0, 19)
        c = open ('cons.txt')
        conLines=c.readlines()
        word = conLines[con]
        wordsList.insert(x, word)

    wordJumble = ''.join(wordList)  
    #print(wordJumble)
    wordJumble = ''.join(sorted(wordJumble))
    print(wordJumble)
    return wordJumble

def getVoul():
    voul = randint(0, 4)
    v = open ('vouls.txt')
    lines=v.readlines()
    word = lines[voul]
    wordList.append(word)
    wordJumble = ''.join(wordList)  
    return 

def getConstenent():
    con = randint(0, 19)
    c = open ('cons.txt')
    conLines=c.readlines()
    word = conLines[con]
    wordList.append(word)
    wordJumble = ''.join(wordList)  
    return 

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


temprompt = None
selected = None
voulCount = 0
conCount = 0

while (temprompt == None): 
    var = input("What would you like to do? Select or Solve: ")
  #  if ('Jumble' in var): 
   #     mixer = jumbler() 
    #    done = solved(mixer)
     #   solved(mixer)   
      #  selected
    if('Solve' in var):
        start_time = time.time()
        done = solved(wordJumble)
        print('All possible solutions')
        print(done)
        print("Solved in %s seconds" % (time.time() - start_time))
        temprompt
        wordJumble = " "

    while(selected == None):

        if('Select' in var):
            letter = input("Would you like a voul(V) or constanent (C)")

        if('V' in letter):
            if(voulCount < 4):
                getVoul()
                voulCount += 1
                wordJumble = ''.join(wordList)  
                wordJumble = ''.join(sorted(wordJumble))
                print(wordJumble)
            else: selected = True

        if('C' in letter, conCount < 5):
            if(conCount < 5):
                getConstenent()
                conCount += 1
                wordJumble = ''.join(wordList)  
                wordJumble = ''.join(sorted(wordJumble))
                print(wordJumble)
            else: selected = True
    