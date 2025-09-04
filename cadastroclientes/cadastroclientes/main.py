from cliente import Cliente
import banco

def menu():
    print("\n=== Cadastro de Clientes ===")
    print("1 - Incluir cliente")
    print("2 - Buscar cliente")
    print("3 - Apagar cliente")
    print("4 - Sair")

def incluir():
    codigo = input("Código: ")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cliente = Cliente(codigo, nome, email, telefone)
    if cliente.validar():
        banco.salvar_cliente(cliente)
        print("✅ Cliente salvo com sucesso.")
    else:
        print("⚠️ Dados inválidos.")

def buscar():
    codigo = input("Digite o código do cliente: ")
    dados = banco.buscar_cliente(codigo)
    if dados:
        print("📋 Dados do cliente:")
        for k, v in dados.items():
            print(f"{k.capitalize()}: {v}")
    else:
        print("❌ Cliente não encontrado.")

def apagar():
    codigo = input("Digite o código do cliente a apagar: ")
    banco.apagar_cliente(codigo)
    print("🗑️ Cliente apagado (se existia).")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            incluir()
        elif opcao == "2":
            buscar()
        elif opcao == "3":
            apagar()
        elif opcao == "4":
            print("👋 Encerrando...")
            break
        else:
            print("Opção inválida.")

