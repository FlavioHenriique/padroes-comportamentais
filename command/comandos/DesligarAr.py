from command.comandos.Command import Command


class DesligarAr(Command):

    _ar = None

    def __init__(self, ar):
        self._ar = ar

    def executar(self):
        self._ar.desligar()

