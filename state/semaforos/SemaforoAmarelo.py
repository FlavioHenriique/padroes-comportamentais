from state.semaforos.Semaforo import Semaforo
import state.semaforos.SemaforoIntermitente



class SemaforoAmarelo(Semaforo):

    def tick(self):
        return state.semaforos.SemaforoVermelho()

    def off(self):
        return state.semaforos.SemaforoIntermitente.SemaforoIntermitente()

    def on(self):
        return state.semaforos.SemaforoVermelho()

    def status(self):
        return "Amarelo"