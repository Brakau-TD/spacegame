# Eine Liste von Fragen und Antworten
quiz = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "antwort": "Berlin"
    },
    {
        "frage": "Wie viele Bundesländer hat Deutschland?",
        "antwort": "16"
    },
    {
        "frage": "Welcher Fluss fließt durch Berlin?",
        "antwort": "Spree"
    }
]

# Durchlaufe jede Frage im Quiz
for i in range(len(quiz)):
    # Stelle die Frage
    antwort = input(quiz[i]["frage"] + " ")

    # Überprüfe die Antwort
    if antwort.lower() == quiz[i]["antwort"].lower():
        print("Richtig!")
    else:
        print("Falsch. Die richtige Antwort ist", quiz[i]["antwort"])

print("Das Quiz ist vorbei. Danke fürs Mitmachen!")