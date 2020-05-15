capital=float(input("Digite o Capital:"));
juros=float(input("Digite a taxa de juros em %: "));
periodo= int(input("Digite o período em meses: "))

taxa= juros/100;

for i in range(1 , periodo+1):
    capital = capital+(capital*taxa);
    print(i,"º mês R$",round(capital,2));
