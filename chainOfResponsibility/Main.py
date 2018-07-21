from chainOfResponsibility.Maquina import Maquina
from chainOfResponsibility.slots.Slot01 import Slot01
from chainOfResponsibility.slots.Slot05 import Slot05
from chainOfResponsibility.slots.Slot1 import Slot1
from chainOfResponsibility.slots.Slot10 import Slot10
from chainOfResponsibility.slots.Slot25 import Slot25
from chainOfResponsibility.slots.Slot50 import Slot50

chain = Slot01(0.01)
chain.setProximo(Slot05(0.05))
chain.setProximo(Slot10(0.1))
chain.setProximo(Slot25(0.25))
chain.setProximo(Slot50(0.5))
chain.setProximo(Slot1(1))

maquina = Maquina(chain)

maquina.inserir(1)
maquina.inserir(1)
maquina.inserir(1)
#maquina.inserir(1)

if maquina.receberProduto("Refrigerante"):
    print("Produto recebido")
