def fraselista():
    frase = input("Digite uma frase: ")
    lista = []
    controle = ''
    for caractere_atual in list(frase):

        if caractere_atual == 'a':
            caractere_atual = 'o'

        controle = str(controle) + str(caractere_atual)

    lista.append(controle)
    return lista

print(fraselista())