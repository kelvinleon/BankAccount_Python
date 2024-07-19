import textwrap
def menu ():
    
 menu = """
 bem vindo . digite a opção desejada :
   1- sacar
   2- depositar
   3- extrato 
   4- cadastro de usuario
   5- listar usuarios
   6- listar contas 
   7- sair  
 
 ==>""" 
 return input(textwrap.dedent(menu))

def sacar (*, saldo, valor,extrato, limite ,numero_saques,limite_saques):
 # and  valor <limite and numero_saques < limite_saques
  
  
   if  numero_saques == limite_saques :
    print ("operação impossivel. Excedeu o numero de saques diarios possiveis")
    
    
   elif   valor > saldo  :
    print ("saldo insuficiente")

   elif valor > limite :
    print ("limite indisponivel")

   elif saldo >=valor and valor == limite:
    
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques = numero_saques+1
    print("\n Saque realizado com sucesso! ")
    

   else:
     ("tente novamente")


    
   return(saldo, extrato)

def deposito (saldo, valor, extrato):
   saldo += valor 
   extrato += f"Deposito:\t\tR$ {valor:.2f}\n"
   print("\n Deposito realizado com sucesso! ")
  
   return (saldo,extrato)

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

 
    return (extrato)
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
     
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "2":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "1":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            ) 
           
            
            numero_saques=numero_saques+1
            limite = 500
            LIMITE_SAQUES=3
            print (f"{numero_saques}")
            
            
            
           

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Operação inválida ")


main()
