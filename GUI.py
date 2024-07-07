import tkinter as tk

class GUI:
    def __init__(self):
        # Erstellen Sie das Hauptfenster
        self.root = tk.Tk()

        # Erstellen Sie die Frames mit bestimmter Höhe und Breite
        self.frame1 = tk.Frame(self.root, height=200, width=500)
        self.frame2 = tk.Frame(self.root, height=200, width=500)
        self.frame3 = tk.Frame(self.root, height=200, width=500)

        self.frame1.pack_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.pack_propagate(False)
        # Packen Sie die Frames vertikal
        self.frame1.pack(side=tk.TOP)
        self.frame2.pack(side=tk.TOP)
        self.frame3.pack(side=tk.TOP)

        # Erstellen Sie drei Buttons und fügen Sie sie dem mittleren Frame hinzu
        self.button1 = tk.Button(self.frame2, text="Button 1", command = self.button1)
        self.button2 = tk.Button(self.frame2, text="Button 2", command = self.button2)
        self.button3 = tk.Button(self.frame2, text="Button 3", command = self.button3)

        # Packen Sie die Buttons vertikal im mittleren Frame
        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.LEFT)
        self.button3.pack(side=tk.LEFT)
        
        # Erstellen wir ein paar Textlabel
        self.label_oben = tk.Label(self.frame1, text = "Hallo")
        self.label_unten = tk.Label(self.frame3, text = "Von mir auch Hallo!")
        
        self.label_oben.pack()
        self.label_unten.pack()
        
        self.eingabe = tk.Entry(self.frame3)
        self.eingabe.pack()
    
    def fenster_starten(self):
        # Starten Sie die Tkinter event loop
        self.root.mainloop()
        
    def button1(self):
        text = self.eingabe.get()
        self.label_oben.config(text = text)
        
    
    def button2(self):
        pass
    
    def button3(self):
        pass
    
gui = GUI()
gui.fenster_starten()
