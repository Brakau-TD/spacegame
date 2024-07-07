class Hauptprogramm:
    def __init__(self):
        self.fragen = {"Wie heisst die Hauptstadt von Deutschland": "Berlin",
          "Wie heisst die Hauptstadt von Italien": "Rom"}
        self.fragenliste = list(self.fragen.keys())
        self.counter = 0
        self.quizlaenge = len(self.fragenliste)
        self.richtig = 0

    def hole_frage_antwort(self):
        if self.counter == self.quizlaenge:
            return False
        frage = self.fragenliste[self.counter]
        return frage
    
    def gebe_auswertung(self):
        return f"Du hast {self.richtig} von {self.quizlaenge} beantwortet!"
    
    def pruefe_antwort(self,antwort):
        if antwort.lower() == self.fragen[self.fragenliste[self.counter]].lower():
            self.counter += 1
            self.richtig += 1
            return "Richtig!"
        else:
            self.counter +=1
            return "Falsch"