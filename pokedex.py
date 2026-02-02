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

# Ouverture de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Projet d'évaluation - Pokedex")
fenetre.geometry("720x480")

# Afficher les informations des pokemons sur une autre fenêtre ainsi que leur photo
def Afficher_infos(event):
    fenetre_infos = tk.Toplevel()
    fenetre_infos.geometry("820x580")
    fenetre_infos.title("Infos sur les pokemon")
    label_infos = tk.Label(fenetre_infos)
    try:
        selection = menu.get(menu.curselection())
        print(selection)
        if selection == "Rondoudou":
            Rondoudouimg_label = tk.Label(fenetre_infos, image=Rondoudouimg)
            Rondoudouimg_label.pack()
            label_infos.config(text=f"{Pokemon1.name} est de type {Pokemon1.type}, a pour capacité le pouvoir de {Pokemon1.ability}, et a {Pokemon1.strenght} XP de force")
        elif selection == "Salamèche":
            Salamecheimg_label = tk.Label(fenetre_infos, image=Salamecheimg)
            Salamecheimg_label.pack()
            label_infos.config(text=f"{Pokemon2.name} est de type {Pokemon2.type}, a pour capacité le pouvoir de {Pokemon2.ability}, et a {Pokemon2.strenght} XP de force")
        elif selection == "Pikachu":
            Pikachuimg_label = tk.Label(fenetre_infos, image=Pikachuimg)
            Pikachuimg_label.pack()
            label_infos.config(text=f"{Pokemon3.name} est de type {Pokemon3.type}, a pour capacité le pouvoir de l'{Pokemon3.ability}, et a {Pokemon3.strenght} XP de force")
    except:
        Informations_pokemon.config(text="Veuillez selectionner un pokemon")
    label_infos.pack()

# Informations liées aux attributs:
Pokemon1 = Pokemon("Rondoudou", "normal", "berceuse", 30)
Pokemon2 = Pokemon("Salamèche", "normal", "feu", 60)
Pokemon3 = Pokemon("Pikachu", "Electrik", "éclair", 100)

# Images de pokemon
Rondoudouimg = ImageTk.PhotoImage(Image.open("rondoudou.png"))
Salamecheimg = ImageTk.PhotoImage(Image.open("salameche.png"))
Pikachuimg = ImageTk.PhotoImage(Image.open("pikatchu.png"))

# Afficher les selections en cliquant sur les éléments de liste
def Afficher_selection(event):
    try:
        selection = menu.get(menu.curselection())
        print(selection)
        if selection == "Rondoudou":
            Pokemon1.Afficher_infos()
        elif selection == "Salamèche":
            Pokemon2.Afficher_infos()
        elif selection == "Pikachu":
            Pokemon3.Afficher_infos
    except:
        Informations_pokemon.config(text="Veuillez selectionner un pokemon")

# Création du menu déroulant qui va répertorier les informations des pokemon
menu = tk.Listbox(fenetre, selectmode=tk.SINGLE)
menu.pack()
menu.bind("<Button-1>", Afficher_selection)

options = ["Rondoudou", "Salamèche", "Pikachu"]
for option in options:
    menu.insert(tk.END, option)

# Bouton permettant d'ouvrir une nouvelle fenêtre affichant les informations sur les pokemons
print_button = tk.Button(fenetre, text="Afficher les informations", command=Afficher_infos)
print_button.pack()
print_button.bind("<Button-1>", Afficher_infos)

Informations_pokemon = tk.Label(fenetre, text= "Voici les informations sur le pokemon selectionné : ")
Informations_pokemon.pack()

# Ajout d'un pokemon au menu
def save_infos(event):
    fenetre_infos = tk.Toplevel()
    fenetre_infos.geometry("820x580")
    fenetre_infos.title("Infos sur les pokemon")
    label_save = tk.Label(fenetre_infos)
    if ajout_pokemon_name.get():
        with open("name.txt", "a") as f:
            menu.insert(tk.END, ajout_pokemon_name.get()+ "\n")
    elif ajout_pokemon_type.get():
        with open("name.txt", "a") as f:
            info1 = f.write(ajout_pokemon_type.get()+ "\n")
            label_save.config(text=f"Il est de type : {info1}")
    elif ajout_pokemon_ability.get():
        with open("name.txt", "a") as f:
            f.write(ajout_pokemon_ability.get()+ "\n")
    elif ajout_pokemon_strenght.get():
        with open("name.txt", "a") as f:
            f.write(ajout_pokemon_strenght.get()+ "\n")
    label_save.pack()

label_name = tk.Label(fenetre, text="Nom du Pokemon")
label_name.pack()

ajout_pokemon_name = tk.Entry(fenetre)
ajout_pokemon_name.pack()

label_type = tk.Label(fenetre, text="Type de Pokemon")
label_type.pack()

ajout_pokemon_type = tk.Entry(fenetre)
ajout_pokemon_type.pack()

label_ability = tk.Label(fenetre, text="Capacitées du Pokemon")
label_ability.pack()

ajout_pokemon_ability = tk.Entry(fenetre)
ajout_pokemon_ability.pack()

label_strenght = tk.Label(fenetre, text="Force du Pokemon")
label_strenght.pack()

ajout_pokemon_strenght = tk.Entry(fenetre)
ajout_pokemon_strenght.pack()

btn_ajout = tk.Button(fenetre, text="Ajoutez un pokemon")
btn_ajout.pack()
btn_ajout.bind("<Button-1>", save_infos)

fenetre.mainloop()