import random

# -------------------------
# Classe base Personaggio
# -------------------------
class Personaggio:
    def __init__(self, nome, classe, sottoclasse):
        self.nome = nome
        self.classe = classe
        self.sottoclasse = sottoclasse
        self.livello = 1
        self.hp = 100
        self.hp_max = 100
        self.mana = 50
        self.mana_max = 50
        self.attacco = 10
        self.difesa = 10
        self.incantesimi = []
        self.abilita_passive = []
        self.condizioni = []

    def vivo(self):
        return self.hp > 0

    def usa_mana(self, costo):
        if self.mana >= costo:
            self.mana -= costo
            return True
        return False

    def subisci_danno(self, danno):
        self.hp -= danno
        if self.hp < 0:
            self.hp = 0

# -------------------------
# Classi e sottoclassi
# -------------------------
class Barbari(Personaggio):
    percorsi = ["Berserker", "Wild Heart", "World Tree", "Zealot"]

    def __init__(self, nome, sottoclasse):
        super().__init__(nome, "Barbaro", sottoclasse)
        self.hp = 120
        self.hp_max = 120
        self.attacco = 15
        # abilità passive della sottoclasse
        self.abilita_passive = self.abilita_barbaro(sottoclasse)

    def abilita_barbaro(self, sottoclasse):
        abilita = []
        if sottoclasse == "Berserker":
            abilita.append("Aumenta danni in Furia")
        elif sottoclasse == "Wild Heart":
            abilita.append("Rigenera HP lentamente fuori combattimento")
        elif sottoclasse == "World Tree":
            abilita.append("Bonus difensivo ad alleati vicini")
        elif sottoclasse == "Zealot":
            abilita.append("Ignora danni mortali una volta")
        return abilita

class Bardo(Personaggio):
    percorsi = ["Dance", "Glamour", "Lore", "Valor"]

    def __init__(self, nome, sottoclasse):
        super().__init__(nome, "Bardo", sottoclasse)
        self.mana = 60
        self.mana_max = 60
        self.attacco = 8
        self.abilita_passive = self.abilita_bardo(sottoclasse)

    def abilita_bardo(self, sottoclasse):
        abilita = []
        if sottoclasse == "Dance":
            abilita.append("Bonus a movimento e evasione")
        elif sottoclasse == "Glamour":
            abilita.append("Affascina nemici passivamente")
        elif sottoclasse == "Lore":
            abilita.append("Bonus conoscenza e percezione")
        elif sottoclasse == "Valor":
            abilita.append("Bonus difensivo a compagni vicini")
        return abilita

class Chierico(Personaggio):
    percorsi = ["Life", "Light", "Trickery", "War"]

    def __init__(self, nome, sottoclasse):
        super().__init__(nome, "Chierico", sottoclasse)
        self.mana = 70
        self.mana_max = 70
        self.attacco = 6
        self.abilita_passive = self.abilita_chierico(sottoclasse)

    def abilita_chierico(self, sottoclasse):
        abilita = []
        if sottoclasse == "Life":
            abilita.append("Cura passiva più efficace")
        elif sottoclasse == "Light":
            abilita.append("Bonus danno luminoso")
        elif sottoclasse == "Trickery":
            abilita.append("Furtività aumentata")
        elif sottoclasse == "War":
            abilita.append("Aumenta attacco e difesa in battaglia")
        return abilita

class Druido(Personaggio):
    percorsi = ["Land", "Moon", "Sea", "Stars"]

    def __init__(self, nome, sottoclasse):
        super().__init__(nome, "Druido", sottoclasse)
        self.mana = 60
        self.mana_max = 60
        self.attacco = 7
        self.abilita_passive = self.abilita_druido(sottoclasse)

    def abilita_druido(self, sottoclasse):
        abilita = []
        if sottoclasse == "Land":
            abilita.append("Rigenerazione terreno favorevole")
        elif sottoclasse == "Moon":
            abilita.append("Forma selvatica più potente")
        elif sottoclasse == "Sea":
            abilita.append("Bonus danno acquatico")
        elif sottoclasse == "Stars":
            abilita.append("Bonus magia stellare")
        return abilita

# Puoi continuare allo stesso modo con: Combattente, Monaco, Paladino, Ranger, Rogue, Stregone, Warlock, Mago
