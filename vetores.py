meuVetor = [1,2,3,4,5,6,7,8,9,10]


for i in range(0,10):
    meuVetor[i] = meuVetor[i]*2
print(meuVetor)

for i in meuVetor:
    print(i)



precosItens = list(range(0,3))

for i in range(0,3):
    precosItens[i] = float(input("Digite o valor do item"))

for i in range (0,3):
    print("O preço do item",i+i,"é", precosItens[i])
