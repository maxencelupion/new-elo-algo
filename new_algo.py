import math as Math
import random
import numpy as np

class player:
    def __init__(self, index: int, elo: int, win: int, lose: int):
        self.index = index
        self.elo = elo
        self.win = win
        self.lose = lose
        self.last_gain = 0

    def __str__(self):
        return f"Player {self.index} has a elo of {self.elo} and has {self.win} wins and {self.lose} loses, he has gain {self.last_gain} points"
def update_elo(player1: player, player2: player, result: int):
    if (result == 1):
        scorep1 = 1
        scorep2 = 0
        k = 50
        if (player1.elo < 1100):
            if (scorep1 < 0.5):
                k = 20 + (player1.elo - 1000) * 30 / 100
            elif (scorep1 > 0.5):
                    k = 80 - (player1.elo - 1000) * 30 / 100
        elif (player1.elo > 1300):
            k = 32
        e = 1 / (1 + Math.pow(10, (player2.elo - player1.elo) / 400))
        player1.elo = round(player1.elo + k * (scorep1 - e))
        player2.elo = round(player2.elo + k * (scorep2 - e))
        player1.last_gain = round(k * (scorep1 - e))
        player2.last_gain = round(k * (scorep2 - e))
        player1.win = player1.win + 1
        player2.lose = player2.lose + 1
    elif (result == 2):
        k = 50
        scorep1 = 0
        scorep2 = 1
        if (player2.elo < 1100):
            if (scorep2 < 0.5):
                k = 20 + (player2.elo - 1000) * 30 / 100
            elif (scorep2 > 0.5):
                k = 80 - (player2.elo - 1000) * 30 / 100
        elif (player2.elo > 1300):
            k = 32
        e = 1 / (1 + Math.pow(10, (player2.elo - player1.elo) / 400))
        player1.elo = round(player1.elo + k * (scorep1 - e))
        player2.elo = round(player2.elo + k * (scorep2 - e))
        player1.last_gain = round(k * (scorep1 - e))
        player2.last_gain = round(k * (scorep2 - e))
        player1.lose = player1.lose + 1
        player2.win = player2.win + 1

def create_player(index: int, elo: int, win: int, lose: int):
    return player(index, elo, win, lose)

def battle(player1: player, player2: player):
    if (player1.elo == player2.elo):
        if random.randint(0, 100) <= 50:
            update_elo(player1, player2, 1)
        else :
            update_elo(player1, player2, 2)
    if (player1.elo > player2.elo):
        nb1 = random.randint(0, 50 + round(((player1.elo - player2.elo) / 15)))
        if random.randint(0, 100) <= nb1:
            update_elo(player1, player2, 1)
        else:
            update_elo(player1, player2, 2)
    else :
        nb2 = random.randint(0, 50 + round(((player2.elo - player1.elo) / 15)))
        if random.randint(0, 100) <= nb2:
            update_elo(player1, player2, 2)
        else:
            update_elo(player1, player2, 1)



if __name__ == '__main__':
    player_list = []
    player_list.append(create_player(1, 1000, 0, 0))
    player_list.append(create_player(2, 1000, 0, 0))
    for i in range(10):
        battle(player_list[0], player_list[1])
        print(player_list[0])
        print(player_list[1])
        print("\n")
