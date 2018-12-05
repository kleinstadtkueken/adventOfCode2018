#!/usr/bin/python3

wordList = []
solutionList = []

with open('input.txt', 'r') as file:
    for line in file:
        wordList.append(line[:-1])

for word1 in wordList:
    for word2 in wordList:
        differences = 0
        wordWithoutDifference = ''

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differences += 1
            else:
                wordWithoutDifference += word1[i]

        if differences == 1:
            solutionList.append({word1, word2})
            print(wordWithoutDifference)

print(solutionList)
