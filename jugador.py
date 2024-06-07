# jugador.py

MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:
    def __init__(self, idPlayer: int, nickName: str):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY + MIN_ENERGY) / 2

    def get_idPlayer(self) -> int:
        return self.__idPlayer

    def get_nickName(self) -> str:
        return self.__nickName

    def get_energy(self) -> int:
        return self.__energy

    def set_idPlayer(self, idPlayer: int):
        self.__idPlayer = idPlayer

    def set_nickName(self, nickName: str):
        self.__nickName = nickName

    def __set_energy(self, energy: int):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self.__energy = energy
        elif energy < MIN_ENERGY:
            self.__energy = MIN_ENERGY
        else:
            self.__energy = MAX_ENERGY

    def toString(self) -> str:
        return f'[{self.__idPlayer}, {self.__nickName}, {self.__energy}]'

    def boost(self, charge) -> (int, int):
        if not isinstance(charge, int):
            charge = 0
        new_energy = self.__energy + charge
        self.__set_energy(new_energy)
        return charge, self.__energy

if __name__ == "__main__":
    jugador = Player(1, "Jugador1")
    print(jugador.toString())
    print(jugador.boost(30))
    print(jugador.boost(-90))
    print(jugador.boost(120))
    print(jugador.boost("50"))
    print(jugador.toString())
