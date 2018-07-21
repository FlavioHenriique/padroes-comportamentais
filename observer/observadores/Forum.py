class Forum:

    def __init__(self):
        self._observadores = []
        self._topicos = []

    def addTopico(self,topico):
        self._topicos.append(topico)
        self.notificarObservadores()

    def addObservador(self,observador):
        self._observadores.append(observador)

    def getTopicos(self):
        return self._topicos

    def notificarObservadores(self):
        for k in range (len(self._observadores)):
            self._observadores.__getitem__(k).atualizar(self)



