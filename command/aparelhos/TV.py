class TV:
    _ligado = None

    def ligar(self):
        self._ligado = True
        print("TV ligada")

    def desligar(self):
        self._ligado = False
        print("TV desligada")