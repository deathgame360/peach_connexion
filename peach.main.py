from tkinter import *
from PIL import ImageTk, Image
import messagebox
import customtkinter
import tkinter

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("green")


peach_connection = customtkinter.CTk()

peach_connection.title('Peach connexion ')
peach_connection.geometry("500x500")
peach_connection.configure(bg="blue")
peach_connection.title('Devis')


image_de_fond = ImageTk.PhotoImage(Image.open("woomen drag.jpg"))
font = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_fond)
font.pack(side=LEFT)

image_de_droite = ImageTk.PhotoImage(Image.open("marche.jpeg"))
font_droite = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_droite)

font_droite.pack()

image_de_gauche = ImageTk.PhotoImage(Image.open("manga_women.jpeg"))
font_gauche = customtkinter.CTkLabel(
    master=peach_connection, image=image_de_gauche)
font_gauche.pack(side=RIGHT)


peach_connection.mainloop()
