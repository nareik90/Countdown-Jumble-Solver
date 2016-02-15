#Kieran Redington

#G00245082

##Countdown word jumble solver in Python

###Summary
The aim of this program is to tae a 9 char string and identify the longest possible
word that can be create from the Oxford English dictionary. The word scrambler must follow the 
rules outlined by the popular tv show "Countdown". The rules can be found at https://en.wikipedia.org/wiki/Countdown_(game_show)

###Code:
Originaly started by adding all the possible orderings of the 9 chars to  a list but found that the factorial 
possibilities caused the program to crash. 9 factorial was to large a number to process economically.

					while factorial(9):
						if s not in list:
							continue
						else:
							s = (random.sample(word, len(word)))
							list = []
							list.append(s)

					print (list)


Update:
Decided to try reording the jumble word in alphaebetical order then comparing that to the alphaebetical order
of the words in the dictionary. If there are 3 letter matches then the unordered word is added to the variable and continue
until longest word is found.

					jumbleSort = ''.join(sorted(s))

####References:
http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
http://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python
https://docs.python.org/2/tutorial/datastructures.html#