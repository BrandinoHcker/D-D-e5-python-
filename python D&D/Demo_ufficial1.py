import random

# ============================
# Classi e sottoclassi PHB 2024
# ============================

classi_phb2024 = {
    "Barbaro": ["Berserker", "Wild Heart", "World Tree", "Zealot"],
    "Bardo": ["Dance", "Glamour", "Lore", "Valor"],
    "Chierico": ["Life", "Light", "Trickery", "War"],
    "Druido": ["Land", "Moon", "Sea", "Stars"],
    "Combattente": ["Champion", "Battle Master", "Eldritch Knight", "Cavalier"],
    "Monaco": ["Way of the Open Hand", "Way of Shadow", "Way of Four Elements", "Way of Drunken Master"],
    "Paladino": ["Oath of Devotion", "Oath of Vengeance", "Oath of Ancients", "Oath of Redemption"],
    "Ranger": ["Hunter", "Beast Master", "Gloom Stalker", "Horizon Walker"],
    "Rogue": ["Thief", "Assassin", "Arcane Trickster", "Swashbuckler"],
    "Stregone": ["Draconic Bloodline", "Wild Magic", "Storm Sorcery", "Aberrant Mind"],
    "Warlock": ["Archfey", "Fiend", "Great Old One", "Hexblade"],
    "Mago": ["Abjuration", "Conjuration", "Divination", "Evocation", "Illusion", "Necromancy", "Transmutation", "Enchantment"],
    "Artificer": ["Alchemist", "Artillerist", "Battle Smith", "Armorer"]
}

# ============================
# Sottoclassi: bonus e abilità passive
# ============================

sottoclassi_stats = {
    "Berserker": {"hp_bonus": 20, "attacco_bonus": 5, "abilita": ["Furia"]},
    "Wild Heart": {"hp_bonus": 15, "mana_bonus": 5, "abilita": ["Rigenerazione lenta"]},
    "World Tree": {"difesa_bonus": 3, "abilita": ["Protezione alleata"]},
    "Zealot": {"attacco_bonus": 4, "abilita": ["Ignora danni mortali una volta"]},
    "Dance": {"mana_bonus": 5, "abilita": ["Bonus movimento"]},
    "Glamour": {"abilita": ["Affascina nemici"]},
    "Lore": {"abilita": ["Bonus conoscenza e percezione"]},
    "Valor": {"difesa_bonus": 2, "abilita": ["Bonus difensivo compagni"]},
    "Life": {"mana_bonus": 10, "abilita": ["Cura passiva"]},
    "Light": {"abilita": ["Bonus danno luminoso"]},
    "Trickery": {"abilita": ["Furtività aumentata"]},
    "War": {"attacco_bonus": 3, "difesa_bonus": 2},
    "Land": {"abilita": ["Rigenerazione terreno"]},
    "Moon": {"abilita": ["Forma selvatica potente"]},
    "Sea": {"abilita": ["Bonus danno acquatico"]},
    "Stars": {"abilita": ["Bonus magia stellare"]},
    "Champion": {"attacco_bonus": 2, "abilita": ["Critici frequenti"]},
    "Battle Master": {"abilita": ["Manovre tattiche"]},
    "Eldritch Knight": {"mana_bonus": 10, "abilita": ["Magia combinata"]},
    "Cavalier": {"difesa_bonus": 3, "abilita": ["Difesa del compagno"]},
    "Way of the Open Hand": {"abilita": ["Colpi speciali"]},
    "Way of Shadow": {"abilita": ["Furtività avanzata"]},
    "Way of Four Elements": {"mana_bonus": 5, "abilita": ["Elementi combinati"]},
    "Way of Drunken Master": {"abilita": ["Evasione agile"]},
    "Oath of Devotion": {"abilita": ["Giuramento sacro"]},
    "Oath of Vengeance": {"attacco_bonus": 2, "abilita": ["Punizione rapida"]},
    "Oath of Ancients": {"difesa_bonus": 2, "abilita": ["Protezione naturale"]},
    "Oath of Redemption": {"abilita": ["Non letale"]},
    "Hunter": {"attacco_bonus": 2, "abilita": ["Caccia precisa"]},
    "Beast Master": {"abilita": ["Animale compagno"]},
    "Gloom Stalker": {"abilita": ["Furtività nelle tenebre"]},
    "Horizon Walker": {"abilita": ["Bonus movimento planare"]},
    "Thief": {"abilita": ["Scasso rapido"]},
    "Assassin": {"attacco_bonus": 2, "abilita": ["Colpo letale"]},
    "Arcane Trickster": {"mana_bonus": 5, "abilita": ["Magia furtiva"]},
    "Swashbuckler": {"abilita": ["Movimento agile"]},
    "Draconic Bloodline": {"attacco_bonus": 2, "abilita": ["Resistenza draconica"]},
    "Wild Magic": {"abilita": ["Effetti casuali"]},
    "Storm Sorcery": {"abilita": ["Volo temporaneo"]},
    "Aberrant Mind": {"mana_bonus": 5, "abilita": ["Psichico"]},
    "Archfey": {"abilita": ["Manipolazione mentale"]},
    "Fiend": {"attacco_bonus": 2, "abilita": ["Infligge paura"]},
    "Great Old One": {"mana_bonus": 5, "abilita": ["Telepatia"]},
    "Hexblade": {"abilita": ["Arma magica"]},
    "Abjuration": {"difesa_bonus": 3, "abilita": ["Scudi magici"]},
    "Conjuration": {"abilita": ["Evocazioni"]},
    "Divination": {"abilita": ["Predizione"]},
    "Evocation": {"attacco_bonus": 2, "abilita": ["Magia esplosiva"]},
    "Illusion": {"abilita": ["Inganno visivo"]},
    "Necromancy": {"abilita": ["Evocazione non morti"]},
    "Transmutation": {"abilita": ["Trasformazione"]},
    "Enchantment": {"abilita": ["Controllo mentale"]},
    "Alchemist": {"abilita": ["Pozioni e miscugli"]},
    "Artillerist": {"attacco_bonus": 2, "abilita": ["Cannoni magici"]},
    "Battle Smith": {"abilita": ["Costruzioni magiche"]},
    "Armorer": {"difesa_bonus": 3, "abilita": ["Armatura speciale"]}
}

# ============================
# Classe Personaggio
# ============================

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
        self.difesa = 5
        self.abilita_passive = []
        self.applica_sottoclasse()

    def vivo(self):
        return self.hp > 0

    def subisci_danno(self, danno):
        self.hp -= max(0, danno - self.difesa)
        if self.hp < 0:
            self.hp = 0

    def applica_sottoclasse(self):
        stats = sottoclassi_stats.get(self.sottoclasse)
        if stats:
            self.hp += stats.get("hp_bonus", 0)
            self.hp_max += stats.get("hp_bonus", 0)
            self.mana += stats.get("mana_bonus", 0)
            self.mana_max += stats.get("mana_bonus", 0)
            self.attacco += stats.get("attacco_bonus", 0)
            self.difesa += stats.get("difesa_bonus", 0)
            self.abilita_passive += stats.get("abilita", [])

    def stampa_statistiche(self):
        print(f"\n--- {self.nome} ---")
        print(f"Classe: {self.classe} ({self.sottoclasse})")
        print(f"Livello: {self.livello}")
        print(f"HP: {self.hp}/{self.hp_max}")
        print(f"Mana: {self.mana}/{self.mana_max}")
        print(f"Attacco: {self.attacco}")
        print(f"Difesa: {self.difesa}")
        print(f"Abilità passive: {self.abilita_passive}")
        print("-------------------\n")

# ============================
# Incantesimi demo
# ============================

incantesimi = {
    "Mago": [
        {"nome": "Palla di Fuoco", "mana": 5, "danno": 25},
        {"nome": "Raggio di Gelo", "mana": 4, "danno": 20}
    ],
    "Chierico": [
        {"nome": "Cura Ferite", "mana": 3, "cura": 20}
    ]
}

# ============================
# Nemici demo
# ============================

nemici_demo = {
    "Goblin": {"hp": 30, "attacco": 5, "difesa": 1},
    "Orco": {"hp": 50, "attacco": 8, "difesa": 2}
}

# ============================
# Mappe ASCII demo
# ============================

mapa_demo = [
    ["Città", "Strada", "Strada", "Dungeon"],
    ["Strada", "Strada", "Strada", "Strada"],
    ["Foresta", "Foresta", "Strada", "Strada"]
]

# ============================
# Funzioni di gioco
# ============================

def combattimento(eroe, nemico_nome):
    nemico = nemici_demo[nemico_nome].copy()
    print(f"\nCombattimento: {eroe.nome} vs {nemico_nome}!\n")
    while eroe == eroe.vivo() and nemico["hp"]>0:
        print(f"{eroe.nome} HP: {eroe.hp} | {nemico_nome} HP: {nemico['hp']}")
        azione = input("Scegli azione: (1) Attacco (2) Magia: ")
        if azione=="1":
            danno = eroe.attacco + random.randint(-2,2)
            print(f"{eroe.nome} infligge {danno} danno!")
            nemico["hp"] -= danno
        elif azione=="2":
            spell = incantesimi.get(eroe.classe, [])
            if not spell:
                print("Nessuna magia disponibile!")
                continue
            print("Magie disponibili:")
            for i,s in enumerate(spell):
                print(f"{i+1}) {s['nome']} (Mana: {s['mana']})")
            scelta = int(input("Scegli magia: "))-1
            if scelta<0 or scelta>=len(spell):
                print("Scelta non valida!")
                continue
            mag = spell[scelta]
            if eroe.mana < mag["mana"]:
                print("Mana insufficiente!")
                continue
            eroe.mana -= mag["mana"]
            danno = mag.get("danno",0)
            cura = mag.get("cura",0)
            if cura>0:
                eroe.hp = min(ero.hp+cura, ero.hp_max)
                print(f"{eroe.nome} si cura {cura} HP!")
            if danno>0:
                nemico["hp"] -= danno
                print(f"{eroe.nome} lancia {mag['nome']} infliggendo {danno} danno!")
        if nemico["hp"]>0:
            dmg = nemico["attacco"] + random.randint(-1,2)
            ero.subisci_danno(dmg)
            print(f"{nemico_nome} infligge {dmg} danno!")
    if eroe.vivo():
        print(f"\n{eroe.nome} ha vinto!\n")
    else:
        print(f"\n{eroe.nome} è stato sconfitto...\n")

def muovi_personaggio(pos):
    x,y = pos
    print(f"\nSei in: {mapa_demo[y][x]}")
    direzione = input("Dove vuoi muovere? (w/a/s/d): ")
    if direzione=="w" and y>0:
        y-=1
    elif direzione=="s" and y<len(mapa_demo)-1:
        y+=1
    elif direzione=="a" and x>0:
        x-=1
    elif direzione=="d" and x<len(mapa_demo[0])-1:
        x+=1
    else:
        print("Mossa non valida!")
    print(f"Spostato in: {mapa_demo[y][x]}")
    return (x,y)

# ============================
# Main loop di gioco
# ============================

def main():
    print("=== Benvenuto nell'RPG Testuale D&D 2024 Demo ===")
    nome = input("Inserisci nome del tuo personaggio: ")
    print("Classi disponibili:")
    for i,c in enumerate(classi_phb2024.keys()):
        print(f"{i+1}) {c}")
    scelta_c = int(input("Scegli classe: "))-1
    classe = list(classi_phb2024.keys())[scelta_c]
    print(f"Sottoclassi disponibili per {classe}:")
    for i,s in enumerate(classi_phb2024[classe]):
        print(f"{i+1}) {s}")
    scelta_s = int(input("Scegli sottoclasse: "))-1
    sottoclasse = classi_phb2024[classe][scelta_s]

    eroe = Personaggio(nome, classe, sottoclasse)
    posizione = (0,0)

    while eroe.vivo():
        eroe.stampa_statistiche()
        print("Menu: (1) Muovi (2) Combatti (3) Magia (4) Statistiche (5) Esci")
        scelta = input("Scegli azione: ")
        if scelta=="1":
            posizione = muovi_personaggio(posizione)
        elif scelta=="2":
            nemico = random.choice(list(nemici_demo.keys()))
            combattimento(eroe, nemico)
        elif scelta=="3":
            if not incantesimi.get(eroe.classe):
                print("Nessuna magia disponibile!")
                continue
            print("Magie disponibili:")
            for i,s in enumerate(incantesimi[eroe.classe]):
                print(f"{i+1}) {s['nome']} (Mana: {s['mana']})")
        elif scelta=="4":
            eroe.stampa_statistiche()
        elif scelta=="5":
            print("Grazie per aver giocato!")
            break
        else:
            print("Scelta non valida!")

if __name__=="__main__":
    main()
