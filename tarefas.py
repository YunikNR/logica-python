tarefas = [
    {"titulo":"Estudar", "Concluida":1, "Prioridade":1},
    {"titulo":"Ler", "Concluida":0, "Prioridade":0}
]
def mostrar_tarefa():
    for tarefa in tarefas:
        if tarefa["Concluida"] == 1:
            status = "[X]" 
        else: 
            status = "[ ]"
        if tarefa["Prioridade"] == 1:
            prioridade = "Alta"
        else: 
            prioridade = "baixa"
        print()
        print(f"{status} {tarefa["titulo"]} |{prioridade}")

def mostrar_tudo():
    mostrar_tarefa()
           
def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["Concluida"] == 1:
            mostrar_tarefa()

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
    elif opcao == 0:
        mostrar()
    else:
        print("Opção inválida, tente novamente...")