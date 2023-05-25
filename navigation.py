from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import tkinter as tk


def create_page_navigation():
    page_nav = Tk()

    Arcelortext = Image.open(
        "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelortext.jpg")
    arcelorlogo = Image.open(
        "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelor-logo.png")
    ico = "C:/Users/ol08f/Desktop/GMAO/peach_connexion/image/arcelor/arcelor-logo.ico"

    page_nav.title("menu de navigation")
    page_nav.geometry("900x900")
    page_nav.configure(bg="#F08228")
    page_nav.state("zoomed")
    page_nav.iconbitmap(ico)

    arcetext = Arcelortext.resize((400, 400), Image.LANCZOS)
    arcelogo = arcelorlogo.resize((200, 200), Image.LANCZOS)

    image_text = ImageTk.PhotoImage(arcetext)
    font_text = customtkinter.CTkLabel(
        master=page_nav, image=image_text, height=100, width=100, text="", text_color='Blue')
    font_text.pack(side=RIGHT, padx=15, pady=0)

    image_logo = ImageTk.PhotoImage(arcelogo)
    font_logo = customtkinter.CTkLabel(
        master=page_nav, image=image_logo, height=100, width=100, text="", text_color='Blue')
    font_logo.pack(side=RIGHT, padx=15, pady=0)

    # Créer un cadre (frame)
    cadre1 = tk.Frame(page_nav, width=200, height=200, bg="#3CE68B")
    # Afficher le cadre
    cadre1.place(x=1, y=1)

    cadre2 = tk.Frame(page_nav, width=200, height=200, bg="#F26433")
    # Afficher le cadre
    cadre2.place(x=400, y=1)

    cadre3 = tk.Frame(page_nav, width=200, height=200, bg="#4EC8F9")
    # Afficher le cadre
    cadre3.place(x=1, y=400)

    # 9 boutons: info général, qualité et amélioration, fiche de vie, controle périodique et vgp, rapport de maintenance BT,maintenance améliorative, doc tech,inventaire,pièce a commander.

    info_general = Button(master=cadre1, text="info_general",
                          background="#419AFA", font=("COMIC Sans MS", 15, "bold"))
    info_general.grid(row=0, column=0, padx=10, pady=10)

    qualite_amelioration = Button(master=cadre1, text="qualite_amelioration",
                                  background="#419AFA", font=("Arial", 15, "bold"))
    qualite_amelioration.grid(row=0, column=1, padx=10, pady=10)

    fiche_de_vie = Button(master=cadre1, text="fiche_de_vie",
                          background="#419AFA", font=("Arial", 15, "bold"))
    fiche_de_vie.grid(row=1, column=0, padx=10, pady=10)

    controle_periodique = Button(master=cadre2, text="controle_periodique",
                                 background="#419AFA", font=("Arial", 15, "bold"))
    controle_periodique.grid(row=0, column=0, padx=10, pady=10)

    maintenance_BT = Button(master=cadre2, text="rapport de maintenance BT",
                            background="#419AFA", font=("Arial", 15, "bold"))
    maintenance_BT.grid(row=0, column=1, padx=10, pady=10)

    m_ameliorative = Button(master=cadre2, text="maintenance améliorative",
                            background="#419AFA", font=("Arial", 15, "bold"))
    m_ameliorative.grid(row=1, column=0, padx=10, pady=10)

    doc_tech = Button(master=cadre2, text="Documentation technique",
                      background="#419AFA", font=("Arial", 15, "bold"))
    doc_tech.grid(row=1, column=1, padx=10, pady=10)

    inventaire = Button(master=cadre3, text="Inventaire",
                        background="#419AFA", font=("Arial", 15, "bold"))
    inventaire.grid(row=0, column=0, padx=10, pady=10)

    a_commander = Button(master=cadre3, text="Pièce à commander",
                         background="#419AFA", font=("Arial", 15, "bold"))
    a_commander.grid(row=0, column=1, padx=10, pady=10)

    page_nav.mainloop()
