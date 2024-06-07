from jugador import Player

def main():
    jugador = Player(1, "Jugador1")
    print(jugador.toString())
    print(jugador.boost(30))
    print(jugador.boost(-90))
    print(jugador.boost(120))
    print(jugador.boost("50"))
    print(jugador.toString())

if __name__ == "__main__":
    main()
