class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.wins = 0

    def checkName(self):
        while self.name == "" or self.name == " ":
            self.name = input("Enter your name again: ")
        return

    def setNumOfPlayers():
        numOfplayers = 0
        try:
            numOfplayers = int(input("Enter num of players: "))
        except ValueError:
            # while numOfplayers != 2 or numOfplayers != 1:
            return Player.setNumOfPlayers()
        else:
            if numOfplayers == 2 or numOfplayers == 1:
                return numOfplayers
            return Player.setNumOfPlayers()
