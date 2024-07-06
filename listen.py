zahlenliste = [1, 2, 3, 4, 5]
einkaufsliste = ["Milch", "Butter", "Brot", "Käse"]
gesamtliste = [zahlenliste, einkaufsliste]

def listen_ausgeben():
    print(gesamtliste)
    print(gesamtliste[0])
    print(gesamtliste[1])
    print(gesamtliste[1][2])

def element_entfernen(index):
    zahl=zahlenliste.pop(index)
    print("Entfernte Zahl: ",zahl)
    print("Liste nach dem Entfernen: ",zahlenliste)

def element_anfuegen(liste, zahl):
    liste.append(zahl)
    print("Liste nach dem Hinzufügen: ",liste)

def element_einfuegen(name, index, liste):
    liste.insert(index,name)
    print("Liste nach dem Einfügen: ",liste)

def element_ersetzen(element,index,liste):
    liste[index] = element
    print("Liste nach dem Ersetzen: ",liste)

def zahlenliste_sortieren():
    zahlenliste.sort()
    print("Liste nach dem Sortieren: ",zahlenliste)

def einkaufsliste_sortieren():
    einkaufsliste.sort()
    print("Liste nach dem Sortieren: ",einkaufsliste)

def liste_huebsch_ausgeben(liste):
    for index,element in enumerate(liste):
        print("Index: ",index," Element: ",element)

# listen_ausgeben()
# element_entfernen(2)
# element_anfuegen(zahlenliste, 6)
# element_einfuegen("Kaffee", 1, einkaufsliste)
# element_ersetzen("Mehl",2,einkaufsliste)
# zahlenliste_sortieren()
# einkaufsliste_sortieren()
# liste_huebsch_ausgeben(zahlenliste)