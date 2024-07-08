import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.font = ("Helvetica",16)
        
        # Frame
        self.frame1 = tk.Frame(self.root, height=200, width=500)
        self.frame2 = tk.Frame(self.root, height=200, width=500)
        self.frame3 = tk.Frame(self.root, height=200, width=500)
        
        self.frame1.pack_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.pack_propagate(False)
        
        self.frame1.pack(side = tk.TOP)
        self.frame2.pack(side = tk.TOP)
        self.frame3.pack(side = tk.TOP)
        
        # Buttons
        self.eingabebutton = tk.Button(self.frame2, text = "Eingabe", command = self.eingabe)
        self.eingabebutton.pack(side = tk.LEFT)
        
        self.startbutton = tk.Button(self.frame2, text = "Start", command = self.start)
        self.startbutton.pack(side = tk.LEFT)
        
        # Eingabefeld
        self.eingabefeld = tk.Entry(self.frame3)
        self.eingabefeld.pack()
        
        # Label
        self.label_oben = tk.Label(self.frame1, text = "Hallo, willkommen zum Quiz", font = self.font)
        self.label_unten = tk.Label(self.frame3, text = "Ob du richtig liegst oder nicht, \nsagt dieses Feld ganz schlicht", font = self.font)
        self.label_oben.pack()
        self.label_unten.pack()
        
    
    def eingabe(self):
        antwort = self.eingabefeld.get().lower()
        # -> Rom -> rom
        if antwort == "rom":
            self.label_unten.config(text = "Richtig!")
        else:
            self.label_unten.config(text = "Falsch!")
    
    def start(self):
        self.label_oben.config(text = "Wie heißt die Hauptstadt von Italien?")
        

gui = GUI()