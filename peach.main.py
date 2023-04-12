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

image_de_fond = ImageTk.PhotoImage(Image.open(""))
l1 = customtkinter.CTkLabel(master=peach_connection , image = image_de_fond)
l1.pack(fill='both')


peach_connection.mainloop()
