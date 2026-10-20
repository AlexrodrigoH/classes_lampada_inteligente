import os
import json
from datetime import datetime

class Lampada:
    def __init__(self, estado):
        self.estado = estado
    def lampada_ligada(self):
        print("\033[32mLigada\033[0m")
    def lampada_desligada(self):
        print("\033[31mDesligada\033[0m")
    def lampada_queimou(self):
        print("\033[90mQueimou\033[0m")
class Salva_registro:
    def registro(self, estado, contar):
        historico = []
        if os.path.exists("historico_lampada.json"):
            with open("historico_lampada.json", "r", encoding="utf-8") as arquivo:
                historico = json.load(arquivo)
        data = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        self.status_lampada = {"data": data,"status": estado, "usos": contar}
        historico.append(self.status_lampada)
        self.status_lampada = historico
        with open("historico_lampada.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.status_lampada, arquivo, indent=4, ensure_ascii=False)