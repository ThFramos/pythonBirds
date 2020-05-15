lado1=int(input(print("digite o valor do lado A: ")))
lado2=int(input(print("digite o valor do lado B: ")))
lado3=int(input(print("digite o valor do lado C: ")))




def triangulo (a,b,c):

    if (a+b) >= c and (a+c) >= b and (c+b) >= a:
        if a==b and b==c:
            print("triangulo equilatero")
        elif a!=b and b!=c and a!=c:
             print("triangulo escaleno")
        else:
            print("triangulo isosceles")
    else:
        print("não é um tringulo")




triangulo(lado1,lado2,lado3)
