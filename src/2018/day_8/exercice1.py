#!/usr/bin/python3


class Node:
    def __init__(self, childNodeQuantity, metaDataQuantity):
        self.childNodeQuantity = childNodeQuantity
        self.metaDataQuantity = metaDataQuantity
        self.childNodes = []
        self.metaDataNodes = []


metaDataSum = 0


with open('input.txt', 'r') as file:
    for line in file:
        input = list(map(lambda s: int(s), line.split(' ')))


def parseChildren(elements):
    global metaDataSum
    currentNode = Node(elements.pop(0), elements.pop(0))

    for i in range(currentNode.childNodeQuantity):
        childNode, elements = parseChildren(elements)
        currentNode.childNodes.append(childNode)


    for i in range(currentNode.metaDataQuantity):
        metaData = elements.pop(0)
        metaDataSum += metaData
        currentNode.metaDataNodes.append(metaData)

    return currentNode, elements


root, _ = parseChildren(input)





print(metaDataSum)
