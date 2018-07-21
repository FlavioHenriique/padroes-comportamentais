from state.semaforos.Semaforo import Semaforo
from state.semaforos.SemaforoAmarelo import SemaforoAmarelo
from state.semaforos.SemaforoIntermitente import SemaforoIntermitente
from state.semaforos.SemaforoPanic import SemaforoPanic
from state.semaforos.SemaforoVermelho import SemaforoVermelho


class SemaforoVerde(Semaforo):
    def tick(self):
        return SemaforoAmarelo()

    def off(self):
        return SemaforoIntermitente()

    def on(self):
        return SemaforoVermelho()

    def status(self):
        return "Verde"