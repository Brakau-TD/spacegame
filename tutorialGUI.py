import tkinter as tk
from tutorialLogik import Hauptprogramm

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.hp = Hauptprogramm()
        
        self.font = ("Helvetica", 16)
        
        # Frames sind rechteckige Plätze im Programmfenster
        # sie können mit allen möglichen GUI-Elementen gefüllt werden
        self.frame1 = tk.Frame(self.root, height=200, width=500)
        self.frame2 = tk.Frame(self.root, height=200, width=500)
        self.frame3 = tk.Frame(self.root, height=200, width=500)
        
        self.frame1.pack_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.pack_propagate(False)
        
        self.frame1.pack(side = tk.TOP)
        self.frame2.pack(side = tk.TOP)
        self.frame3.pack(side = tk.TOP)
        
        # Buttons sind das, wonach es sich anhört, es sind Knöpfe, mit denen
        # man bestimmte Funktionen aufrufen kann
        self.start = tk.Button(self.frame2, text="start", command = self.start)        
        self.eingabe_button = tk.Button(self.frame2, text = "Eingabe", command = self.eingabe)
        
        self.eingabe_button.pack(side = tk.LEFT)
        self.start.pack(side = tk.LEFT)
        
        # Label enthalten Textelemente
        self.label_oben = tk.Label(self.frame1, text = "Hallo Welt!", font = self.font)
        self.label_unten = tk.Label(self.frame3, text = "Huhu", font = self.font)
        
        self.label_oben.pack()
        self.label_unten.pack()
        
        # Entry-Felder sind Eingabe-Felder für Text
        self.eingabe_feld = tk.Entry(self.frame3)
        self.eingabe_feld.pack()
        
    def labeltext_aendern(self,fragentext):
        self.label_oben.config(text = fragentext, font = self.font)
    
    def eingabe(self):
        usertext = self.eingabe_feld.get()
        bestaetigung = self.hp.pruefe_antwort(usertext)
        self.label_unten.config(text = bestaetigung)
        self.eingabe_feld.delete(0,"end")
        self.stelle_frage()
    
    def start(self):
        self.labeltext_aendern("")
        self.stelle_frage()
        
    def stelle_frage(self):
        frage = self.hp.hole_frage_antwort()
        if frage == False:
            self.auswertung()
        else:
            self.labeltext_aendern(frage)
        
    def auswertung(self):
        ausgabetext = self.hp.gebe_auswertung()
        self.labeltext_aendern(ausgabetext)       

gui = GUI()