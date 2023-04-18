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
resize_MM = Image.open("manga_marché.jpeg")

marche = resize_IG.resize((600, 900), Image.LANCZOS)
manga_women = resize_ID.resize((200, 400), Image.LANCZOS)
woomen_drag = resize_IF.resize((600, 900), Image.LANCZOS)
manga_marché = resize_MM.resize((200, 400), Image.LANCZOS)

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
    master=peach_connection, width=320, height=380, corner_radius=100)
frame_connexion.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


peach_connection.mainloop()
