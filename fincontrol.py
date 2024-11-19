import requests
from tkinter import *

# Script para cálculo de dívidas (Saídas - Entradas - POSITIVO/NEGATIVO)

# DISPOSIÇÕES
# Receber o valor das dívidas e somá-lo
# Receber o valor de entradas e somá-lo
# Retornar o quanto se deve ou sobra

def get_float_values(prompt):
    while True:
        try:
            # Solicita os valores e converte em uma lista de floats
            values = input(prompt).replace(',', '.').split()
            return [float(value) for value in values]
        except ValueError:
            print("Erro: Insira apenas números válidos, separados por espaço.")
            
# Calcula as dívidas
def billSum():
    values = get_float_values("Digite os valores das suas dívidas (separados por espaço): ")
    billsArraySum = sum(values)
    print("A soma da sua dívida é:", billsArraySum)
    return billsArraySum


# Calcula as entradas
def cashInSum():
    values = get_float_values("Digite os valores das entradas (separados por espaço): ")
    cashInflowArraySum = sum(values)
    print("O valor total de entrada em sua conta é:", cashInflowArraySum)
    return cashInflowArraySum


# Calcula se o saldo é positivo ou negativo
def finalBalanceSum(cashInflowArraySum, billsArraySum):
    # Realiza a conta utilizando o array de entradas e o de saídas
    finalBalance = cashInflowArraySum - billsArraySum
    if finalBalance > 0:
        print(f"Você está positivado (em R$): {finalBalance}")
    else:
        print(f"Você está negativado (em R$): {finalBalance}")
        
        
# ===================================== INTEGRAÇÃO COM A INTERFACE DA BIBLIOTECA TKINTER ======================================================= #
        
def calculate_balance():
    try:
        bills = bills_entry.get()
        cash_in = cash_in_entry.get()

# Convertendo os valores em floats
        bills_sum = sum(float(v.replace(',', '.')) for v in bills.split())
        cash_in_sum = sum(float(v.replace(',', '.')) for v in cash_in.split())

        final_balance = cash_in_sum - bills_sum
        if final_balance > 0:
            result_label.config(text=f"Você está positivado: R$ {final_balance:.2f}")
        else:
            result_label.config(text=f"Você está negativado: R$ {final_balance:.2f}")
    except ValueError:
        result_label.config(text="Erro: Insira apenas números válidos.")



# Função principal para rodar o código
def main():
    bills = billSum()
    cashInflow = cashInSum()
    finalBalanceSum(cashInflow, bills)


# Criando a interface com tkinter
window = Tk()
window.title("Calculadora de Dívidas e Entradas")

# Rótulos e campos de entrada
Label(window, text="Digite suas dívidas (separadas por espaço):").pack(pady=5)
bills_entry = Entry(window, width=40)
bills_entry.pack(pady=5)

Label(window, text="Digite suas entradas (separadas por espaço):").pack(pady=5)
cash_in_entry = Entry(window, width=40)
cash_in_entry.pack(pady=5)

# Botão de cálculo
calculate_button = Button(window, text="Calcular", command=calculate_balance)
calculate_button.pack(pady=10)

# Rótulo para exibir o resultado
result_label = Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Inicia a interface
window.mainloop()
