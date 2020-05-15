nome= input("Digite o nome: ");
altura= float(input("Digite a altura: "));
peso= float(input("Digite o peso: "));
imc= peso/ altura**2;
print(nome," possui o IMC de ", round(imc,3));