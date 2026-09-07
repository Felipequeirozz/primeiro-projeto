# calculando o consumo de energia
#Autor: Felipe Queiroz

# entrada de dados
print("Olá, seja bem-vindo!")
Eletrodoméstico = input("Digite o nome do eletrodoméstico que você deseja consultar: ")
potência = input("Digite a potência do eletrodoméstico em W(Watts): ")
Uso_diário = input("Digite o tempo médio de uso diário em horas: ")

# processamento de dados
consumo_diário = (float(potência) * float(Uso_diário)* 30) / 1000
custo = consumo_diário * 0.75

# saída de dados
print(f"O consumo mensal do {Eletrodoméstico} é de {consumo_diário:.2f} kWh.")
print(f"O custo mensal do {Eletrodoméstico} é de R$ {custo:.2f}.")