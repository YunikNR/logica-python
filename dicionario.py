clientes = [
    {"nome":"ana", "nota":8, "cel":"11 9224-0984"},
    {"nome":"joao", "nota":5, "cel":"11 9114-0224"},
    {"nome":"marcel", "nota":0, "cel":"11 9214-0984"}
]

def mostrar():
    print(clientes)

def cadastrar():
    nome = input("Nome: ")
    nota = input("Nota: ")
    cel = input("Celular: ")

    novo_cliente = {
        "nome":nome,
        "nota":nota,
        "cel":cel
    }
    clientes.append(novo_cliente)
    print("safado cadastrado com sucesso.")

def remover():
    nome = input("Qual o nome do cliente? ")
    for cliente in clientes:
        if cliente["nome"] == nome:
            clientes.remove(cliente)

while True:
    print("Alunos")
    print("1 - Mostrar lista")
    print("2 - Cadastrar produto na lista")
    print("3 - Cancelar CPF")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        mostrar()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção inválida, tente novamente...")