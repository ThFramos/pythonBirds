temperatura=int();
x=0;
media=0;
soma=0;
while temperatura !=999:
    print("Digite 999 para sair do programa")
    temperatura=int(input("Digite o valor da temperatura:"));
    if temperatura !=999:

        soma= temperatura;
        soma+=soma;
        x += 1;



media = (soma) / x;
print("A média das temperaturas digitadas é:",media);