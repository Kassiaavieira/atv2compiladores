def fraselista():
    frase = input("Digite uma frase: ")
    lista = []
    controle = ''
    for caractere_atual in list(frase):
        if caractere_atual == ' ':
            lista.append(controle)
            controle = ''
            caractere_atual = ''
        controle = str(controle) + str(caractere_atual)
    lista.append(controle)


    return lista

print(fraselista())