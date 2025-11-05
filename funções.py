def usuario():
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe seu CPF (somente números): ")
    endereco = {
        "rua": input("Informe sua rua: "),
        "numero": input("Informe o número da residência: "),
        "bairro": input("Informe seu bairro: "),
        "cidade": input("Informe sua cidade: "),
        "estado": input("Informe seu estado (ex.:PE): ")
    }
    enderecoCompleto = (f" {endereco['rua']}, {endereco['numero']} - {endereco['bairro']} - {endereco['cidade']}/{endereco['estado']}")
    return nome
    
    
def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")
        print("-" * 40)
        
    if cpf in usuarios:
        print("Já existe um usuário cadastrado com esse CPF.")
        return



def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

    
    
def depositar(saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
            
        return saldo, extrato
    
      



    