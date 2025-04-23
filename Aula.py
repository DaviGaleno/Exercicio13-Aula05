sal = float(input("digite seu salario: "))

if sal <= 2000:
    print('insento de imposto')

elif 2000 < sal <= 3500:
    imp = sal * 0.10
    print(f'O imposto é R$ {imp}')

elif sal > 3500:
    imp = sal * 0.15
    print(f'O imposto é R$ {imp}')

else:
    print('o valor é invalido')
