import tkinter as tk
import customtkinter as ctk

# Créer une fenêtre Tkinter
fenetre = tk.Tk()

# Créer un cadre (frame) avec CustomTkinter
cadre = ctk.CTkFrame(fenetre, width=200, height=200,
                     corner_radius=10, bg="gray")

# Afficher le cadre
cadre.pack()

# Lancer la boucle principale Tkinter
fenetre.mainloop()
