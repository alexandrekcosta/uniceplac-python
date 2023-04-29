opcao = 'n'

while opcao != 's':
    print("############# Digite uma das opções abaixo #################\n")
    print("+ para soma\n")
    print("- para subtração \n")
    print("* para multiplicação\n")
    print("/ para divisão\n")
    print("s para sair do programa \n")
    opcao = input("Digite a opção desejada: \n")
    if opcao == 's':

        print("Volte sempre!")
        break

    elif opcao !='+' and  opcao !='-' and opcao  !='*'  and opcao !='/':

        print("Opção invalida")
        
        continue

    numero1 = int(input("Digite um número:\n"))
    numero2 = int(input("Digite outro número:\n"))

    if opcao == '+':
        
        soma = numero1 + numero2
        print("A soma dos valores = \n",soma)
        
    elif opcao == '-':

        subtracao = numero1 - numero2
        print("A subtração dos valores = \n",subtracao)

    elif opcao == '*':


        multiplicacao = numero1 * numero2
        print("A multiplicação dos valores = \n",multiplicacao)

    elif opcao == '/':
        division = numero1 / numero2
        print("A divisão dos valores = \n",division)

