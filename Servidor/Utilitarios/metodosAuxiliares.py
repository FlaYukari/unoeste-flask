def ehvalidoDadosPet(pet):
    if pet.nome =="":
        return False
    elif pet.especie =="":
        return False
    elif pet.raca =="":
        return False    
    elif pet.cor =="":
        return False    
    elif pet.dataNasc =="":
        return False    
    elif pet.numMicrochip =="":
        return False    
    elif pet.rga =="":
        return False
    else:
        return True

#nome, rg, cpf, dataNasc, endereco, num, complemento, bairro, cep, cidade, uf, telFixo, telCel
def ehvalidoDadosCliente(cliente):
    if cliente.nome =="":
        return False
    elif cliente.rg =="":
        return False
    elif cliente.cpf =="":
        return False        
    elif cliente.dataNasc =="":
        return False
    elif cliente.endereco =="":
        return False    
    elif cliente.num =="":
        return False    
    elif cliente.complemento =="":
        return False
    elif cliente.bairro =="":
        return False
    elif cliente.cep =="":
        return False
    elif cliente.cidade =="":
        return False
    elif cliente.uf =="":
        return False
    elif cliente.telFixo =="":
        return False
    elif cliente.telCel =="":
        return False
    else:
        return True