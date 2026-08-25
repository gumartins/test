import pandas as pd


# =====================================================
# EXTRAÇÃO
# =====================================================

def carregar_dados(caminho):
    """
    Carrega os dados de um arquivo CSV.
    """

    df = pd.read_csv(caminho)

    return df


# =====================================================
# TRANSFORMAÇÃO
# =====================================================

def transformar_dados(df):
    """
    Realiza as regras de tratamento dos dados.
    """

    # Criamos uma cópia para evitar alterações
    # inesperadas no DataFrame original
    df = df.copy()

    # Remove registros onde o cliente está vazio
    df = df.dropna(
        subset=["id_cliente"]
    )

    # Mantém somente quantidades maiores que zero
    df = df[
        df["quantidade"] > 0
    ]

    # Mantém somente valores positivos
    df = df[
        df["valor_unitario"] > 0
    ]

    # Calcula o faturamento da venda
    df["faturamento"] = (
        df["quantidade"]
        * df["valor_unitario"]
    )

    return df


# =====================================================
# AGREGAÇÃO
# =====================================================

def gerar_resumo(df):
    """
    Calcula o faturamento total por produto.
    """

    resumo = (
        df
        .groupby("produto")["faturamento"]
        .sum()
        .reset_index()
    )

    return resumo


# =====================================================
# EXECUÇÃO DO PIPELINE
# =====================================================

if __name__ == "__main__":

    # Extrai
    df = carregar_dados(
        "data/vendas.csv"
    )

    # Transforma
    df = transformar_dados(df)

    # Agrega
    resumo = gerar_resumo(df)

    # Exibe resultado
    print(resumo)

    # Salva resultado
    resumo.to_csv(
        "data/resultado.csv",
        index=False
    )