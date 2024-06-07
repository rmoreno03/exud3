
import random
from jugador import Player


class Game:
    def __init__(self, player1: Player, player2: Player, rounds: int):
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = rounds

    def playRound(self):
        charge1 = random.randint(-25, 25)
        result1 = self.__player1.boost(charge1)

        charge2 = random.randint(-25, 25)
        result2 = self.__player2.boost(charge2)

        return [result1, result2]

    def winner(self) -> Player:
        if self.__player1.get_energy() > self.__player2.get_energy():
            return self.__player1
        else:
            return self.__player2

    def play(self):
        for round_number in range(1, self.__rounds + 1):
            results = self.playRound()
            print(f"Round {round_number}: {results}")


if __name__ == "__main__":
    player1 = Player(1, "Jugador1")
    player2 = Player(2, "Jugador2")
    game = Game(player1, player2, 3)
    game.play()
    winner = game.winner()
    print(f"El ganador es: {winner.toString()}")
