while True:
    try:
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        if x == 0 or y == 0:
            break
        elif x == 0:
            print("Eixo Y")
        elif y == 0:
            print("Eixo X")
        elif x > 0 and y > 0:
            print("Primeiro Quadrante")
        elif x < 0 and y > 0:
            print("Segundo Quadrante")
        elif x < 0 and y < 0:
            print("Terceiro Quadrante")
        else:
            print("Quarto Quadrante")
    except ValueError:
        print("Por favor, insira números inteiros válidos.")