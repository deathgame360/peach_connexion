from tkinter import *
import csv


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

        # Fermer la fenêtre d'inscription
        account_window.destroy()

    # Ajouter un bouton "S'inscrire"
    register_button = Button(
        account_window, text="S'inscrire", command=register)
    register_button.grid(row=2, column=1)


# Créer la fenêtre de connexion
peach_connection = Tk()
peach_connection.title("Peach Connexion")
# Ajouter un bouton "Créer un compte"
create_account_button = Button(
    peach_connection, text="Créer un compte", command=create_account_window)
create_account_button.pack()

# Ajouter les autres éléments de l'interface
# ...

peach_connection.mainloop()
