user = []
cc = []
agencia = "0001"
numeroConta = 111

def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("ERRO: Já existe um usuário cadastrado com esse CPF.")
            return None, None
        
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    endereco = {
        "rua": input("Informe sua rua: "),
        "numero": input("Informe o número da residência: "),
        "bairro": input("Informe seu bairro: "),
        "cidade": input("Informe sua cidade: "),
        "estado": input("Informe seu estado (ex.:PE): ")
    }
    
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "enderecoCompleto" : (f" {endereco['rua']}, {endereco['numero']} - {endereco['bairro']} - {endereco['cidade']}/{endereco['estado']}")
    }
    
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")
    return nome, cpf

    
    
def listar_usuarios(usuarios):
    print("=-=-=-=Lista de Usuários Cadastrados =-=-=-=")
    
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['enderecoCompleto']}")
        print("-" * 40)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def contaCorrente(agencia, numeroConta, usuarios):
    cpf = input("Informe o seu CPF: ")
    usuario =filtrar_usuario(cpf, usuarios)
    
    if usuario:
        novaConta = {
            "agencia": agencia,
            "numeroConta": numeroConta,
            "usuario": usuario
        }
        return novaConta
    else:
        print("Usuário não encontrado. crie um usuário antes.")
        return None
    
    
    
def listar_contas(cc):
    print("\n=-=-=-= Lista de Contas Correntes Cadastradas =-=-=-=")

    if not cc:
        print("Nenhuma conta corrente cadastrada.")
        return
        
    for conta in cc:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numeroConta']}
            Titular:\t{conta['usuario']['nome']}
            CPF:\t\t{conta['usuario']['cpf']}
        """
        print(linha.strip())
        print("-" * 40)



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

    
    
def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
            
        return saldo, extrato
    
      

def verExtrato(saldo, / ,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
    return saldo, extrato
