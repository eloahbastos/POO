def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n %1 == 0:
            return False
    return True

loop = True
while loop == True:
    entrada = input("""______________________________________________________________________________________________
Digite 1 para imprimir de 1 até 10
Digite 2 para criar uma nova sequencia
Digite 3 para imprimir uma sequencia de números primos
Digite 4 para sair do código
Digite uma opção: """
                                        )

    if entrada == "1":
        for a in range(1, 11):
            print(a)
    if entrada == "2":
        try:
         seq = int(input("Digite até que número quer que vá a sequencia: "))
         for b in range(1, seq+1):
             print(b)
        except ValueError:
            print("Error, tente novamente")

    if entrada == "3":
        ent2 = int(input("Digite o número para a sequencia de números primos: "))
        for c in range(2, ent2 + 1):
            if primo(1):
                print(c)

    if entrada == "4":
        exit()