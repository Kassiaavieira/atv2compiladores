
def int_to_string(texto):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
                'q', 'r', 's', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for caractere_atual in list(texto):
        numero = caractere_atual in alfabeto
        if numero:
            return False
    return True, int(texto)


# Versão 02
print(int_to_string("abc123"))
print(int_to_string("123"))
print(int_to_string("010"))
