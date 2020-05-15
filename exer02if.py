nome= input("Nome:");
nota01= float(input("Digite o valor da primeira nota: "));
nota02= float(input("Digite o valor da segunda nota: "));
nota03= float(input("Digite o valor da terceira nota: "));
media= (nota01+nota02+nota03)/3;

if media>5:
    if media <7:
        print("O aluno ",nome, " com a média ",round(media,1)," está de recuperação");
    else:
        print("O aluno ",nome, " com a média ",round(media,1)," está aprovado");
else:
    print("O aluno ", nome, " com a média ", round(media,1), " está reprovado");