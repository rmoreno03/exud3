# test.py

import unittest
from jugador import Player
from game import Game


class Test(unittest.TestCase):

    def test1(self):
        player = Player(1, 'a')
        self.assertEqual(player.get_energy(), (100 + 0) / 2)

    def test2(self):
        player = Player(2, 'b')
        charge, resulting_energy = player.boost(-100)
        min_energy = 0
        self.assertTrue(resulting_energy == min_energy)

    def test3(self):
        player = Player(3, 'c')
        charge, resulting_energy = player.boost(200)
        max_energy = 100
        self.assertTrue(resulting_energy == max_energy)

    def test4(self):
        player1 = Player(4, 'player1')
        player2 = Player(5, 'player2')
        game = Game(player1, player2, 1)
        player1.boost(20)
        player2.boost(10)
        self.assertEqual(game.winner(), player1)


if __name__ == "__main__":
    unittest.main()
