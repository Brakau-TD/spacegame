guthaben = 300
apple = ("Apple", 200)
microsoft = ("Microsoft", 301)
amazon = ("Amazon", 50)
aktien = [apple, microsoft, amazon]

def aktien_kaufen(kaufen):
    if kaufen == "Ja":
        print("Ich kaufe Aktien.")
    elif kaufen == "Nein":
        print("Ich kaufe keine Aktien.")
    else:
        print("Ich kaufe nicht.")

def ist_erschwinglich(aktienpreis):
    if guthaben >= aktienpreis:
        print("Die Aktie ist erschwinglich.")
        return True
    else:
        print("Die Aktie ist nicht erschwinglich.")
        print()
        return False
    
def zeige_aktien():
    print("Aktienkurse:")
    for nummer, aktie in enumerate(aktien):
        print("Aktie ", nummer, ": ",aktie[0], "kostet", aktie[1], "Euro")

def programmende():
    print("Das Programm wird beendet.")
    exit()

def begruessung(guthaben):
    print("**************   Willkommen zur Aktienapp.**************")
    print("Du hast ein Guthaben von",guthaben,"Euro.")
    print("Die Aktienkurse sind: ")
    zeige_aktien()
    print("Möchtest du Aktien kaufen?")
    kaufen = input("Ja, Nein, Exit: ")
    return kaufen

def aktienapp(guthaben):
    kaufen = begruessung(guthaben)

    if kaufen == "Ja":
        aktiennummer = int(input("Welche Aktie möchtest du kaufen? "))
        aktienpreis = aktien[aktiennummer][1]
        if ist_erschwinglich(aktienpreis):
            print("Du hast die Aktie",aktien[aktiennummer][0],"gekauft.")
            guthaben = guthaben-aktienpreis
            print("Dein Guthaben beträgt jetzt",guthaben,"Euro.")
            print()
        elif not ist_erschwinglich(aktienpreis):
            input("Drücke Enter, um fortzufahren.")
    elif kaufen == "Nein" or kaufen == "Exit":
        programmende()

    aktienapp(guthaben)



aktienapp(guthaben)