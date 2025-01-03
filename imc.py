altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em quilogramas): "))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Seu IMC é igual a baixo peso")
elif 18.5 < imc <= 24.9:
    print("Seu IMC é igual a peso adequado")
elif 24.9 < imc <= 29.9:
    print("Seu IMC é igual a sobrepeso")
elif 29.9 < imc <= 34.9:
    print("Seu IMC é igual a obesidade grau I")
elif 34.9 < imc <= 39.9:
    print("Seu IMC é igual a obesidade grau II")
else:
    print("Seu IMC é igual a obesidade grau III")
