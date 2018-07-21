class ArCondicionado:

    _ligado = None
    _temperatura = None

    def ligar(self, temperatura):
        self._temperatura = temperatura
        self._ligado = True
        print("Ar condicionado ligado na temperatura "+ str(self._temperatura))

    def desligar(self):
        self._ligado = False
        print("Ar condicionado desligado")