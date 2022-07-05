nome = str(input('Digite o seu nome: '))
while True:
    try:
        nasc = int(input('Digite o ano do seu nascimento: '))
        atual = 2022
        idade = atual - nasc
    except(ValueError):
        print('Você deve digitar 4 números para o nascimento!')
        continue
    if (nasc < 1922):
        print('Digite uma data maior que 1921')
        continue
    elif (nasc > 2021):
        print('Digite uma data menor que 2022')     
        continue
    else:    
        print(nome,'sua idade em 2022 é:',idade)
    break