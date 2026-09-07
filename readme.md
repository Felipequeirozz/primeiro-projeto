Calculadora de Consumo de Energia e Custos

Este projeto tem como objetivo calcular o consumo mensal de energia elétrica de eletrodomésticos e estimar o custo mensal de acordo com o tempo de utilização.

Fórmulas utilizadas

Para realizar os cálculos, o sistema utiliza as seguintes fórmulas:

Consumo mensal
consumo_mensal = (potencia * uso_diario * 30) / 1000

O resultado é apresentado em kWh (quilowatt-hora).

Custo mensal
custo = consumo_mensal * 0.75

O valor de R$ 0,75 por kWh é utilizado como referência para estimar o custo mensal.

Linguagem utilizada

O projeto foi desenvolvido utilizando a linguagem Python.




Como executar
1. Instale o Python

Certifique-se de que o Python esteja instalado em seu computador.

Para verificar, abra o terminal e execute:

python --version
2. Acesse a pasta do projeto

Abra o terminal na pasta onde o projeto foi salvo.

3. Execute o programa

Execute o arquivo app.py utilizando o comando:

python app.py
4. Insira os dados

Após iniciar o programa, informe os dados solicitados, como a potência do eletrodoméstico e o tempo médio de utilização diária.

5. Confira os resultados

Após inserir os dados, o sistema realizará automaticamente os cálculos e apresentará:

Consumo mensal em kWh
Custo estimado por mês

Pronto! Agora você pode consultar o consumo e o custo mensal estimado do eletrodoméstico.