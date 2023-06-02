import random

# Lista de temas e suas palavras correspondentes
temas = {
    '1': ['Entrada', 'canape', 'bruschettas', 'nachos'],
    '2': ['Almoco', 'buchada', 'pirao', 'peixada'],
    '3': ['Sobremesa', 'sorvete', 'pave', 'mousse']
}

# Função para escolher um tema
def escolher_tema():
    print("Escolha um tema:")
    print("1. Entrada")
    print("2. Almoco")
    print("3. Sobremesa")
    tema = input("Digite o número do tema desejado: ")
    while tema not in temas.keys():
        tema = input("Digite um número válido: ")
    return tema

# Função para escolher uma palavra dentro do tema escolhido
def escolher_palavra(tema):
    palavra = random.choice(temas[tema][1:])
    return palavra

# Função principal do jogo
def jogo_da_forca():
    tema_escolhido = escolher_tema()
    palavra = escolher_palavra(tema_escolhido)
    palavra = palavra.upper()
    letras_erradas = []
    letras_certas = []
    tentativas = 6
    
    print("Começou o jogo da forca!")
    print("Tema: " + temas[tema_escolhido][0])
        
    while True:
        print("\nPalavra:")
        for letra in palavra:
            if letra in letras_certas:
                print(letra + " ", end="")
            else:
                print("_ ", end="")
        
        print("\nTentativas restantes: " + str(tentativas))
        
        if tentativas == 0:
            print("\nVocê perdeu! A palavra correta era: " + palavra)
            break
        
        if set(palavra) == set(letras_certas):
            print("\nParabéns! Você acertou a palavra: " + palavra)
            break
        
        tentativa = input("Digite uma letra: ").upper()
        
        if tentativa in letras_erradas or tentativa in letras_certas:
            print("Essa letra já foi escolhida. Tente outra.")
            continue
        
        if tentativa in palavra:
            letras_certas.append(tentativa)
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1
        
        print("Letras erradas: " + ", ".join(letras_erradas))

# Executa o jogo
jogo_da_forca()