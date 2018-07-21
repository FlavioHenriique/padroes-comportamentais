from state.semaforos.Semaforo import Semaforo
from state.semaforos.SemaforoAmarelo import SemaforoAmarelo
from state.semaforos.SemaforoIntermitente import SemaforoIntermitente
from state.semaforos.SemaforoPanic import SemaforoPanic
from state.semaforos.SemaforoVerde import SemaforoVerde
from state.semaforos.SemaforoVermelho import SemaforoVermelho


class SemaforoVermelho(Semaforo):

    def tick(self):
        return SemaforoVerde()

    def off(self):
        return SemaforoIntermitente()

    def on(self):
        return SemaforoVermelho()

    def status(self):
        return "Vermelho"