import math as Math
import random
import numpy as np


class player:
    def __init__(self, index: int):
        self.index = index
        self.elo = random.randint(1000, 1100)
        self.win = 0
        self.lose = 0
        self.nb_game = 0
        self.last_gain = 0

    def __str__(self):
        return f"Player {self.index} has a elo of {self.elo} and has {self.win} wins and {self.lose} loses, he has gain {self.last_gain} points"


def print_change_elo(player1: player, player2: player):
    print(
        f"Player {player1.index} was {player1.elo - player1.last_gain} LP and is now {player1.elo} LP ({player1.last_gain}), Player {player2.index} was {player2.elo - player2.last_gain} LP and is now {player2.elo} LP ({player2.last_gain})")
    return


def update_elo(player1: player, player2: player, result: int):
    e = 1 / (1 + Math.pow(10, (player2.elo - player1.elo) / 400))
    if result == 1:
        scorep1 = 1
        scorep2 = 0
        k = 50
        if player1.elo < 1100:
            if scorep1 < 0.5:
                k = 20 + (player1.elo - 1000) * 30 / 100
            elif scorep1 > 0.5:
                k = 80 - (player1.elo - 1000) * 30 / 100
        elif player1.elo > 1300:
            k = 32
        player1.elo = round(player1.elo + k * (scorep1 - e))
        player2.elo = round(player2.elo + k * (scorep2 - e))
        player2.last_gain = round(k * (scorep2 - e))
        if player2.elo < 800:
            player2.elo = 800
            player2.last_gain = 0
        player1.last_gain = round(k * (scorep1 - e))
        player1.win = player1.win + 1
        player2.lose = player2.lose + 1
        print_change_elo(player1, player2)
        return
    elif result == 2:
        k = 50
        scorep1 = 0
        scorep2 = 1
        if player2.elo < 1100:
            if scorep2 < 0.5:
                k = 20 + (player2.elo - 1000) * 30 / 100
            elif scorep2 > 0.5:
                k = 80 - (player2.elo - 1000) * 30 / 100
        elif player2.elo > 1300:
            k = 32
        player1.elo = round(player1.elo + k * (scorep1 - e))
        player2.elo = round(player2.elo + k * (scorep2 - e))
        player1.last_gain = round(k * (scorep1 - e))
        if player1.elo < 800:
            player1.elo = 800
            player1.last_gain = 0
        player2.last_gain = round(k * (scorep2 - e))
        player1.lose = player1.lose + 1
        player2.win = player2.win + 1
        print_change_elo(player1, player2)
        return


def matchmaking(player_list: list):
     for i in range(len(player_list)):
         for j in range(i + 1, len(player_list)):
             battle(player_list[i], player_list[j])


def create_player(index):
    return player(index)


def battle(player1: player, player2: player):
    player1.nb_game = player1.nb_game + 1
    player2.nb_game = player2.nb_game + 1
    if player1.elo == player2.elo:
        if random.randint(0, 100) <= 50:
            update_elo(player1, player2, 1)
            return
        else:
            update_elo(player1, player2, 2)
            return
    if player1.elo > player2.elo:
        nb1 = random.randint(0, 50 + round(((player1.elo - player2.elo) / 1)))
        if random.randint(0, 100) <= nb1:
            update_elo(player1, player2, 1)
            return
        else:
            update_elo(player1, player2, 2)
            return
    else:
        nb2 = random.randint(0, 50 + round(((player2.elo - player1.elo) / 1)))
        if random.randint(0, 100) <= nb2:
            update_elo(player1, player2, 2)
            return
        else:
            update_elo(player1, player2, 1)
            return


if __name__ == '__main__':
    player_list = []
    nb_player = int(input("How many players do you want ?"))
    for i in range(0, nb_player):
        player_list.append(create_player(i))
    matchmaking(player_list)
