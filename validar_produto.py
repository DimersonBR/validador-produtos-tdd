import math


def cadastrar_produtos(fotos, estoque, valor, descricao):
    # 1. O produto deve possuir pelo menos 3 fotos
    if not isinstance(fotos, list) or len(fotos) < 3:
        return False

    for foto in fotos:
        if not isinstance(foto, str) or not foto.strip():
            return False

    # 2. O estoque deve ser inteiro e não pode ser negativo
    if type(estoque) is not int or estoque < 0:
        return False

    # 3. O valor é obrigatório e não pode ser negativo
    if type(valor) not in (int, float):
        return False

    if not math.isfinite(valor) or valor < 0:
        return False

    # 4. A descrição é obrigatória
    if not isinstance(descricao, str) or not descricao.strip():
        return False

    # 5. A descrição deve possuir no máximo 255 caracteres
    if len(descricao) > 255:
        return False

    # Caminho feliz: passou por todas as barreiras
    return True