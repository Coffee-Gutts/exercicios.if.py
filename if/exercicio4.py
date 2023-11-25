salario=int(input("Digite o seu salário:"))

conta1= salario + (15 * salario) / 100
conta2= salario + (10 * salario) / 100
conta3= salario + (5 * salario) / 100

if salario < 500:
    print("O seu salário foi aumentado em 15%, seu novo salário é:", conta1)
if salario > 500 and salario <=  1000:
    print("O seu salário foi aumentado em 10%, seu novo salário é:", conta2)
if salario > 1000:
    print("O seu salário foi aumentado em 5%, seu novo salário é:", conta3)


  