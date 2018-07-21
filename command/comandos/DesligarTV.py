from command.comandos.Command import Command


class DesligarTV(Command):

    _tv = None

    def __init__(self, tv):
        self._tv = tv

    def executar(self):
        self._tv.desligar()
