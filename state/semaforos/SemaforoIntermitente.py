from state.semaforos.Semaforo import Semaforo
from state.semaforos.SemaforoVermelho import SemaforoVermelho


class SemaforoIntermitente(Semaforo):
    def tick(self):
        return self

    def off(self):
        return self

    def on(self):
        return SemaforoVermelho()

    def status(self):
        return "Amarelo Intermitente"