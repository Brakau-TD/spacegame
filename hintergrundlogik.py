"""
Dieses Modul enthält die Hintergrundlogik des Spiels.
Logik bedeutet hier die Regeln, die das Spiel bestimmen.
Zur Zeit gibt es drei Funktionen, die die Regeln des Spiels festlegen:
- kollision_pruefen: prüft, ob es eine Kollision zwischen Spieler und Gegner gibt
- gewinnbedingung_pruefen: prüft, ob das Spiel gewonnen ist
- bewegung_aktualisieren: aktualisiert die Bewegung der Gegner und des Spielers
"""

from sprite import Sprite

def neuer_sprite(x, y, breite, hoehe, richtung, bildpfad, name, gesundheit, energie, speed, anderesprites):
    """
    Erzeugt ein neues Sprite-Objekt mit den übergebenen Parametern und
    fügt es der Liste der anderen Sprites hinzu.
    """
    anderesprites.append(Sprite(x, y, breite, hoehe, richtung, bildpfad, name, gesundheit, energie, speed).gebe_sprite())
    return anderesprites

def sprite_entfernen(anderesprites, element):
    """
    Entfernt ein Sprite-Objekt aus der Liste der anderen Sprites.
    """
    anderesprites.remove(element)
    return anderesprites

def kollision_pruefen(spielersprite,gegnersprite,anderesprites):
    """
    Prueft, ob es eine Kollision zwischen Spieler und Gegner gibt.
    Es wird für jeden Gegner geprüft, ob es eine Kollision gibt.
    Zu Anfang geben wir nur die Anzahl der Kollisionen zurück.
    Das kann später noch erweitert werden, weil wir jetzt schon wissen, welche Gegner kollidiert sind (kollidiert_liste, nummer)
    und welche anderen Sprites mit dem Spieler kollidiert sind (andere_kollision, nummer)
    """
    kollisionen = 0
    zaehler = 0
    kollidiert_liste = []
    andere_kollision = []
    for nummer, gegner in enumerate(gegnersprite):
        if gegner.ist_kollision(spielersprite):
            kollisionen += 1
            kollidiert_liste.append(nummer)
    for nummer,anderer_sprite in enumerate(anderesprites):
        if anderer_sprite.ist_kollision(spielersprite):
            zaehler += 1
            andere_kollision.append(nummer)
    return kollisionen

def pruefe_spielende(spielstand, parameter = None):
    """
    Prüft, ob das Spiel zu Ende ist.
    Die Funktion nimmt zwei Parameter entgegen, die für die Prüfung benötigt werden.
    Noch gibt die Funktion nur None zurück.
    Du kannst diese Funktion erweitern, um eine eigene Bedingung für das Spielende zu prüfen.
    """
    if gewinnbedingung_pruefen(spielstand) and not verlorenbedingung_pruefen(parameter):
        return True
    elif not gewinnbedingung_pruefen(spielstand) and not verlorenbedingung_pruefen(parameter):
        return False
    elif not gewinnbedingung_pruefen(spielstand) and verlorenbedingung_pruefen(parameter):
        return False

def bewegung_aktualisieren(spielersprite,gegnersprite,maus_position):
    """
    Bewegt die Gegner über deren Methode neue_position_rechnen() und prüft, ob sie aus dem Spielfeld heraus sind und
    setzt die Position des Spielers auf die aktuelle Mausposition.
    Falls die Gegner in einer Liste sind, wird für jeden Gegner die Methode neue_position_rechnen() aufgerufen
    andernfalls wird nur für den einen Gegner diese Methode aufgerufen
    """
    if type(gegnersprite) == list:
        for gegner in gegnersprite:
            gegner.neue_position_rechnen()
            gegner.ist_ausserhalb()
    else:
        gegnersprite.neue_position_rechnen()
        gegnersprite.ist_ausserhalb()
    spielersprite.neue_position_setzen(maus_position[0],maus_position[1])
    
def gewinnbedingung_pruefen(spielstand):
    """
    in dieser Spielvariante wird das Spiel gewonnen, wenn der Spielstand 100 erreicht hat,
    man kann es im Moment noch nicht verlieren, aber
    man kann hier auch eine andere Bedingung für das Gewinnen des Spiels festlegen
    """
    if spielstand >= 100:
        gewonnen = True
    else:
        gewonnen = False
    return gewonnen

def verlorenbedingung_pruefen(parameter = None):
    """
    hier kann geprueft werden, ob das Spiel verloren ist
    die Funktion nimmt drei Parameter entgegen, die für die Prüfung benötigt werden
    noch gibt die Funktion nur False zurück
    du kannst diese Funktion erweitern, um eine eigene Verlorenbedingung zu prüfen
    """
    return False
