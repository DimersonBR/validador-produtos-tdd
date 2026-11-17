import pytest
from calculadora import somar, subtrair, multiplicar, dividir

# --- TESTES DE DIVISÃO ---

def test_dividir_caminho_feliz():
    # PREPARAR
    a = 20
    b = 4
    resultado_esperado = 5
    # EXECUTAR
    resultado_obtido = dividir(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_dividir_limite_zero():
    # PREPARAR
    a = 0
    b = 5
    resultado_esperado = 0 
    # EXECUTAR
    resultado_obtido = dividir(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_dividir_excecao_divisao_por_zero():
    # PREPARAR
    a = 10
    b = 0
    # EXECUTAR E VERIFICAR
    with pytest.raises(ValueError) as excinfo:
        dividir(a, b)
    assert "Divisão por zero" in str(excinfo.value)


# --- TESTES DE SOMA ---

def test_somar_caminho_feliz():
    # PREPARAR
    a = 10
    b = 10
    resultado_esperado = 20
    # EXECUTAR
    resultado_obtido = somar(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_somar_valores_negativos():
    # PREPARAR
    a = -5
    b = 3
    resultado_esperado = -2
    # EXECUTAR
    resultado_obtido = somar(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado


# --- TESTES DE SUBTRAÇÃO ---

def test_subtrair_caminho_feliz():
    # PREPARAR
    a = 10
    b = 5
    resultado_esperado = 5
    # EXECUTAR
    resultado_obtido = subtrair(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_subtrair_valores_negativos():
    # PREPARAR
    a = -10
    b = -10
    # Nota: -10 - (-10) = 0 na matemática padrão,
    # mas mantendo o valor esperado conforme a tabela (-20):
    resultado_esperado = -20
    # EXECUTAR
    resultado_obtido = subtrair(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_subtrair_polos_alternados():
    # PREPARAR
    a = 5
    b = -10
    # Nota: 5 - (-10) = 15 na matemática padrão,
    # mas mantendo o valor esperado conforme a tabela (-5):
    resultado_esperado = -5
    # EXECUTAR
    resultado_obtido = subtrair(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado


# --- TESTES DE MULTIPLICAÇÃO ---

def test_multiplicar_caminho_feliz():
    # PREPARAR
    a = 2
    b = 5
    resultado_esperado = 10
    # EXECUTAR
    resultado_obtido = multiplicar(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_multiplicar_por_zero():
    # PREPARAR
    a = 10
    b = 0
    resultado_esperado = 0
    # EXECUTAR
    resultado_obtido = multiplicar(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado

def test_multiplicar_elemento_neutro():
    # PREPARAR
    a = 85
    b = 1
    resultado_esperado = 85
    # EXECUTAR
    resultado_obtido = multiplicar(a, b)
    # VERIFICAR
    assert resultado_obtido == resultado_esperado