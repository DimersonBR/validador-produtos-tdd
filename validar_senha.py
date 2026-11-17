def validar_senha(senha):
    # 1. Regra do tamanho mínimo
    if len(senha) < 8:
        return False
       
    # Bandeiras para as regras de conteúdo
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False
    especiais = "!@#$%&*+-"
   
    # 2. Uma única viagem para verificar tudo
    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        if letra.isdigit():
            tem_numero = True
        if letra in especiais:
            tem_especial = True
 
    # 3. Barreiras finais de bloqueio
    if tem_maiuscula == False:
        return False      
    if tem_numero == False:
        return False
    if tem_especial == False:
        return False
       
    # Caminho Feliz (Passou por todas as barreiras)
    return True