from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter as tk

page_navigation = Tk()

Arcelortext = Image.open(
    "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelortext.jpg")
arcelorlogo = Image.open(
    "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelor-logo.png")
ico = "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelor-logo.ico"

page_navigation.title("menu de navigation")
page_navigation.geometry("900x900")
page_navigation.configure(bg="#F08228")
page_navigation.state("zoomed")
page_navigation.iconbitmap(ico)

arcetext = Arcelortext.resize((400, 400), Image.LANCZOS)
arcelogo = arcelorlogo.resize((200, 200), Image.LANCZOS)

image_text = ImageTk.PhotoImage(arcetext)
font_text = customtkinter.CTkLabel(
    master=page_navigation, image=image_text, height=100, width=100, text="", text_color='Blue')
font_text.pack(side=RIGHT, padx=15, pady=0)

image_logo = ImageTk.PhotoImage(arcelogo)
font_logo = customtkinter.CTkLabel(
    master=page_navigation, image=image_logo, height=100, width=100, text="", text_color='Blue')
font_logo.pack(side=RIGHT, padx=15, pady=0)

# Créer un cadre (frame)
cadre1 = tk.Frame(page_navigation, width=200, height=200, bg="#3CE68B")
# Afficher le cadre
cadre1.place()
# Créer un cadre (frame)

cadre2 = tk.Frame(page_navigation, width=200, height=200, bg="#F26433")
# Afficher le cadre
cadre2.place()  # Créer un cadre (frame)

cadre3 = tk.Frame(page_navigation, width=200, height=200, bg="#FCF074")
# Afficher le cadre
cadre3.place()
# 9 boutons: info général, qualité et amélioration, fiche de vie, controle périodique et vgp, rapport de maintenance BT,maintenance améliorative, doc tech,inventaire,pièce a commander.

info_general = Button(master=cadre, text="info_general",
                      background="#419AFA", font=("COMIC Sans MS", 15, "bold"))
info_general.place()

qualite_amelioration = Button(
    master=cadre, text="qualite_amelioration", background="#419AFA", font=("Arial", 15, "bold"))
qualite_amelioration.place()

fiche_de_vie = Button(master=cadre, text="fiche_de_vie",
                      background="#419AFA", font=("Arial", 15, "bold"))
fiche_de_vie.place()

controle_periodique = Button(master=cadre2,
                             text="controle_periodique", background="#419AFA", font=("Arial", 15, "bold"))
controle_periodique.place()

maintenance_BT = Button(master=cadre2, text="rapport de maintenance BT",
                        background="#419AFA", font=("Arial", 15, "bold"))
maintenance_BT.place()

m_ameliorative = Button(master=cadre2, text="maintenance améliorative",
                        background="#419AFA", font=("Arial", 15, "bold"))
m_ameliorative.place()

doc_tech = Button(master=cadre2, text="Documentation technique",
                  background="#419AFA", font=("Arial", 15, "bold"))
doc_tech.place()

inventaire = Button(master=cadre3, text="Inventaire", background="#419AFA",
                    font=("Arial", 15, "bold"))
inventaire.place()

a_commander = Button(master=cadre3, text="Pièce à commander",
                     background="#419AFA", font=("Arial", 15, "bold"))


a_commander.place()


page_navigation.mainloop()
