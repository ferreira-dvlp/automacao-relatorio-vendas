# 📊 Automação de Relatórios de Vendas

Projeto desenvolvido em **Python** para automatizar a análise de dados de vendas e a geração de informações relevantes para acompanhamento da performance comercial.

A proposta é transformar uma base de vendas em análises organizadas, permitindo identificar padrões de faturamento, desempenho de produtos, categorias, vendedores e regiões.

## 🎯 Objetivo

Automatizar etapas comuns de análise de vendas, reduzindo a necessidade de cálculos manuais e facilitando a interpretação dos dados para apoiar a tomada de decisões.

O projeto utiliza **Python e Pandas** para tratamento e análise dos dados, além de recursos de visualização e exportação para facilitar a apresentação dos resultados.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Pandas** — manipulação e análise dos dados
* **NumPy** — operações numéricas
* **Matplotlib** — criação de gráficos
* **Jupyter Notebook** — desenvolvimento e análise
* **Excel** — organização e exportação dos resultados
* **Git/GitHub** — versionamento do projeto

## 📁 Base de dados

A base utilizada contém **5.000 registros de vendas**, com as seguintes informações:

| Coluna           | Descrição                    |
| ---------------- | ---------------------------- |
| `id_venda`       | Identificador da venda       |
| `data`           | Data da venda                |
| `produto`        | Produto vendido              |
| `categoria`      | Categoria do produto         |
| `quantidade`     | Quantidade de itens vendidos |
| `preco_unitario` | Preço unitário do produto    |
| `desconto`       | Desconto aplicado            |
| `valor_total`    | Valor total da venda         |
| `vendedor`       | Responsável pela venda       |
| `regiao`         | Região da venda              |

### Categorias presentes

* Periféricos
* Informática
* Telefonia
* Impressão
* Armazenamento

## ⚙️ Etapas do projeto

O processo de análise é dividido em algumas etapas principais:

### 1. Carregamento dos dados

A base de vendas é importada para o ambiente Python utilizando o Pandas.

### 2. Tratamento dos dados

São realizadas verificações para identificar possíveis problemas na base, como:

* Valores ausentes
* Dados duplicados
* Tipos de dados incorretos
* Inconsistências nos valores
* Necessidade de conversão de colunas

### 3. Análise exploratória

São analisados indicadores e características da base, como:

* Quantidade de vendas
* Faturamento
* Produtos mais vendidos
* Categorias com maior volume de vendas
* Desempenho dos vendedores
* Desempenho por região
* Quantidade de produtos vendidos
* Valores médios das vendas

### 4. Visualização dos dados

Os resultados são apresentados por meio de gráficos utilizando **Matplotlib**, facilitando a identificação de padrões e diferenças entre os dados.

### 5. Geração dos resultados

As informações obtidas durante a análise podem ser organizadas e exportadas para utilização em relatórios no **Excel**.

## 📈 Alguns resultados da base

A base possui:

* **5.000 vendas analisadas**
* **R$ 16.560.800,50** em valor total de vendas
* Valor médio por venda de aproximadamente **R$ 3.312,16**

Distribuição das vendas por categoria:

| Categoria     | Quantidade |
| ------------- | ---------: |
| Periféricos   |      1.937 |
| Informática   |      1.016 |
| Telefonia     |      1.009 |
| Impressão     |        534 |
| Armazenamento |        504 |

A categoria **Periféricos** apresenta o maior número de registros na base, representando uma parcela significativa das vendas analisadas.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### 2. Acesse a pasta do projeto

```bash
cd automacao-relatorios-vendas
```

### 3. Instale as dependências

```bash
pip install pandas numpy matplotlib openpyxl jupyter
```

### 4. Execute o Jupyter Notebook

```bash
jupyter notebook
```

Depois, abra o arquivo `.ipynb` do projeto e execute as células em sequência.

## 📂 Estrutura do projeto

```text
automacao-relatorios-vendas/
│
├── dados/
│   └── vendas.csv
│
├── relatorios/
│   └── relatorio_vendas.xlsx
│
├── notebooks/
│   └── automacao_relatorios_vendas.ipynb
│
├── README.md
```

> A estrutura pode variar de acordo com a organização final dos arquivos no repositório.

## 👨‍💻 Autor

**Cauan Ferreira**

Estudante de **Análise e Desenvolvimento de Sistemas — FATEC**.

Projeto desenvolvido com foco no desenvolvimento de habilidades em **Python, análise de dados, automação de processos e geração de relatórios**.
