from command.comandos.Command import Command


class LigarAr(Command):

    _ar = None

    def __init__(self,ar, temperatura):
        self._ar = ar
        self._temperatura = temperatura


    def executar(self):
        self._ar.ligar(self._temperatura)

