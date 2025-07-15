# Equação Climática 

## Sobre
Essa Branch do projeto trata a respeito das predições das concentrações de gás carbônico na atmosfera a partir do Acordo de Paris. 

## Configuração

### Requisitos
Precisa ter o `python` com o pacote `venv` instalado. Além disso é preciso instalar o `pip`.

### Setup
Primeiro, crie o ambiente virtual:

```sh
python -m venv venv
```

Depois, entre no ambiente virtual:

```sh
source venv/bin/activate
```

Em seguida, instale as dependências usando o `pip`

```sh
pip install -r requirements.txt
```

## Executando

Tenha um arquivo de dados no formato `.csv`. Seu arquivo deve possuir duas colunas.
A primeira linha do arquivo será ignorada, recomenda-se que você use essa linha para documentar
o que representa cada coluna.

Abaixo se encontra um exemplo de como seu arquivo deve estar formatado:

```
x,y
1,2
3,4
5,6
```

Tendo o arquivo, basta executar:

```sh
python src/main_{metodo_de_ajuste}.py data/co2_de_seasoned_since_paris_agreement.csv
```
Esse comando gera um gráfico com o ajuste feito pelo método e a predição até 2035, dois arquivos `.csv`, um com o ajuste de 2016 a 2025, baseado na base de dados, outro com as previsões de 2025 a 2035. Os métodos disponível são `linear, geométrico, exponencial, logarítmico, potencial, quadrático`.

### Exemplo
Usando o arquivo `data/example.csv` deve-se obter este resultado ao executar o script:

<div align="center">
    <img src="./docs//images/example.csv.png"/>
</div>

### Medição do R2
Para avaliar o método a partir do cálculo do R2, basta executar o seguinte comando:

```sh
python src/main_r2.py data/co2_de_seasoned_since_paris_agreement.csv r2_comparation_paris_agreement/ajuste_2016_2025_{metodo_de_ajuste}.csv
```

Esse comando irá gerar o(s) valor(s) da medição do R2, que está disponível no arquivo r2_resultado.txt.