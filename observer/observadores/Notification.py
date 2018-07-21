from observer.observadores.Observador import Observador


class Notification(Observador):
    def atualizar(self, forum):
        print("Notification - tópicos do fórum:")
        topicos = forum.getTopicos()
        for k in range (len(topicos)):
            print(topicos.__getitem__(k))
