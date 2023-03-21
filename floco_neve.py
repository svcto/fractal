import time
import turtle

# Configuração da tela
WIDTH, HEIGHT = 1366, 650
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(2*WIDTH, 2*HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# Configuração da tartaruga
trig = turtle.Turtle()
trig.pensize(2)
trig.speed(1)
trig.setpos(-WIDTH // 6, HEIGHT // 6)
trig.color('gold')

# L-system
generation = 5  # número de gerações
axiom = 'F++F++F'  # axioma inicial
chr_1, rule_1 = 'F', 'F-F++F-F'  # regra para o caracter 'F'
step = 400  # comprimento da linha
angle = 60  # ângulo de rotação

def apply_rules(axiom):
    """
    Aplica a regra definida para cada caracter no axioma.
    Retorna o novo axioma.
    """
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])

# def get_result(generation, axiom):
#     for gen in range(generation):
#         axiom = apply_rules(axiom)
#     return axiom

# Iteração para gerar o fractal
for gen in range(generation):
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'Geração: {generation}', font=('Arial', 60, "normal"))

    trig.setheading(0)
    trig.goto(-WIDTH // 6, HEIGHT // 6)
    trig.clear()

    length = step / pow(3, gen)  # novo comprimento da linha para a geração atual

    # Iteração para desenhar a figura
    for chr in axiom:
        if chr == chr_1:
            trig.forward(length)
        elif chr == '+':
            trig.right(angle)
        elif chr == '-':
            trig.left(angle)

    axiom = apply_rules(axiom)  # atualiza o axioma para a próxima geração

screen.exitonclick()
