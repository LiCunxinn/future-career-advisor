import json
from models.carreira import Carreira

class Recomendador:
    def __init__(self):
        self.carreiras = self.carregar_carreiras()

    def carregar_carreiras(self):
        with open("data/carreiras.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        carreiras = []
        for nome, comps in data.items():
            carreiras.append(Carreira(nome, comps))
        return carreiras

    def recomendar(self, perfil):
        ranking = []
        for carreira in self.carreiras:
            score = carreira.pontuar(perfil)
            ranking.append((carreira.nome, score))

        ranking.sort(key=lambda x: x[1], reverse=True)
        return ranking
