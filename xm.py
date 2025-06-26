class Viagem:
    def __init__(self, nome_viajante, destino):
        self.nome_viajante = nome_viajante
        self.destino = destino

    def mostrar_resumo(self):
        print("\nCadastro concluído!")
        print(f"Viajante: {self.nome_viajante}")
        print(f"Destino selecionado: {self.destino}")


class SistemaCadastro:
    destinos_disponiveis = ["Paris", "Petrolina", "Juazeiro", "Rio de Janeiro"]

    def exibir_opcoes(self):
        print("Opções de destino:")
        for i, destino in enumerate(self.destinos_disponiveis, 1):
            print(f"{i}. {destino}")

    def selecionar_destino(self):
        self.exibir_opcoes()
        escolha = int(input("Escolha o número do destino desejado: ")) - 1
        return self.destinos_disponiveis[escolha]


def main():
    print("=== Cadastro de Viagem ===")
    nome = input("Digite o nome do viajante: ")
    sistema = SistemaCadastro()
    destino_escolhido = sistema.selecionar_destino()
    viagem = Viagem(nome, destino_escolhido)
    viagem.mostrar_resumo()


if __name__ == "__main__":
    main()

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} (Autor: {self.autor})"


class Biblioteca:
    def __init__(self):
        self.livros = [
            Livro("A Arte da Guerra", "Sun Tzu"),
            Livro("Dom Casmurro", "Machado de Assis")
        ]

    def mostrar_livros(self):
        print("Livros disponíveis para empréstimo:")
        for i, livro in enumerate(self.livros, 1):
            print(f"{i}. {livro}")

    def emprestar_livro(self, indice):
        return self.livros[indice - 1]


def main():
    print("=== Sistema de Empréstimo de Livros ===")
    nome = input("Digite o nome do solicitante: ")
    biblioteca = Biblioteca()
    biblioteca.mostrar_livros()
    escolha = int(input("Escolha o número do livro desejado: "))
    livro_escolhido = biblioteca.emprestar_livro(escolha)
    print("\nEmpréstimo realizado com sucesso!")
    print(f"Solicitante: {nome}")
    print(f"Livro emprestado: {livro_escolhido}")


if __name__ == "__main__":
    main()

frutas = ["Maçã", "Banana", "Uva", "Laranja", "Abacaxi"]

print("Bem-vindo à Feira Livre!")
print("Frutas disponíveis:")
for i, fruta in enumerate(frutas, 1):
    print(f"{i}. {fruta}")

nome = input("Digite seu nome: ")
escolha = int(input("Escolha o número da fruta desejada: "))

if 1 <= escolha <= len(frutas):
    fruta_escolhida = frutas[escolha - 1]
    print(f"\n{nome}, você escolheu a fruta: {fruta_escolhida}")
else:
    print("Escolha inválida. Tente novamente.")

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        else:
            print("\nContatos na Agenda:")
            for contato in self.contatos:
                print(contato)


agenda = Agenda()
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")
contato = Contato(nome, telefone, email)
agenda.adicionar_contato(contato)
agenda.listar_contatos()
