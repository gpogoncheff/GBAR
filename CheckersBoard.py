from GameObservable import *
from PieceFactory import *
from Space import *
from PieceFactory import *
import numpy as np

class CheckersBoard(GameObservable):

    def __init__(self):
        super().__init__()
        self._pieceFactory = PieceFactory()
        self.playerPieces = []
        self.spaces = [[Space(locationJ=j, locationI=i) for i in range(0, 8)] for j in range(0, 8)]
        self.moveOptions = [{'moveLeft':(1,1), 'moveRight':(1,-1), 'jumpLeft':(2,2), 'jumpRight':(2,-2)}, {'moveLeft':(-1,-1), 'moveRight':(-1,1), 'jumpLeft':(-2,-2), 'jumpRight':(-2,2)}]

    def addObserver(self, player):
        super().addObserver(player)
        self.playerPieces.append([None for pieceNumber in range(0, 12)])


    def initializeGameBoard(self):
        assert (len(self._observers) == 2), 'Must have two players to start game'
        pieceCounter = 0
        for i in range(0, 3):
            for j in range(0, len(self.spaces), 2):
                if ((i % 2) == 0):
                    # initialize player1 pieces for even rows
                    self.playerPieces[0][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{0:02d}'.format(pieceCounter), pieceLocation=(i, j+1))
                    self.spaces[i][j+1].setSpaceOwner(self.playerPieces[0][pieceCounter])

                    # initialize player2 pieces for even rows
                    self.playerPieces[1][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{0:02d}'.format(pieceCounter), pieceLocation=(7-i, j))
                    self.spaces[7-i][j].setSpaceOwner(self.playerPieces[1][pieceCounter])
                else:
                    # initialize player1 pieces for odd rows
                    self.playerPieces[0][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='X{0:02d}'.format(pieceCounter), pieceLocation=(i, j))
                    self.spaces[i][j].setSpaceOwner(self.playerPieces[0][pieceCounter])
                    # initialize player2 pieces for odd rows
                    self.playerPieces[1][pieceCounter] = self._pieceFactory.getPiece(pieceOwner='O{0:02d}'.format(pieceCounter), pieceLocation=(7-i, j+1))
                    self.spaces[7-i][j+1].setSpaceOwner(self.playerPieces[1][pieceCounter])
                pieceCounter += 1

    def getState(self):
        pass

    def setState(self):
        pass

    def getSpaceByLocation(self, i, j):
        returnSpace = None
        if (i >= 0 and j < len(self.spaces)) and (i >= 0 and j < len(self.spaces[0])):
            returnSpace = self.spaces[i][j]
        return returnSpace

    #for testing
    def printBoard(self):
        for row in self.spaces:
            print(['---' if (space.getSpaceOwner() is None) else space.getSpaceOwner()._owner for space in row])
