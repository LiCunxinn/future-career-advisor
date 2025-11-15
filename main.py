# Arquivo responsável pela interface com o usuário (CLI)
from models.competencia import Competencia
from models.perfil import Perfil
from services.recomendador import Recomendador

# Função que exibe o menu principal
def menu():
    print("\n===== Future Career Advisor =====")
    print("1. Criar perfil e gerar recomendações")
    print("2. Sair")
    return input("Escolha: ")

# Função responsável por coletar informações do usuário
def cadastrar_perfil():
    nome = input("\nDigite o nome do usuário: ")
    perfil = Perfil(nome)

    print("\nInforme seus níveis de competência (0 a 10):")

    # Lista das competências analisadas pelo sistema
    competencias = [
        "Lógica", "Criatividade", "Colaboração", "Adaptabilidade",
        "Organização", "Comunicação", "Curiosidade",
        "Resolução de Problemas", "Matemática", "Empatia"
    ]

    # Pergunta o nível de cada competência ao usuário
    for comp in competencias:
        while True:
            try:
                nivel = int(input(f"- {comp}: "))
                
                # Validação para garantir nível entre 0 e 10
                if 0 <= nivel <= 10:
                    break
                else:
                    print("Valor deve ser entre 0 e 10.")
            except:
                print("Digite um número válido.")

        # Cria um objeto Competencia e adiciona ao perfil
        perfil.adicionar_competencia(Competencia(comp, nivel))

    return perfil

# Função principal que controla o fluxo da aplicação
def main():
    recomendador = Recomendador()    # Carrega carreiras e pesos

    while True:
        opc = menu()

        if opc == "1":
            perfil = cadastrar_perfil()
            perfil.exibir_perfil()

            # Gera o ranking de carreiras baseado no perfil
            ranking = recomendador.recomendar(perfil)

            print("\n===== Recomendações de Carreira =====")
            # Mostra apenas as 3 melhores
            for carreira, score in ranking[:3]:
                print(f"- {carreira} (score: {score})")

        elif opc == "2":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")
            
# Ponto de entrada do programa
if __name__ == "__main__":
    main()
