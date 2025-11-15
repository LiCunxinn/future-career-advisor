# A classe Carreira representa uma profissão do futuro.
# Ela possui um nome e uma lista de competências relevantes com pesos associados.
class Carreira:
    def __init__(self, nome: str, competencias_relevantes: dict):
        self.nome = nome
        # Dicionário de competências importantes e seus pesos.
        self.competencias_relevantes = competencias_relevantes

    # Calcula o score da carreira com base no perfil do usuário
    def pontuar(self, perfil):
        score = 0

        # Percorre todas as competências importantes da carreira
        for comp, peso in self.competencias_relevantes.items():
            # Pega o nível da competência do usuário. Se não tiver, assume 0.
            nivel = perfil.competencias.get(comp, 0)
            # Multiplica o nível pelo peso
            score += nivel * peso

        # Retorna o score final da carreira
        return score
