from command.aparelhos.ArCondicionado import ArCondicionado
from command.aparelhos.Som import Som
from command.aparelhos.TV import TV
from command.comandos.DesligarAr import DesligarAr
from command.comandos.DesligarSom import DesligarSom
from command.comandos.DesligarTV import DesligarTV
from command.comandos.Invocador import Invocador
from command.comandos.LigarAr import LigarAr
from command.comandos.LigarSom import LigarSom
from command.comandos.LigarTV import LigarTV

invocador = Invocador()

tv = TV()
ar = ArCondicionado()
som = Som()

# Adicionando comandos de ligar aparelhos
invocador.addLigar(LigarTV(tv))
invocador.addLigar(LigarSom(som,"10:30"))
invocador.addLigar(LigarAr(ar,"20"))

# Adicionando comandos de desligar aparelhos
invocador.addDesligar(DesligarTV(tv))
invocador.addDesligar(DesligarSom(som))
invocador.addDesligar(DesligarAr(ar))

print("Ligando todos os aparelhos:")
invocador.ligarTodos()

print("Desligando todos os aparelhos:")
invocador.desligarTodos()
