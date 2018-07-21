from command.comandos.Command import Command


class DesligarSom(Command):

    _som = None

    def __init__(self,som):
        self._som = som

    def executar(self):
        self._som.desligar()


