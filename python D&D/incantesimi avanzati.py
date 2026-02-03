class Incantesimo:
    def __init__(self, nome, costo_mana, danno=0, cura=0, effetto=None):
        self.nome = nome
        self.costo_mana = costo_mana
        self.danno = danno
        self.cura = cura
        self.effetto = effetto

# -------------------------
# Incantesimi divisi per classe
# -------------------------
incantesimi_classe = {
    "Mago": [
        Incantesimo("Dardo Incantato", 3, danno=8),
        Incantesimo("Palla di Fuoco", 10, danno=20),
        Incantesimo("Scudo Magico", 5, effetto="Difesa")
    ],
    "Chierico": [
        Incantesimo("Cura Ferite", 5, cura=15),
        Incantesimo("Luce Sacra", 3, danno=10)
    ],
    "Stregone": [
        Incantesimo("Raggio Infuocato", 4, danno=12),
        Incantesimo("Telecinesi", 8)
    ]
}

# Funzione per mostrare solo incantesimi disponibili in base al mana
def incantesimi_disponibili(personaggio):
    return [i for i in incantesimi_classe.get(personaggio.classe, []) if i.costo_mana <= personaggio.mana]
