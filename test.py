import json


#Open and load data.json into wordList
file = open('data.json')
data = json.load(file)
wordList = []
for i in data:
    wordList.append(i)
    
#Input Prompt
word = input("Enter a word to find in the dictionary: ")

if word in wordList:
    print("This word is in the dictionary")

else:
    print("This word is not in the dictionary")
