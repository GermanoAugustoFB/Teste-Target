import json

with open('dados.json') as f:
    dados = json.load(f)

faturamento_diario = [dia['valor'] for dia in dados]

menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

dias_com_faturamento = [f for f in faturamento_diario if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_mensal)

print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)

