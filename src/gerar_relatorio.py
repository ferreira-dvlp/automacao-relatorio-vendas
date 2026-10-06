import pandas as pd
import numpy as np
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ARQUIVO_ENTRADA = BASE / "dados" / "vendas.xlsx"
ARQUIVO_SAIDA = BASE / "relatorios" / "relatorio_vendas.xlsx"

df = pd.read_excel(ARQUIVO_ENTRADA)

df.columns = df.columns.str.strip().str.lower()
for col in ["produto", "categoria", "vendedor", "regiao"]:
    df[col] = df[col].astype("string").str.strip()

df["data"] = pd.to_datetime(df["data"], errors="coerce")
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors="coerce")
df["desconto"] = pd.to_numeric(df["desconto"], errors="coerce")

df = df.dropna(subset=["data", "produto", "quantidade", "preco_unitario", "desconto"])

df = df[df["quantidade"] > 0]
df = df[df["preco_unitario"] >= 0]
df["desconto"] = df["desconto"].clip(0, 1)

df["valor_total"] = np.round(
    df["quantidade"] * df["preco_unitario"] * (1 - df["desconto"]), 2
)
df["mes"] = df["data"].dt.to_period("M").astype(str)

faturamento = df["valor_total"].sum()
qtd_vendas = df["id_venda"].nunique()
unidades = df["quantidade"].sum()
ticket_medio = faturamento / qtd_vendas if qtd_vendas else 0

resumo = pd.DataFrame({
    "Indicador": ["Faturamento total", "Quantidade de vendas", "Unidades vendidas", "Ticket médio"],
    "Valor": [faturamento, qtd_vendas, unidades, ticket_medio]
})

por_categoria = df.groupby("categoria", as_index=False).agg(
    vendas=("id_venda","nunique"),
    unidades=("quantidade","sum"),
    faturamento=("valor_total","sum")
).sort_values("faturamento", ascending=False)

por_produto = df.groupby("produto", as_index=False).agg(
    vendas=("id_venda","nunique"),
    unidades=("quantidade","sum"),
    faturamento=("valor_total","sum")
).sort_values("faturamento", ascending=False)

por_vendedor = df.groupby("vendedor", as_index=False).agg(
    vendas=("id_venda","nunique"),
    unidades=("quantidade","sum"),
    faturamento=("valor_total","sum")
).sort_values("faturamento", ascending=False)

por_regiao = df.groupby("regiao", as_index=False).agg(
    vendas=("id_venda","nunique"),
    unidades=("quantidade","sum"),
    faturamento=("valor_total","sum")
).sort_values("faturamento", ascending=False)

por_mes = df.groupby("mes", as_index=False).agg(
    vendas=("id_venda","nunique"),
    unidades=("quantidade","sum"),
    faturamento=("valor_total","sum")
).sort_values("mes")

qualidade = pd.DataFrame({
    "Metrica": ["Linhas originais", "Linhas após limpeza", "Linhas removidas",
                "Nulos após limpeza", "IDs duplicados após limpeza"],
    "Valor": [len(pd.read_excel(ARQUIVO_ENTRADA)), len(df),
              len(pd.read_excel(ARQUIVO_ENTRADA)) - len(df),
              int(df.isna().sum().sum()), int(df["id_venda"].duplicated().sum())]
})

ARQUIVO_SAIDA.parent.mkdir(exist_ok=True)
with pd.ExcelWriter(ARQUIVO_SAIDA, engine="openpyxl") as writer:
    resumo.to_excel(writer, sheet_name="Resumo", index=False)
    por_categoria.to_excel(writer, sheet_name="Por Categoria", index=False)
    por_produto.to_excel(writer, sheet_name="Por Produto", index=False)
    por_vendedor.to_excel(writer, sheet_name="Por Vendedor", index=False)
    por_regiao.to_excel(writer, sheet_name="Por Regiao", index=False)
    por_mes.to_excel(writer, sheet_name="Por Mes", index=False)
    qualidade.to_excel(writer, sheet_name="Qualidade", index=False)
    df.to_excel(writer, sheet_name="Dados Tratados", index=False)

print(f"Relatório gerado em: {ARQUIVO_SAIDA}")
