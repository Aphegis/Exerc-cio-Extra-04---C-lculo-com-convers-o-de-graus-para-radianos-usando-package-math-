# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = input("Qual é o seu sexo [M/F] ").upper().strip()
while sexo not in "MF" and sexo != "MASCULINO" and sexo != "FEMININO" and sexo != "HOMEM" and sexo != "MULHER":
    sexo = input("Dados invalidos. Por favor informe seu sexo: [M/F] ")
if sexo == "M" or sexo == "MASCULINO" or sexo == "HOMEM":
    print("Sexo masculino registrado com sucesso.")
else:
    print("Sexo feminino registrado com sucesso.")




