# Programação Orientada a Objetos
#-- 5 classes
#-- 3 atributos
#-- 1 funcao

from Computadores import Computador
from Livros import Livro
from Teclados import Teclado
from Monitores import Monitor
from Xicaras import Xicara

c = Computador("Dell", 1)
c.ligar()

livro1 = Livro() #instancia
livro1.terminou()

livro2 = Livro()
print(Livro.titulo)

t = Teclado()
t.capsLook()
# tem o atributo na classe então não precisa instanciar 
print(Teclado.marca) 

monitor = Monitor()
monitor.ligado()
print(Monitor.tamanhoTela, Monitor.marca)

x = Xicara("Café", 200, "Leite")
x.tipoBebida()