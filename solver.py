from random import randint
import time
import string



#open the .txt files
f = open('wordList.txt', 'r')
v = open ('vouls.txt', 'r')
c= open ('cons.txt', 'r')

words = [line.rstrip() for line in f]

counter = 0
global voulCount
global consCount

# This method takes 4 random strings from a .txt file containing all the vouls
# and 5 random strings from a .txt file containg constanents. The strings are joined and organised 
# alphabetically.
def jumbler():
    wordList = []
    voulCount = 0
    consCount = 0

    while len(wordList) < 9:
        letter = randint(0, 1)

        if (letter == 1 and voulCount < 4):
            voul = randint(0, 4)
            #v = open ('vouls.txt', 'r')
            v = open ('vouls.txt')
            voulLines=v.readlines()
            lines = [line.rstrip() for line in v]
            word = voulLines[voul]
            if word.strip() != '':
                wordList.append(word.strip())
                voulCount = voulCount + 1
         
        
        if (letter == 0 and consCount < 5):
            con = randint(0, 18)
           # c= open ('cons.txt', 'r')
            c = open ('cons.txt')
            lines = [line.rstrip() for line in c]
            conLines=c.readlines()
            word = lines[con]
            if word.strip() != '':
                wordList.append(word.strip())
                consCount = consCount + 1
        

    wordJumble =''.join(wordList)  
    print(wordJumble)
    wordJumble =''.join(sorted(wordList))
    return wordJumble

#simple method that compares two strings when they are arranged alphabetically
#if there are more than 2 matching characters the unordered word is aded to the solution[] list.
def solved(jumbleSort):
    solution = []
    for line in words:
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
    var = raw_input("What would you like to do? Jumble or Solve: ")
    if ('Jumble' in var):
        count = 0
        mixer = jumbler()
        done = solved(mixer)
        #print(done,)
        solved(mixer) 
        	
        
    if("Solve" in var):
        start_time = time.time()
        print('All possible solutions')
        print(done)
        print("Solved in %s seconds" % (time.time() - start_time))
        temprompt
        wordJumble = ""
        selected = None