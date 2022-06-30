class Board:
    def __init__(self):
        self.size = 3
        self.mat = []

    def initBoard(self):
        for i in range(self.size):
            boardLine = []
            for j in range(self.size):
                boardLine.append(" ")
            self.mat.append(boardLine)

    def printBoard(self):
        print(" " + ("-" * (self.size) + " ") * self.size)
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                print(" " + self.mat[i][j] + " |", end="")
            print()
            print(" " + ("-" * (self.size) + " ") * self.size)
