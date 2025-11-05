from funções import sacar, depositar, cadastrar_usuario, listar_usuarios, user

menu = """

[u] Acesso de usuário - digite seus dados para liberar seu acesso.
[l] Listar usuários
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "u":
        novo_nome, novo_cpf = cadastrar_usuario(user)
        
        if novo_nome and novo_cpf:
            nome_usuario = novo_nome
            print(f"Bem-vindo, {nome_usuario} ")
            
    elif opcao == "l":
        listar_usuarios(usuarios)
    
    elif opcao == "d":
        valor = float(input(f"Olá, {nome_usuario}, Informe o valor do depósito: "))
        
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: (mínimo R$500,00) "))
        saldo, extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            LIMITE_SAQUES = LIMITE_SAQUES
        )
    

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo de {nome_usuario}: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break
    

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        