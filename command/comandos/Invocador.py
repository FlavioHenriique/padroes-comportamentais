class Invocador:

    _comandosLigar = []
    _comandosDesligar = []

    def addLigar(self,comando):
        self._comandosLigar.append(comando)

    def addDesligar(self,comando):
        self._comandosDesligar.append(comando)

    def ligarTodos(self):
        for k in range(len(self._comandosLigar)):
            self._comandosLigar.__getitem__(k).executar()

    def desligarTodos(self):
        for k in range(len(self._comandosDesligar)):
            self._comandosDesligar.__getitem__(k).executar()