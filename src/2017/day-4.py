#!/usr/bin/python3

validPhrases = 0
validPhrases2 = 0

with open('day-4.txt', 'r') as file:
    for line in file:
        phraseList = line[:-1].split(' ')
        phraseSet = set(phraseList)

        if len(phraseList) == len(phraseSet):
            validPhrases += 1


        sortedWordsList = list(map(lambda w: ''.join(sorted(w)), phraseList))
        sortedWordsSet = set(sortedWordsList)

        if len(sortedWordsList) == len(sortedWordsSet):
            validPhrases2 += 1


print(validPhrases)
print(validPhrases2)

