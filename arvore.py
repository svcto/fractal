import turtle   # Importando a biblioteca turtle

turtle.bgcolor("black")  # Definindo a cor de fundo da tela como preto

arv = turtle.Turtle()   # Criando uma instância do objeto turtle
arv.pensize(2)   # Configurando o tamanho da caneta
arv.color("green")  # Configurando a cor da caneta
arv.left(89)   # Rotacionando a tartaruga 89 graus para a esquerda
arv.backward(70)   # Movendo a tartaruga para trás em 70 unidades
arv.speed(199999)   # Configurando a velocidade de desenho da tartaruga

def drawTree(i):   # Definindo a função drawTree que recebe um parâmetro i
    if i < 15:   # Se i for menor que 15, a função retorna sem fazer nada
        # print("Inside")
        return
    else:
        # print("Quitside")
        arv.forward(i)   # Move a tartaruga para frente em i unidades
        arv.color("magenta")   # Configurando a cor da caneta como magenta
        arv.circle(2)   # Desenhando um círculo de raio 2
        arv.color("brown")   # Configurando a cor da caneta como marrom
        arv.left(30)   # Rotacionando a tartaruga 30 graus para a esquerda
        drawTree(3*i/4)   # Chamando a função drawTree com um valor reduzido de i
        arv.right(60)   # Rotacionando a tartaruga 60 graus para a direita
        drawTree(3*i/4)   # Chamando a função drawTree com um valor reduzido de i
        arv.left(30)   # Rotacionando a tartaruga 30 graus para a esquerda
        arv.backward(i)   # Movendo a tartaruga para trás em i unidades

drawTree(100)   # Chamando a função drawTree com um valor inicial de i igual a 100
turtle.done()   # Finalizando a janela gráfica```
