import pandas as pd

from pipeline import (
    transformar_dados,
    gerar_resumo
)


# =====================================================
# TESTE 1
# Cálculo do faturamento
# =====================================================

def test_calculo_faturamento():

    dados = {
        "id_cliente": [1],
        "produto": ["Notebook"],
        "quantidade": [2],
        "valor_unitario": [100]
    }

    df = pd.DataFrame(dados)

    resultado = transformar_dados(df)

    assert (
        resultado.iloc[0]["faturamento"]
        == 200
    )


# =====================================================
# TESTE 2
# Quantidade negativa
# =====================================================

def test_quantidade_negativa():

    dados = {
        "id_cliente": [1],
        "produto": ["Notebook"],
        "quantidade": [-2],
        "valor_unitario": [100]
    }

    df = pd.DataFrame(dados)

    resultado = transformar_dados(df)

    assert len(resultado) == 0


# =====================================================
# TESTE 3
# Cliente nulo
# =====================================================

def test_cliente_nulo():

    dados = {
        "id_cliente": [None],
        "produto": ["Notebook"],
        "quantidade": [2],
        "valor_unitario": [100]
    }

    df = pd.DataFrame(dados)

    resultado = transformar_dados(df)

    assert len(resultado) == 0


# =====================================================
# TESTE 4
# Agregação por produto
# =====================================================

def test_resumo_produto():

    dados = {
        "produto": [
            "Mouse",
            "Mouse"
        ],
        "faturamento": [
            100,
            200
        ]
    }

    df = pd.DataFrame(dados)

    resultado = gerar_resumo(df)

    assert (
        resultado.iloc[0]["faturamento"]
        == 300
    )
    