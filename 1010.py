codigo_peca1, num_peca1, valor_unitario1 = map(float, input().split())
codigo_peca2, num_peca2, valor_unitario2 = map(float, input().split())

total_a_pagar = (num_peca1 * valor_unitario1) + (num_peca2 * valor_unitario2)

print("VALOR A PAGAR: R$ %.2f" %total_a_pagar)