from Board import Board
from Player import Player
from GameControl import GameControl
from Bot import Bot
import time


players = Player.setNumOfPlayers()

if players == 2:
    player1 = Player(input("Enter player 1 name: "), "X")
    player1.checkName()
    player2 = Player(input("Enter player 2 name: "), "O")
    player2.checkName()
    rounds = int(input("Enter number of rounds: "))

    tic = time.perf_counter()

    while rounds != 0 or rounds == -1:

        print(f"\nRound number #{rounds}\n")
        game = GameControl(Board(), player1, player2)
        game.startGame()
        rounds -= 1

    toc = time.perf_counter()
    print(
        f"\nBuild finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
    print(f"{player1.name} won {player1.wins} times and {player2.name} won {player2.wins} times.")
else:
    player = Player(input("Enter your name: "), "X")
    bot = Bot()
