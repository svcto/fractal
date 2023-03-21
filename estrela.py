import turtle   # Importando a biblioteca turtle
from random import random, randint   # Importando as funções random e randint da biblioteca random

turtle.pensize(5)   # Configurando o tamanho da caneta
turtle.colormode(255)   # Configurando o modo de cores da tartaruga para 255 (RGB)

# Criando um loop que vai de 0 a 4999
for i in range(5000):
    # Configurando uma cor aleatória para a tartaruga usando a função randint do módulo random
    turtle.color(randint(0, 150), randint(0, 150), randint(0, 150))
    turtle.forward(200)   # Movendo a tartaruga para frente em 200 unidades
    turtle.left(216)   # Rotacionando a tartaruga 216 graus para a esquerda

turtle.Screen().exitonclick()   # Esperando um clique do mouse para fechar a janela gráfica
