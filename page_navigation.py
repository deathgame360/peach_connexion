from tkinter import *
from PIL import ImageTk, Image
import customtkinter

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


# 9 boutons: info général, qualité et amélioration, fiche de vie, controle périodique et vgp, rapport de maintenance BT,maintenance améliorative, doc tech,inventaire,pièce a commander.

info_general = Button(text="info_general",
                      background="#419AFA", font=("Arial", 12))
info_general.pack(padx=4, pady=4)

qualite_amelioration = Button(
    text="qualite_amelioration", background="#419AFA")
qualite_amelioration.pack(padx=4, pady=4)

fiche_de_vie = Button(text="fiche_de_vie", background="#419AFA")
fiche_de_vie.pack(padx=4, pady=4)

controle_periodique = Button(text="controle_periodique", background="#419AFA")
controle_periodique.pack(padx=4, pady=4)

maintenance_BT = Button(text="rapport de maintenance BT", background="#419AFA")
maintenance_BT.pack(padx=4, pady=4)

m_ameliorative = Button(text="maintenance améliorative", background="#419AFA")
m_ameliorative.pack(padx=4, pady=4)

doc_tech = Button(text="Documentation technique", background="#419AFA")
doc_tech.pack(padx=4, pady=4)

inventaire = Button(text="Inventaire", background="#419AFA")
inventaire.pack(padx=4, pady=4)

a_commander = Button(text="Pièce à commander", background="#419AFA")
a_commander.pack(padx=4, pady=4)


page_navigation.mainloop()
