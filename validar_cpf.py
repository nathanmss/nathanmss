print('---------------- Validação de CPF ----------------')

cpf = input('Informe seu CPF, apenas os números: ')
lista_cpf = []

for element in cpf:
    lista_cpf.append(int(element))
print(f'Seu CPF: {lista_cpf}')

# ----------------------- VERIFICAÇÃO PRIMEIRO DIGITO--------------------------- #
verificar_1_digito = [10, 9, 8, 7, 6, 5, 4, 3, 2]
nove_primeiros = lista_cpf[0:9]

lista_multiplicada = [x*y for x, y in zip(nove_primeiros, verificar_1_digito)] # gerando lista com a multiplicação entre os nove primeiros e de 10 a 2.
lista_somada = sum(lista_multiplicada) * 10  # soma de todos os indices da lista multiplicada, multipl. 10.

if lista_somada % 11 == lista_cpf[9]:
    print(f'Primeiro digito do seu CPF: {lista_cpf[9]}\nO primeiro digito do seu CPF foi verificado e é valido. ')
else:
    print('Seu CPF é invalido.')

# ----------------------- VERIFICAÇÃO SEGUNDO DIGITO--------------------------- #
verificar_2_digito = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
dez_primeiros = lista_cpf[0:10]

lista_multiplicada_2 = [x*y for x, y in zip(dez_primeiros, verificar_2_digito)]
lista_somada_2 = sum(lista_multiplicada_2) * 10

if lista_somada_2 % 11 == lista_cpf[10]:
    print(f'Segundo digito do seu CPF: {lista_cpf[10]}\nO segundo digito do seu CPF foi verificado e é valido.\nSeu CPF é válido.')
else:
    print('Seu CPF é invalido.')