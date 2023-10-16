from random import randint
from Player import Player

class RandomPlayer(Player):

    def name(self):
        return "Random"

    #
    # retorna a coluna onde a bola será jogada
    #
    def move(self, player_code, board, depth):
        return randint(0, 6)
