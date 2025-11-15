# A classe Perfil representa o usuário do sistema.
# Ela armazena o nome e um conjunto de competências em um dicionário.
class Perfil:
    def __init__(self, nome: str):
        self.nome = nome
        # Armazena as competências no formato: {"Lógica": 8, "Criatividade": 6, ...}
        self.competencias = {}

    # Adiciona uma competência ao perfil
    def adicionar_competencia(self, competencia):
        # Usa o nome da competência como chave e o nível como valor
        self.competencias[competencia.nome] = competencia.nivel

    # Exibe as informações completas do perfil
    def exibir_perfil(self):
        print(f"\nPerfil de {self.nome}\nCompetências:")
        for c, n in self.competencias.items():
            print(f"- {c}: {n}/10")
