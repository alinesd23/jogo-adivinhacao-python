import random 
numero_secreto = random.randint(1, 10)
 
print("=== jogo da adivinhação ===")
print("tente adivinhar o número de 1 a 10")

tentativas = 0 

while True:
    palpite = int(input("Digite seu palpite"))
    tentativas +=1

    if palpite == numero_secreto:
        print(f"Parabéns! você acertou em {tentativas} tentativas!")
        break

    elif palpite < numero_secreto:
        print("o número é maior!")

    else:
        print("o número é menor!")

