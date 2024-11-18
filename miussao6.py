for numero in range(10,31):
    for i in range(10, numero):
        if numero % i == 0:
            break
    else:
        print(f"{numero} é primo")
