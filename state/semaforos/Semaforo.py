class Semaforo(object):

    def tick(self):
        raise NotImplementedError

    #def panic(self):
     #   return SemaforoPanic()

    def off(self):
        raise NotImplementedError

    def on(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError