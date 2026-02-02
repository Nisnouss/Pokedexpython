import tkinter as tk
from PIL import ImageTk, Image

# Mise en place d'une classe pour répertorier les variables ainsi que leurs attributs

class Pokemon:
    def __init__(self, nom, type, capacité, force):
        self.name = nom
        self.type = type
        self.ability = capacité
        self.strenght = force

    def Afficher_infos(self):
        print(f"Nom : {self.name}")
        print(f"Type : {self.type}")
        print(f"Capacité : {self.ability}")
        print(f"Force : {self.strenght}")

fenetre = tk.Tk()
fenetre.title("Projet d'évaluation - Pokedex")
fenetre.geometry("720x480")

# Informations liées aux attributs:

Pokemon1 = Pokemon("Rondoudou", "normal", "berceuse", 30)
Pokemon2 = Pokemon("Salamèche", "normal", "feu", 60)
Pokemon3 = Pokemon("Pikachu", "Electrik", "éclair", 100)
Rondoudouimg = ImageTk.PhotoImage(Image.open("rondoudou.png"))
Salamecheimg = ImageTk.PhotoImage(Image.open("salameche.png"))
Pikachuimg = ImageTk.PhotoImage(Image.open("pikatchu.png"))

def Afficher_selection(event):
    try:
        selection = menu.get(menu.curselection())
        print(selection)
        if selection == "Rondoudou":
            Affich1 = Pokemon1.Afficher_infos()
            Informations_pokemon.config(text=f"Voici les informations sur le pokemon selectionné:{Affich1}")
        elif selection == "Salamèche":
            Affich2 = Pokemon2.Afficher_infos()
            Informations_pokemon.config(text=f"Voici les informations sur le pokemon selectionné:{Affich2}")
        elif selection == "Pikachu":
            Affich3 = Pokemon3.Afficher_infos()
            Informations_pokemon.config(text=f"Voici les informations sur le pokemon selectionné:{Affich3}")
    except:
        Informations_pokemon.config(text="Veuillez selectionner un pokemon")

# Création du menu déroulant qui va répertorier les informations des pokemon

menu = tk.Listbox(fenetre, selectmode=tk.SINGLE)
menu.pack()
menu.bind("<Button-1>", Afficher_selection)

options = ["Rondoudou", "Salamèche", "Pikachu"]
for option in options:
    menu.insert(tk.END, option)

#print_button = tk.Button(fenetre, text="Afficher les informations")
#print_button.pack()
#print_button.bind("<Button-1>", Afficher_selection)

Informations_pokemon = tk.Label(fenetre, text= "Voici les informations sur le pokemon selectionné : ")
Informations_pokemon.pack()



fenetre.mainloop()