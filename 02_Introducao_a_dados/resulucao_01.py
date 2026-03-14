# Lê a linha de entrada e separa os valores
entrada = input().strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

# TODO: Calcule o valor final do pedido após aplicar o desconto percentual
# Calculamos o valor do desconto primeiro
valor_do_desconto = valor_total * (percentual_desconto / 100)

# Subtraímos do valor total para ter o preço final
valor_final = valor_total - valor_do_desconto

# Imprima o valor final com duas casas decimais
print(f"{valor_final:.2f}")