from models.competencia import Competencia
from models.perfil import Perfil
from services.recomendador import Recomendador

def menu():
    print("\n===== Future Career Advisor =====")
    print("1. Criar perfil e gerar recomendações")
    print("2. Sair")
    return input("Escolha: ")

def cadastrar_perfil():
    nome = input("\nDigite o nome do usuário: ")
    perfil = Perfil(nome)

    print("\nInforme seus níveis de competência (0 a 10):")
    competencias = [
        "Lógica", "Criatividade", "Colaboração", "Adaptabilidade",
        "Organização", "Comunicação", "Curiosidade",
        "Resolução de Problemas", "Matemática", "Empatia"
    ]

    for comp in competencias:
        while True:
            try:
                nivel = int(input(f"- {comp}: "))
                if 0 <= nivel <= 10:
                    break
                else:
                    print("Valor deve ser entre 0 e 10.")
            except:
                print("Digite um número válido.")
        perfil.adicionar_competencia(Competencia(comp, nivel))

    return perfil

def main():
    recomendador = Recomendador()

    while True:
        opc = menu()

        if opc == "1":
            perfil = cadastrar_perfil()
            perfil.exibir_perfil()

            ranking = recomendador.recomendar(perfil)

            print("\n===== Recomendações de Carreira =====")
            for carreira, score in ranking[:3]:
                print(f"- {carreira} (score: {score})")

        elif opc == "2":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
