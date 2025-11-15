import json
from models.carreira import Carreira

# Classe responsável por carregar as carreiras e gerar recomendações.
class Recomendador:
    def __init__(self):
        # Ao iniciar o sistema, carrega as carreiras do arquivo JSON.
        self.carreiras = self.carregar_carreiras()

    # Lê o arquivo data/carreiras.json e transforma cada carreira em um objeto Carreira
    def carregar_carreiras(self):
        with open("data/carreiras.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            
        carreiras = []
        
        # Para cada carreira no JSON, criamos um objeto Carreira
        for nome, comps in data.items():
            carreiras.append(Carreira(nome, comps))
            
        return carreiras
        
    # Gera um ranking de carreiras com base no perfil
    def recomendar(self, perfil):
        ranking = []

        # Pontua cada carreira individualmente
        for carreira in self.carreiras:
            score = carreira.pontuar(perfil)
            ranking.append((carreira.nome, score))

        # Ordena o ranking do maior para o menor score
        ranking.sort(key=lambda x: x[1], reverse=True)
        
        # Retorna a lista ordenada
        return ranking
