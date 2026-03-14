# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# Lógica de decisão baseada nas regras do enunciado:
if valor <= 1000 and (prioridade == "alta" or prioridade == "media"):
    print("aprovado")
elif valor > 1000 and prioridade == "alta":
    print("revisao")
else:
    # Caso não se encaixe nas regras acima (como prioridade baixa ou valor alto com média/baixa)
    print("rejeitado")