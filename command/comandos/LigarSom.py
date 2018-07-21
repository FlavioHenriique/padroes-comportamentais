from command.comandos.Command import Command


class LigarSom(Command):

    _som = None

    def __init__(self, som, horario):
        self._som = som
        self._horario = horario

    def executar(self):
        self._som.ligar(self._horario)



