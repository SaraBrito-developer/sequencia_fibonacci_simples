sequencia = int(input("Quantos numero Fibonacci você deseja? "))
contagem = 0
num1, num2 = 0, 1

if sequencia <= 0:
   print("você precisa digitar um numero maior que 0")

elif sequencia == 1:
    print("sequencia numerica fibonacci",sequencia,":")
    print(num1)

else:
    print("A sequencia Fibonacci requisitada foi:")

    while contagem < sequencia:
        print(num1)
        soma = num1 + num2
        num1 = num2
        num2 = soma
        contagem += 1



      