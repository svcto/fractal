import turtle   # Importando a biblioteca turtle

# Criando um loop que vai de 0 a 650 com incremento de 10
for i in range(0, 650, 10):
    turtle.pensize(5)   # Configurando o tamanho da caneta
    turtle.speed(100)   # Configurando a velocidade de desenho da tartaruga

    turtle.forward(i)   # Movendo a tartaruga para frente em i unidades
    turtle.left(90)   # Rotacionando a tartaruga 90 graus para a esquerda

turtle.Screen().exitonclick()   # Esperando um clique do mouse para fechar a janela gráfica
