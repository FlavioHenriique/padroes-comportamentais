from command.comandos.Command import Command


class LigarTV(Command):

    _tv = None

    def __init__(self, tv):
        self._tv = tv

    def executar(self):
        self._tv.ligar()
