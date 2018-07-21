from chainOfResponsibility.Produto import Produto


class Maquina:

    def __init__(self,chain):
        self._chain = chain
        self._acumulado = 0
        self._produtos = self.adicionaProdutos()

    def inserir(self,valor):
        if self._chain.inserirMoeda(valor):
            self._acumulado += valor

    def getProdutos(self):
        return self._produtos

    def receberProduto(self, produto):

        prod = None
        for k in range (len(self._produtos)):
            if self._produtos.__getitem__(k).getNome() == produto:
                prod = self._produtos.__getitem__(k)

        if  self._acumulado >= prod.getValor():
            return True
        print("Valor inserido não é suficiente. acumulado: "+ str(self._acumulado))

    def adicionaProdutos(self):
        p1 = Produto("Refrigerante",3.5)
        p2 = Produto("Salgadinhos", 2)
        p3 = Produto("Chocolate", 1)
        produtos = []
        produtos.append(p1)
        produtos.append(p2)
        produtos.append(p3)
        return produtos
