import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess


def executer_fichier():
    chemin_fichier = r"C:\Users\ol08f\Desktop\GMAO\peach_connexion\test\commande python.py"
    subprocess.call(['python', chemin_fichier])


mapp = Tk()

mapp.title("Information du personnel")
mapp.state("zoomed")

# définir que la page soit a la taille de l'écran


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry(
            "{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


# définir une fenètre:
Info_personnel = Frame(mapp)
Info_personnel.pack(side=tk.LEFT, padx=20)

Tableau = ttk.Treeview(mapp, columns=(1, 2, 3), show="headings", height="5")
Tableau.pack()

Tableau.heading(1, text="Nom")
Tableau.heading(2, text="Prénom")
Tableau.heading(3, text="mail")

bouton = Button(text="script", command=executer_fichier)
bouton.pack()


app = FullScreenApp(master=mapp)
mapp.mainloop()
