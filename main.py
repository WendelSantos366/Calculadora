import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.), a função retornará nan, 
    sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")
    
    if operador == '+':
        result = num1 + num2

    elif operador == '-':
        result = num1 - num2
        
    elif operador == '*':
        result = num1 * num2
        
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
                 raise ZeroDivisionError ("Impossível dividir por zero")
        
    elif operador == '**':
        result = num1 ** num2
        
    return result 

def menu_operacoes():
    print("Escolha a operação desejada: ")
    print(" (+) para somar ")
    print(" (-) para subtrair")
    print(" (*) para multiplicar ")
    print(" (**) para obter a exponenciação")
    
    

if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora em Python')
            menu_operacoes()
            operador = input("Digite o operador: ").strip()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float (input("Digite o segundo número: "))
            
            resultado = calculadora (num1, num2, operador)
            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")


        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            
            
            
        continuar = input("Deseja fazer outra operação? (s/n): ").strip().lower()
        if continuar != 's':
         print('\nVolte Sempre!\n')
         break
            
            
