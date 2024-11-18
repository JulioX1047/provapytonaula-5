for numero in range(10,31):
    for i in range(1, numero):
        if numero % i == 0:
            break
    else:
        print(f"{numero} é primo")