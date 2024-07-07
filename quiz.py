fragen = {"Hauptstadt von Deutschland": "Berlin",
          "Hauptstadt von Frankreich": "Paris",
          "Hauptstadt von Italien": "Rom",
          "Hauptstadt von Spanien": "Madrid",
          "Hauptstadt von Portugal": "Lissabon",
          "Hauptstadt von Polen": "Warschau",
          "Hauptstadt von Österreich": "Wien",
          "Hauptstadt von Schweiz": "Bern",}

def spiele_quiz(quizfragen):
    richtig = 0
    mögliche = len(quizfragen)
    for frage in quizfragen:
        antwort = fragen_darstellen(frage)
        if antwort == fragen[frage].lower():
            spieltext_darstellen("Richtig!")
        else:
            spieltext_darstellen("Falsch! Die richtige Antwort ist " + fragen[frage])
    return richtig, mögliche

def fragen_darstellen(frage):
    antwort = input(frage + ": ")
    return antwort.lower()

def spieltext_darstellen(text):
    print(text)

def spiel_beenden():
    richtig, mögliche = spiele_quiz()
    spieltext_darstellen("Du hast " + str(richtig) + " von " + str(mögliche) + " Fragen richtig beantwortet.")

def abfrage_darstellen(text):
    print(text)
    return input()

def nochmal_spielen():
    antwort = abfrage_darstellen("Möchtest du nochmal spielen? (Ja/Nein): ")
    if antwort.lower() == "ja":
        spiele_quiz()

if __name__ == "__main__":
    spiele_quiz(fragen)
    spiel_beenden()
    nochmal_spielen()

# Ideen für Erweiterungen:
# - Füge weitere Fragen hinzu.
# - Füge eine Zeitbegrenzung hinzu:
    # https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
    # oder: https://www.delftstack.com/de/howto/python/time.clock-python/
# - Füge eine Highscoreliste hinzu und speichere diese:
    # https://www.guru99.com/de/reading-and-writing-files-in-python.html
# - Füge eine Quizauswahlauswahl hinzu. Dafür musst du auch mit if-Abfragen arbeiten.
    # https://www.python-lernen.de/if-abfrage-python.htm
    # und du musst eine weitere fragenliste, z.B. fragen2, erstellen.
# - Füge eine GUI hinzu:
    # https://ichi.pro/de/erstellen-sie-eine-gui-auf-python-mit-tkinter-from-scratch-schritt-fur-schritt-fur-anfanger-115751015136479
