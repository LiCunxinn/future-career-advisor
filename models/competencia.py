# Classe que representa uma competência específica, como Lógica, Criatividade, etc.
# Cada competência tem um nome e um nível de 0 a 10.
class Competencia:
    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel    # nível informado pelo usuário

    def __str__(self):
        # Retorna uma representação da competência
        return f"{self.nome}: {self.nivel}/10"
