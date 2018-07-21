class Som:
    _ligado = None
    _tempo = None

    def ligar(self,tempo):
        self._ligado = True
        self._tempo = tempo
        print("Som ligado as "+ str(tempo))

    def desligar(self):
        self._ligado  = False
        print("Som desligado")