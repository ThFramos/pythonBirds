lado1=input(print("digite o valor do lado A: "))
lado2=input(print("digite o valor do lado B: "))
lado3=input(print("digite o valor do lado C: "))




def triangulo (a,b,c):
    if (a+b) >= c and (a+c) >= b and (c+b) >= a:
        return print("è um triangulo")
    else:
        return print("não é um tringulo")




triangulo(lado1,lado2,lado3)