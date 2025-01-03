altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = altura * altura / peso

if imc <= 18.5 :
    print("Seu IMC é igual a baixo peso")
if imc >= 18.5:
    print("Seu IMC é igual a peso adequado")
if imc >= 24.9:
    print("Seu IMC é igual a sobrepeso")
if imc >= 29.9:
    print("Seu IMC é igual a obesidade grau I")
if imc >= 34.9:
    print("Seu IMC é igual a obesidade grau II")
if imc >= 39.9:  
    print("Seu IMC é igual a obesidade grau III")
else:
    print("Encerrando programa")
    

