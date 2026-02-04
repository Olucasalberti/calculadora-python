while True:

    print('Vamos começar o calculo! Para começar escolha umas das operações a seguir:')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')

    operacao = int(input('Escolha a operação:'))

    num1 = int(input('insira o primeiro valor:'))
    num2 = int(input('insira o segundo valor:'))

    if operacao == 1:
        print('A soma de seus valores é:', num1 + num2)

    elif operacao == 2:
        print('A subtração de seus valores é:', num1 - num2)

    elif operacao == 3:
        print('A multiplicação de seus valores é:', num1 * num2)

    elif operacao == 4:
        if num2 == 0:
            print('Não é possivel dividir por zero')
        else:
            print('A divisão de seus valores é:', num1 / num2)

    else:
        print('Operação invalida!')
