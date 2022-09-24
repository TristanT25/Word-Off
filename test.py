import json


#Open and load data.json into wordList
file = open('data.json')
data = json.load(file)
wordList = []
for i in data:
    wordList.append(i)
    
#Input Prompt
word = []
while(1):
    letter = input("Enter a letter: ")
    word.append(letter)
    word2 = "".join(word)
    if (len(word)>3) and (word2 in wordList):
        print("You lost! Better luck next time.")
        break

