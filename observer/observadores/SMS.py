from observer.observadores.Observador import Observador

class SMS(Observador):
    def atualizar(self, forum):
        print("SMS - tópicos do fórum:")
        topicos = forum.getTopicos()
        for k in range (len(topicos)):
            print(topicos.__getitem__(k))
