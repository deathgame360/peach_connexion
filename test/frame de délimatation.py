import tkinter as tk

# Créer une fenêtre Tkinter
fenetre = tk.Tk()

# Créer un cadre (frame)
cadre = tk.Frame(fenetre, width=200, height=200, bg="gray")

# Afficher le cadre
cadre.pack()

# Lancer la boucle principale Tkinter
fenetre.mainloop()
