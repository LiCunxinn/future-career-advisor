class Carreira:
    def __init__(self, nome: str, competencias_relevantes: dict):
        self.nome = nome
        self.competencias_relevantes = competencias_relevantes

    def pontuar(self, perfil):
        score = 0
        for comp, peso in self.competencias_relevantes.items():
            nivel = perfil.competencias.get(comp, 0)
            score += nivel * peso
        return score
