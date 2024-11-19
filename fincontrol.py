# Script para cálculo de dívidas (Saídas - Entradas - POSITIVO/NEGATIVO)

# DISPOSIÇÕES
# Receber o valor das dívidas e somá-lo
# Receber o valor de entradas e somá-lo
# Retornar o quanto se deve ou sobra


# Calcula as dívidas
def billSum():
    # Input que vai receber o valor das dívidas
    bills = input("Digite os valores das suas dívidas (separados por espaço): ")
    print("Dívidas informadas:", bills)

    values = []  # Array vazio que receberá os valores informados no input

    for value in bills.split():  # Loop que pega o número adicionado no input bills e transforma ele em valor
        while True:  # Loop que verifica se o valor atribuído consiste em um número
            value = value.replace(',', '.')  # Substitui a vírgula por ponto
            try:
                # Caso consista, insere no array (utilizando float para que possam ter números quebrados)
                values.append(float(value))
                break
            except ValueError:  # Caso ocorra um erro de valor
                value = input(f"'{value}' não é um número válido. Insira novamente:")

    billsArraySum = sum(values)  # Soma os valores do array values
    print("A soma da sua dívida é:", billsArraySum)
    return billsArraySum


# Calcula as entradas
def cashInSum():
    cashInflow = input("Digite os valores das entradas (separados por espaço): ")  # Input que vai receber o valor das entradas
    print("Entradas informadas:", cashInflow)

    values = []  # Array vazio que receberá os valores informados no input

    for value in cashInflow.split():  # Loop que pega o número adicionado no input cashInflow e transforma ele em valor
        while True:  # Loop que verifica se o valor atribuído consiste em um número
            value = value.replace(',', '.')  # Substitui a vírgula por ponto
            try:
                # Caso consista, insere no array (utilizando float para que possam ter números quebrados)
                values.append(float(value))
                break
            except ValueError:  # Caso ocorra um erro de valor
                value = input(f"'{value}' não é um número válido. Insira novamente:")

    cashInflowArraySum = sum(values)  # Soma os valores do array values
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


# Função principal para rodar o código
def main():
    bills = billSum()
    cashInflow = cashInSum()
    finalBalanceSum(cashInflow, bills)


# Executa a função principal
if __name__ == "__main__":
    main()
