x=0;
cont1=-1;
cont2=0;
cont3=0;
cont4=0;

while x>=0:
    x= int(input("Digite um número negativo para sair ou algum outro valor: "));
    if x<26:
        cont1+=1;
    else:
        if x<51:
         cont2+=1;

        else:
            if x<76:
                cont3+=1;
            else:
                if x<=100:
                    cont4+=1;
                else:
                    print("Número digitado esta fora do limite");

print("Você fechou o programa!");
print("O total de números digitados netre os valores (0 e 25)é: ",cont1);
print("O total de números digitados netre os valores (26 e 50)é: ",cont2);
print("O total de números digitados netre os valores (51 e 75)é: ",cont3);
print("O total de números digitados netre os valores (76 e 100)é: ",cont4);

