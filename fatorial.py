n = int(input("Digite um número:"))

fatorial = 1

for i in range(n,1,-1):
    fatorial = fatorial * i
    print("O fatorial do número digitado = ",fatorial)
    
