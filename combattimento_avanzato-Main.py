import random

def tiro_per_colpire(attaccante, difensore, vantaggio=False, svantaggio=False):
    dado1 = random.randint(1,20)
    dado2 = random.randint(1,20)
    if vantaggio:
        dado = max(dado1, dado2)
    elif svantaggio:
        dado = min(dado1, dado2)
    else:
        dado = dado1
    totale = dado + attaccante.attacco
    return totale >= difensore.difesa

def attacco(eroe, nemico):
    colpito = tiro_per_colpire(eroe, nemico)
    if colpito:
        danno = random.randint(1,10) + eroe.attacco
        nemico.subisci_danno(danno)
        print(f"{eroe.nome} colpisce {nemico.nome} per {danno} danni! HP rimanenti nemico: {nemico.hp}")
    else:
        print(f"{eroe.nome} manca il colpo a {nemico.nome}!")

def usa_incantesimo(personaggio, incantesimo, nemico=None):
    if personaggio.usa_mana(incantesimo.costo_mana):
        if incantesimo.danno > 0 and nemico:
            nemico.subisci_danno(incantesimo.danno)
            print(f"{personaggio.nome} lancia {incantesimo.nome} e infligge {incantesimo.danno} danni a {nemico.nome}")
        if incantesimo.cura > 0:
            personaggio.hp += incantesimo.cura
            if personaggio.hp > personaggio.hp_max:
                personaggio.hp = personaggio.hp_max
            print(f"{personaggio.nome} lancia {incantesimo.nome} e recupera {incantesimo.cura} HP")
    else:
        print(f"{personaggio.nome} non ha abbastanza mana per {incantesimo.nome}!")

