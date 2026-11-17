from validar_senha import validar_senha
def test_tamanho_menor_que_8_deve_retornar_False():
    senha = "curta"
    resultado_esperado = False
    # Act
    resultado_obtido = validar_senha(senha)
    # Assert
    assert resultado_obtido == resultado_esperado

def test_falta_letra_maiuscula_deve_retornar_False():
    # Arrange
    senha = "semfraca1!"
    resultado_esperado = False
    # Act 
    resultado_obtido = validar_senha(senha)
    # Assert
    assert resultado_obtido == resultado_esperado

def test_falta_numero_deve_retornar_False():
    # Arrange
    senha = "Semnumeronasenha1"
    resultado_esperado = False
    # Act 
    resultado_obtido = validar_senha(senha)
    # Assert
    assert resultado_obtido == resultado_esperado

def test_falta_caractere_especial_deve_retornar_False():
    # Arrange
    senha = "NaoSemCaractereEspecial1"
    resultado_esperado = False
    # Act 
    resultado_obtido = validar_senha(senha)
    # Assert
    assert resultado_obtido == resultado_esperado

def test_caminho_feliz_deve_retornar_True():
    # Arrange
    senha = "Asenha@goraF0rte"
    resultado_esperado = True
    # Act 
    resultado_obtido = validar_senha(senha)
    # Assert
    assert resultado_obtido == resultado_esperado
