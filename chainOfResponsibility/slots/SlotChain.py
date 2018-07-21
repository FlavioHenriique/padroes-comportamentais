class SlotChain:

    _proximo = None

    def __init__(self,moeda):
        self._moeda = moeda


    def setProximo(self,proximoMetodo):
        if self._proximo == None:
            self._proximo = proximoMetodo
        else:
            self._proximo.setProximo(proximoMetodo)

    def inserirMoeda(self, valorMoeda):
            if self.verificaMoeda(valorMoeda):
                return True
            else:
                return self._proximo.inserirMoeda(valorMoeda)

    def verificaMoeda(self, valorMoeda):
        return valorMoeda == self._moeda