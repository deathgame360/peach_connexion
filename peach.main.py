from tkinter import *
from PIL import ImageTk , Image
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

image_de_fond = ImageTk.PhotoImage(Image.open("manga_marché.jpeg"))
font = customtkinter.CTkLabel(master=peach_connection, image=image_de_fond, text="heart beam")
font.pack(fill='both')

image_de_droite=ImageTk.PhotoImage(Image.open("manga_women.jpeg"))
font_droite=customtkinter.CTkLabel(master=peach_connection, image=image_de_droite, texte=None)
font_droite.pack(fill='right')

image_de_gauche=ImageTk.PhotoImage(Image.open("woomen drag.jpg"))
font_gauche=customtkinter.CTkLabel(master=peach_connection, image=image_de_gauche, texte=None)
font_gauche.pack(fill='left')




peach_connection.mainloop()
