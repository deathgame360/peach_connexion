from tkinter import *
from PIL import ImageTk, Image
import messagebox
import customtkinter
import tkinter
import csv


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


peach_connection = customtkinter.CTk()

peach_connection.title('Peach connexion ')
peach_connection.geometry("900x900")
peach_connection.configure(bg="blue")
peach_connection.title('Connexion')


resize_IG = Image.open("manga_women.jpeg")
resize_ID = Image.open("marche.jpeg")
resize_IF = Image.open("woomen drag.jpg")
resize_MM = Image.open("manga_marché.jpeg")

marche = resize_IG.resize((600, 900), Image.LANCZOS)
manga_women = resize_ID.resize((200, 400), Image.LANCZOS)
woomen_drag = resize_IF.resize((600, 900), Image.LANCZOS)
manga_marché = resize_MM.resize((200, 400), Image.LANCZOS)


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


def create_account_window():
    # Créer une nouvelle fenêtre
    account_window = Toplevel()
    account_window.title("Créer un compte")

    # Ajouter des champs de saisie pour l'utilisateur et le mot de passe
    Label(account_window, text="Nom d'utilisateur").grid(row=0, column=0)
    username_entry = Entry(account_window)
    username_entry.grid(row=0, column=1)

    Label(account_window, text="Mot de passe").grid(row=1, column=0)
    password_entry = Entry(account_window, show="*")
    password_entry.grid(row=1, column=1)

    # Fonction liée au bouton "S'inscrire"
    def register():
        # Récupérer les valeurs des champs de saisie
        username = username_entry.get()
        password = password_entry.get()

        # Stocker les valeurs dans un fichier CSV
        with open("users.csv", mode="a") as users_file:
            writer = csv.writer(users_file)
            writer.writerow([username, password])

    # Ajouter un bouton "S'inscrire"
    register_button = Button(
        account_window, text="S'inscrire", command=register)
    register_button.grid(row=2, column=1)


image_de_fond = ImageTk.PhotoImage(woomen_drag)
font = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_fond, height=100, width=100, text="", text_color='Blue')
font.pack(side=LEFT, padx=15, pady=0)

image_de_droite = ImageTk.PhotoImage(marche)
font_droite = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_droite, height=100, width=100, text="", text_color="blue")
font_droite.pack(side=RIGHT, padx=15, pady=0)

image_de_droite_2 = ImageTk.PhotoImage(manga_marché)
font_droite = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_droite_2, height=100, width=100, text="", text_color="blue")
font_droite.pack(side=TOP, padx=15, pady=0)

image_de_gauche = ImageTk.PhotoImage(manga_women)
font_gauche = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_gauche, height=100, width=100, text="", text_color="blue")
font_gauche.pack(side=BOTTOM, padx=15, pady=0)


frame_connexion = customtkinter.CTkFrame(
    master=peach_connection, width=800, height=800, corner_radius=100)
frame_connexion.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

connexion = customtkinter.CTkLabel(
    master=frame_connexion, text="Connexion", font=("Strike", 24))
connexion.pack(pady=12, padx=10)  # place(x=150, y=45)

Utilisateur = customtkinter.CTkEntry(
    master=frame_connexion, placeholder_text="Utilisateur")
Utilisateur.pack(pady=12, padx=10)  # place(x=150, y=100)

Mot_de_passe = customtkinter.CTkEntry(
    master=frame_connexion, placeholder_text="Mot de passe", show='*')
Mot_de_passe.pack(pady=12, padx=10)  # place(x=150, y=200)


bouton = customtkinter.CTkButton(
    master=frame_connexion, text="Connexion")
bouton.pack(pady=12, padx=10, side=LEFT)

bouton = customtkinter.CTkButton(
    master=frame_connexion, text="créer un compte", command=create_account_window)
bouton.pack(pady=12, padx=10, side=LEFT)

# checkbox = customtkinter.CTkCheckBox(
#    master=frame_connexion, text="Se souvenir de moi")
# checkbox.pack(pady=12, padx=10, side=BOTTOM)

# bouton = customtkinter.CTkLabel(
#    master=frame_connexion, text="mot de passe oublé", font=('Century Gothic', 12))
# bouton.pack(pady=12, padx=10, side=BOTTOM)

app = FullScreenApp(master=peach_connection)
peach_connection.mainloop()
