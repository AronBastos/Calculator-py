def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

def calculadora():
    print("Opções de operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. multiplicacão")
    print("4. Divisão")

    escolha = input("Escolha uma operação (1/2/3/4): ")

    if escolha not in ('1', '2', '3', '4'):
        print("Opção inválida")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", soma(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))

if __name__ == "__main__":
    calculadora()
    
