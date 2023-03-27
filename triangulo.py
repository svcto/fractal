import turtle  # importa a biblioteca turtle

n = 10  # define o número de iterações
pen = turtle.Turtle()  # cria uma tartaruga chamada "pen"

# inicia um loop que desenha um triângulo equilátero com n lados
for i in range(n * 3):  # repete n * 3 vezes
    pen.forward(i * 10)  # move a tartaruga para a frente por i * 10 unidades
    pen.right(120)  # gira a tartaruga 120 graus para a direita

turtle.done()  # exibe o desenho concluído
