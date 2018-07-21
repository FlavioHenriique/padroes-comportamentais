from observer.observadores.Observador import Observador


class Email(Observador):
    def atualizar(self, forum):
        print("Email - tópicos do fórum:")
        topicos = forum.getTopicos()
        for k in range (len(topicos)):
            print(topicos.__getitem__(k))
