import tkinter as tk

# Mise en place d'une classe pour répertorier les variables ainsi que leurs attributs

class Pokemon:
    def __init__(self, nom, type, capacité, force):
        self.name = nom
        self.type = type
        self.ability = capacité
        self.strenght = force

fenetre = tk.Tk()
fenetre.title("Projet d'évaluation - Pokedex")
fenetre.geometry("720x480")

# Informations liées aux attributs:

Pokemon1 = Pokemon("Rondoudou", "normal", "berceuse", 30)
Pokemon2 = Pokemon("Salamèche", "normal", "feu", 60)
Pokemon3 = Pokemon("Pikachu", "Electrik", "éclair", 100)

# Création du menu déroulant qui va répertorier les informations des pokemon

menu = tk.Listbox(fenetre)
menu.pack()

menu.insert(tk.END)
menu.insert(tk.END)
menu.insert(tk.END)



fenetre.mainloop()