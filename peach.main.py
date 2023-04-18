from tkinter import *
from PIL import ImageTk, Image
import messagebox
import customtkinter
import tkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


peach_connection = customtkinter.CTk()

peach_connection.title('Peach connexion ')
peach_connection.geometry("500x500")
peach_connection.configure(bg="blue")
peach_connection.title('Devis')


resize_IG = Image.open("manga_women.jpeg")
resize_ID = Image.open("marche.jpeg")
resize_IF = Image.open("woomen drag.jpg")

marche = resize_IG.resize((500, 800), Image.LANCZOS)
manga_women = resize_ID.resize((500, 800), Image.LANCZOS)
woomen_drag = resize_IF.resize((500, 800), Image.LANCZOS)

image_de_fond = ImageTk.PhotoImage(woomen_drag)
font = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_fond, height=100, width=100, text="", text_color='Blue')
font.pack(side=LEFT, padx=15, pady=0)

image_de_droite = ImageTk.PhotoImage(marche)
font_droite = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_droite, height=100, width=100, text="", text_color="blue")
font_droite.pack(side=LEFT, padx=15, pady=0)

image_de_gauche = ImageTk.PhotoImage(manga_women)
font_gauche = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_gauche, height=100, width=100, text="", text_color="blue")
font_gauche.pack(side=LEFT, padx=15, pady=0)


peach_connection.mainloop()
