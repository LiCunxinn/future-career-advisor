# A classe Perfil representa o usuário do sistema.
# Ela armazena o nome e um conjunto de competências em um dicionário.
class Perfil:
    def __init__(self, nome: str):
        self.nome = nome
        self.competencias = {}

    def adicionar_competencia(self, competencia):
        self.competencias[competencia.nome] = competencia.nivel

    def exibir_perfil(self):
        print(f"\nPerfil de {self.nome}\nCompetências:")
        for c, n in self.competencias.items():
            print(f"- {c}: {n}/10")
