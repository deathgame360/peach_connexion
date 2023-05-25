from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import customtkinter
import tkinter
import csv
import subprocess

# Importer la fonction run_second_script depuis votre deuxième script
from navigation import page_navigation

def on_connect_button_click():
    # Appeler la fonction run_second_script lorsque le bouton de connexion est actionné
    page_navigation()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


peach_connection = customtkinter.CTk()

moncone = "C:\\Users\\ol08f\\Desktop\\GMAO\\peach_connexion\\image\\ordi.ico"

peach_connection.title('Peach connexion ')
peach_connection.geometry("900x900")
peach_connection.configure(bg="blue")
peach_connection.title('Connexion')
peach_connection.iconbitmap(moncone)


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



# Définir les images


resize_IG = Image.open("manga_women.jpeg")
resize_ID = Image.open("marche.jpeg")
resize_IF = Image.open("woomen drag.jpg")
resize_MM = Image.open("manga_marché.jpeg")

marche = resize_IG.resize((600, 900), Image.LANCZOS)
manga_women = resize_ID.resize((200, 400), Image.LANCZOS)
woomen_drag = resize_IF.resize((600, 900), Image.LANCZOS)
manga_marché = resize_MM.resize((200, 400), Image.LANCZOS)

# fonctions


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


def open_success_window():
    # Créer une nouvelle fenêtre pour afficher le message de connexion réussie
    success_window = Toplevel(peach_connection)
    success_window.title("Connexion réussie")
    success_window.geometry("200x200")
    success_window.iconbitmap(moncone)

    # Créer un label avec le message de connexion réussie
    label = Label(success_window, text="Connexion réussie")
    label.pack()

    # Exécuter un script Python
    chemin_fichier = r"C:\Users\ol08f\Desktop\GMAO\peach_connexion\2page_navigation.py"
    subprocess.call(['python', chemin_fichier])


def Connexion():
    # Ouvrir le fichier CSV contenant les noms d'utilisateur et les mots de passe
    with open("users.csv", mode="r") as users_file:
        reader = csv.reader(users_file)

        # Récupérer les valeurs des champs de saisie
        username = Utilisateur.get()
        password = Mot_de_passe.get()

        # Vérifier si les informations de connexion sont valides
        for row in reader:
            if username == row[0] and password == row[1]:
                messagebox.showinfo("Succès", "Connexion réussie")
                open_success_window()
                peach_connection.destroy()
                return
            chemin_fichier = r"C:\Users\ol08f\Desktop\GMAO\peach_connexion\2page_navigation.py"
            subprocess.call(['python', chemin_fichier])

        # Si les informations de connexion ne sont pas valides, afficher un message d'erreur
        messagebox.showerror(
            "Erreur", "Nom d'utilisateur ou mot de passe incorrect")

# dispositions des images avec affichage


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

# création de la partie centrale de la fenêtre

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

# création des boutons

bouton = customtkinter.CTkButton(
    master=frame_connexion, text="Connexion", command=Connexion)
bouton.pack(pady=12, padx=10, side=LEFT)

bouton = customtkinter.CTkButton(
    master=frame_connexion, text="créer un compte", command=create_account_window)
bouton.pack(pady=12, padx=10, side=LEFT)

# Créez le bouton Quitter
bouton_quitter = customtkinter.CTkButton(
    master=peach_connection, text="Quitter", command=peach_connection.destroy
)
bouton_quitter.pack(side=BOTTOM, padx=20, pady=12)
bouton_quitter.place(x=735, y=520)


app = FullScreenApp(master=peach_connection)
peach_connection.mainloop()
