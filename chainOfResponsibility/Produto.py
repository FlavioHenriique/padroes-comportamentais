class Produto:

    def __init__(self,nome,valor):
        self._nome = nome
        self._valor = valor

    def getValor(self):
        return self._valor

    def getNome(self):
        return self._nome

