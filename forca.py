# Jogo da Forca -- adaptado de https://youtu.be/_A_2aTFHzJ0?si=N2XN-35MLTjvajMo
#Novo teste
#Um teste novo
from palavraforca import palavra

letras_usuario = []
chances = 4
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print(" _ ", end=" ")

    print(f"Você tem {chances} chances!")

    tentativa = input("Escolha uma letra: ")
    letras_usuario.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
         break

if ganhou:
    # encerra o jogo
    print(f"Parabéns! Você ganhou, a palavra era {palavra}")
else:
    # encerra o jogo
    print(f"Você perdeu, a palavra era {palavra}")
