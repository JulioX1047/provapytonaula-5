primo=0;
for numero in range(10,31):
  if numero % 1 == 0:
    primo=1
    for i in range(2, numero):
        if numero % i == 0:
           primo=0;
           break
    if primo==1:
        print(f"{numero} é primo")