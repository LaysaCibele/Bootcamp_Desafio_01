from funções import sacar, depositar, verExtrato,  cadastrar_usuario, listar_usuarios, contaCorrente, listar_contas,  user, cc, agencia, numeroConta

menu = """

[u] Acesso de usuário - digite seus dados para liberar seu acesso.
[cc] Criar conta corrente
[l] Listar usuários
[lc] Listar conta corrente
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
            print(f"Bem-vindo!")
            
            
    elif opcao == "cc":
        conta = contaCorrente(agencia, numeroConta, user)
        if conta:
            cc.append(conta)
            numeroConta += 1
            
    elif opcao == "l":
        listar_usuarios(user)
        
        
    elif opcao == "lc":
        listar_contas(cc)
    
    elif opcao == "d":
        valor = float(input(f"Informe o valor do depósito: "))
        
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
        verExtrato(saldo, extrato=extrato)

    elif opcao == "q":
        break
    

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

