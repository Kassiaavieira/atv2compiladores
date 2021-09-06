def fraselista():
    frase = input("Digite uma frase: ")
    lista = []
    controle = ''
    for caractere_atual in list(frase):

        if caractere_atual == 'o':
            caractere_atual = caractere_atual + 's'

        controle = str(controle) + str(caractere_atual)

    lista.append(controle)
    return lista

print(fraselista())