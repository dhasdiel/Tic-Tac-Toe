import os


class GameControl:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.isGameOver = False

    # def getIsGameOver(self):
    #     return self.isGameOver

    # def setIsGameOver(self, bool):
    #     self.isGameOver = bool

    def playerTurn(self, player):
        mat = self.board.mat
        name = player.name
        sign = player.sign
        while True:
            print(f"{name} you play as {sign}")
            try:
                row, col = input(
                    "Please enter a row and col between 1-3 (in this format 'row,col'): ").split(",")
                row = int(row) - 1
                col = int(col) - 1
            except ValueError:
                pass
            else:
                if row >= 0 and row <= 2 and col >= 0 and col <= 2 and mat[row][col] == " ":
                    mat[row][col] = sign
                    break

    def checkWinner(self):
        size = self.board.size
        mat = self.board.mat
        # rows
        for x in range(size):
            row = set([mat[x][0], mat[x][1], mat[x][2]])
            if len(row) == 1 and mat[x][0] != " ":
                self.isGameOver = True
                return f"Player {mat[x][0]} win!"
        # columns
        for x in range(size):
            column = set([mat[0][x], mat[1][x], mat[2][x]])
            if len(column) == 1 and mat[0][x] != " ":
                self.isGameOver = True
                return f"Palyer {mat[0][x]} win!"
        # diagonals
        diag1 = set([mat[0][0], mat[1][1], mat[2][2]])
        diag2 = set([mat[0][2], mat[1][1], mat[2][0]])
        if (len(diag1) == 1 or len(diag2) == 1) and mat[1][1] != " ":
            self.isGameOver = True
            return f"Player {mat[1][1]} win!"
        return "Keep playing!!!"

    def startGame(self):
        board = self.board
        players = [self.player1, self.player2]
        # os.system('clear')
        print("The game is begining...")
        board.initBoard()
        board.printBoard()
        while not self.isGameOver:
            for player in players:
                self.playerTurn(player)
                board.printBoard()
                message = self.checkWinner()
                if message != "Keep playing!!!":
                    player.wins += 1
                    print(message)
                    break
