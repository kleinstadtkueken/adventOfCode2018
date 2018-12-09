#!/usr/bin/python3

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

def printBoard(startNode, currentMarble, currentPlayer):
    current = startNode
    print(f'[{currentPlayer + 1}] {current.value}', end=" ")
    current = current.next
    while current is not startNode:
        if current is currentMarble:
            print(f'({current.value})', end="")
        else:
            print(f' {current.value} ', end="")
        current = current.next
    print()


numberPlayers = 470
lastMarble = 72170 * 100


board = Node(0, None, None)
board.next = board
board.prev = board
currentMarble = board

players = [0 for i in range(numberPlayers)]
currentPlayer = -1


for marble in range(1, lastMarble + 1):
    currentPlayer = (currentPlayer + 1) % numberPlayers

    if marble % 23 == 0:
        for i in range(7):
            currentMarble = currentMarble.prev

        players[currentPlayer] += (marble + currentMarble.value)
        currentMarble.prev.next = currentMarble.next
        currentMarble.next.prev = currentMarble.prev
        currentMarble = currentMarble.next

    else:
        currentMarble = currentMarble.next

        insertedMarble = Node(marble, currentMarble, currentMarble.next)
        currentMarble.next.prev = insertedMarble
        currentMarble.next = insertedMarble
        currentMarble = insertedMarble

    # printBoard(board, currentMarble, currentPlayer)




print(max(players))
