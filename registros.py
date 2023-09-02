# meu programa de registros, by: italo gabriel - 044704
# Deve criar um arquivo com nome " cadastros.txt "

def novo_registro():
    nome = input("Digite o Nome:")
    sexo = input("Digite o Sexo:")
    idade = input("Digite a Idade:")
    cpf = input("Digite o CPF:")
    data_de_nascimento = input("Digite a Data de Nascimento:")
    cidade = input("Digite a Cidade de Nascimento:")
    estado = input("Digite o Estado de Nascimento:")
    pais = input("Digite o País de Nascimento:")

    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(f"{nome},{sexo},{idade},{cpf},{data_de_nascimento},{cidade},{estado},{pais}\n")

    print("Registro adicionado com sucesso!")

def mostrar_registros():
    try:
        with open("cadastros.txt", "r") as arquivo:
            registros = arquivo.readlines()

            if registros:
                print("\nLista de registros:")
                for i, registro in enumerate(registros, start=1):
                    nome, sexo, idade, cpf, data_de_nascimento, cidade, estado, pais = registro.strip().split(',')
                    print(f"{i}. Nome: {nome}\n Sexo: {sexo}\n Idade: {idade}\n CPF: {cpf}\n Data de Nascimento: {data_de_nascimento}\n Cidade: {cidade}\n Estado: {estado}\n País: {pais}")
            else:
                print("Nenhum registro encontrado.")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")

def deletar_registro():
    try:
        with open("cadastros.txt", "r") as arquivo:
            registros = arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum registro encontrado.")
        return

    if not registros:
        print("Nenhum registro encontrado.")
        return

    print("\nLista de registros:")
    for i, registro in enumerate(registros, start=1):
        nome, sexo, idade, cpf, data_de_nascimento, cidade, estado, pais = registro.strip().split(',')
        print(f"{i}. Nome: {nome}\n Sexo: {sexo}\n Idade: {idade}\n CPF: {cpf}\n Data de Nascimento: {data_de_nascimento}\n Cidade: {cidade}\n Estado: {estado}\n País: {pais}")

    try:
        numero_registro = int(input("Digite o número do registro que deseja deletar: "))
    except ValueError:
        print("Número de registro inválido.")
        return

    if 1 <= numero_registro <= len(registros):
        del registros[numero_registro - 1]
        with open("cadastros.txt", "w") as arquivo:
            arquivo.writelines(registros)
        print("Registro deletado com sucesso.")
    else:
        print("Número de registro fora do intervalo válido.")

def pesquisa_por_cpf():
    try:
        cpf_pesquisa = input("Digite o CPF que deseja pesquisar: ")

        with open("cadastros.txt", "r") as arquivo:
            registros = arquivo.readlines()

            if registros:
                encontrado = False
                for registro in registros:
                    nome, sexo, idade, cpf, data_de_nascimento, cidade, estado, pais = registro.strip().split(',')
                    if cpf == cpf_pesquisa:
                        encontrado = True
                        print(f"Registro encontrado:\n Nome: {nome}\n Sexo: {sexo}\n Idade: {idade}\n CPF: {cpf}\n Data de Nascimento: {data_de_nascimento}\n Cidade: {cidade}\n Estado: {estado}\n País: {pais}")
                        break

                if not encontrado:
                    print("CPF não encontrado.")
            else:
                print("Nenhum registro encontrado.")
    except FileNotFoundError:
        print("Nenhum registro encontrado.")

def main():
    while True:
        print(" ------------- Registros By: Italo -------------")
        print("\nMenu:")
        print("1. Adicionar registro")
        print("2. Listar registros")
        print("3. Deletar registro")
        print("4. Pesquisar registro por CPF")
        print("5. Sair")
        print(" ------------- Registros By: Italo -------------")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novo_registro()
        elif escolha == '2':
            mostrar_registros()
        elif escolha == '3':
            deletar_registro()
        elif escolha == '4':
            pesquisa_por_cpf()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
