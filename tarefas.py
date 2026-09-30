tarefas = [
    {"titulo":"Estudar", "concluida":"[X]", "prioridade":"Alta"},
    {"titulo":"Ler", "concluida":"[ ]", "prioridade":"Baixa"}
]

def mostrar_tudo():
    for tarefa in tarefas:
        print()
        print(f"{tarefa["concluida"]} {tarefa["titulo"]} |{tarefa["prioridade"]}")

def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["concluida"] == "[X]":
            print("|")
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} |{tarefa["prioridade"]}")

def mostrar_pendentes():
    for tarefa in tarefas:
        if tarefa["concluida"] == "[ ]":
            print("|")
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} |{tarefa["prioridade"]}")

def mostrar_prioridade():
    for tarefa in tarefas:
        if tarefa["prioridade"] == "Alta":
            print(" |")
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} |{tarefa["prioridade"]}")
        if tarefa["prioridade"] == "Baixa":
            print(" |")
            print(f"{tarefa["concluida"]} {tarefa["titulo"]} |{tarefa["prioridade"]}")

def cadastrar():
    titulo = input("Qual é o titulo? ")
    prioridade = input("Qual é a prioridade? ")
    concluida = input("Já foi concluida? ")
    nova_tarefa = [{titulo},{concluida},{prioridade}]
    tarefas.append(nova_tarefa)
    print("Tarefa cadastrada com sucesso.")

def finalizar():
    resposta = input("Qual item deseja modificar? ")
    for tarefa in tarefas:
        if tarefa["titulo"] == resposta:
            tarefa["concluida"] = "[X]"
            print("Tarefa concluida.")

def excluir():
    resposta = input("Qual item deseja excluir? ")
    for tarefa in tarefas:
        if tarefa["titulo"] == resposta:
            tarefas.remove(tarefa)
            print("Tarefa excluida.")

while True:
    print("\n---\n Lista de Tarefas \n---\n")
    print("1 - Mostrar todas as tarefas")
    print("2 - Mostrar as tarefas concluidas")
    print("3 - Mostrar as tarefas pendentes")
    print("4 - Mostrar as tarefas por prioridade")
    print("5 - Cadastrar nova tarefa")
    print("6 - Finalizar uma tarefa")
    print("7 - Excluir tarefa")
    print("8 - Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        mostrar_tudo()
    elif opcao == 2:
        mostrar_concluidas()
    elif opcao == 3:
        mostrar_pendentes()
    elif opcao == 4:
        mostrar_prioridade()
    elif opcao == 5:
        cadastrar()
    elif opcao == 6:
        finalizar()
    elif opcao == 7:
        excluir()
    elif opcao == 8:
        print("Saindo do sistema...")
        exit()