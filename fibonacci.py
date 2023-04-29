n = int(input("Digite um número: "))
anterior = 0
atual = 1
contador = 1

print(anterior,end=" ")
while contador <= n:
    print(atual,end =" ")
    
    proximo = atual + anterior
    anterior = atual
    atual = proximo

    contador = contador + 1
