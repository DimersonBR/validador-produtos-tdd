from validar_produto import cadastrar_produtos
def test_menos_de_3_fotos_deve_retornar_False():
    # Arrange
    fotos = ["foto1.jpg", "foto2.jpg"]
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        fotos, 10, 150.00, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_foto_vazia_deve_retornar_False():
    # Arrange
    fotos = ["foto1.jpg", "foto2.jpg", ""]
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        fotos, 10, 150.00, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_estoque_negativo_deve_retornar_False():
    # Arrange
    estoque = -1
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        estoque, 150.00, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_valor_ausente_deve_retornar_False():
    # Arrange
    valor = None
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, valor, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_valor_vazio_deve_retornar_False():
    # Arrange
    valor = ""
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, valor, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_valor_negativo_deve_retornar_False():
    # Arrange
    valor = -0.01
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, valor, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_descricao_ausente_deve_retornar_False():
    # Arrange
    descricao = None
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, 150.00, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_descricao_vazia_deve_retornar_False():
    # Arrange
    descricao = ""
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, 150.00, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_descricao_apenas_espacos_deve_retornar_False():
    # Arrange
    descricao = "   "
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, 150.00, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_descricao_com_256_caracteres_deve_retornar_False():
    # Arrange
    descricao = "a" * 256
    resultado_esperado = False

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, 150.00, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_descricao_com_255_caracteres_deve_retornar_True():
    # Arrange
    descricao = "a" * 255
    resultado_esperado = True

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        10, 150.00, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_estoque_e_valor_zero_deve_retornar_True():
    # Arrange
    estoque = 0
    valor = 0
    resultado_esperado = True

    # Act
    resultado_obtido = cadastrar_produtos(
        ["foto1.jpg", "foto2.jpg", "foto3.jpg"],
        estoque, valor, "Armação de óculos."
    )

    # Assert
    assert resultado_obtido == resultado_esperado


def test_caminho_feliz_deve_retornar_True():
    # Arrange
    fotos = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
    estoque = 10
    valor = 150.00
    descricao = "Armação de óculos leve e resistente."
    resultado_esperado = True

    # Act
    resultado_obtido = cadastrar_produtos(
        fotos, estoque, valor, descricao
    )

    # Assert
    assert resultado_obtido == resultado_esperado