import tkinter as tk
from PIL import ImageTk, Image

# Mise en place d'une classe pour répertorier les variables ainsi que leurs attributs
class Pokedex:
    def __init__(self, name, type, ability, strenght):
        self.name = name
        self.type = type
        self.ability = ability
        self.strenght = strenght

    def Display_infos_pokemon(self):
        print(f"Nom : {self.name}")
        print(f"Type : {self.type}")
        print(f"Capacité : {self.ability}")
        print(f"Force : {self.strenght}")

# Ouverture de la fenêtre principale
window = tk.Tk()
window.title("Projet d'évaluation - Pokedex")
window.geometry("720x480")

# Afficher les informations des pokemons sur une autre fenêtre ainsi que leur photo
def Display_infos(event):
    window_info = tk.Toplevel()
    window_info.geometry("820x580")
    window_info.title("Infos sur les pokemon")
    label_infos = tk.Label(window_info)
    try:
        selection = menu.get(menu.curselection())
        print(selection)
        if selection == "Rondoudou":
            Rondoudouimg_label = tk.Label(window_info, image=Rondoudouimg)
            Rondoudouimg_label.pack()
            label_infos.config(text=f"{Pokemon1.name} est de type {Pokemon1.type}, a pour capacité le pouvoir de la {Pokemon1.ability}, et a {Pokemon1.strenght} XP de force")
        elif selection == "Salamèche":
            Salamecheimg_label = tk.Label(window_info, image=Salamecheimg)
            Salamecheimg_label.pack()
            label_infos.config(text=f"{Pokemon2.name} est de type {Pokemon2.type}, a pour capacité le pouvoir du {Pokemon2.ability}, et a {Pokemon2.strenght} XP de force")
        elif selection == "Pikachu":
            Pikachuimg_label = tk.Label(window_info, image=Pikachuimg)
            Pikachuimg_label.pack()
            label_infos.config(text=f"{Pokemon3.name} est de type {Pokemon3.type}, a pour capacité le pouvoir de l'{Pokemon3.ability}, et a {Pokemon3.strenght} XP de force")
    except:
        Informations_pokemon.config(text="Veuillez selectionner un pokemon")
    label_infos.pack()

# Informations liées aux attributs:
Pokemon1 = Pokedex("Rondoudou", "normal", "berceuse", 30)
Pokemon2 = Pokedex("Salamèche", "normal", "feu", 60)
Pokemon3 = Pokedex("Pikachu", "Electrik", "éclair", 100)

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
            Pokemon1.Display_infos_pokemon()
        elif selection == "Salamèche":
            Pokemon2.Display_infos_pokemon()
        elif selection == "Pikachu":
            Pokemon3.Display_infos_pokemon()
    except:
        Informations_pokemon.config(text="Veuillez selectionner un pokemon")

# Création du menu déroulant qui va répertorier les informations des pokemon
menu = tk.Listbox(window, selectmode=tk.SINGLE)
menu.pack()
menu.bind("<Button-1>", Afficher_selection)

options = ["Rondoudou", "Salamèche", "Pikachu"]
for option in options:
    menu.insert(tk.END, option)

# Bouton permettant d'ouvrir une nouvelle fenêtre affichant les informations sur les pokemons
print_button = tk.Button(window, text="Afficher les informations", command=Display_infos)
print_button.pack()
print_button.bind("<Button-1>", Display_infos)

Informations_pokemon = tk.Label(window, text= "Voici les informations sur le pokemon selectionné : ")
Informations_pokemon.pack()

# Ajout d'un pokemon au menu
def save_infos(event):
    window_infos = tk.Toplevel()
    window_infos.geometry("820x580")
    window_infos.title("Infos sur les pokemon")
    label_save = tk.Label(window_infos)
    with open("NewPokemon.txt", "a", encoding="utf-8") as file:
        menu.insert(tk.END, add_pokemon_name.get()+ "\n")
        label_save.config(text=f"Le nom du Pokemon est : {add_pokemon_name.get()}. Il est de type : {add_pokemon_type.get()}, ses capacités sont : {add_pokemon_ability.get()}, et sa force est de {add_pokemon_strenght.get()}")
        txt = f"Nom: {add_pokemon_name.get()}, Type: {add_pokemon_type.get()}, Capacité: {add_pokemon_ability.get()}, Force: {add_pokemon_strenght.get()}"
        x = txt.split(" ,")
        file.write(f"{x}")
        print(x)
        file.close()
    label_save.pack()

# Formulaire d'ajout de pokemon
label_name = tk.Label(window, text="Nom du Pokemon")
label_name.pack()

add_pokemon_name = tk.Entry(window)
add_pokemon_name.pack()

label_type = tk.Label(window, text="Type de Pokemon")
label_type.pack()

add_pokemon_type = tk.Entry(window)
add_pokemon_type.pack()

label_ability = tk.Label(window, text="Capacités du Pokemon")
label_ability.pack()

add_pokemon_ability = tk.Entry(window)
add_pokemon_ability.pack()

label_strenght = tk.Label(window, text="Force du Pokemon")
label_strenght.pack()

add_pokemon_strenght = tk.Entry(window)
add_pokemon_strenght.pack()

btn_add = tk.Button(window, text="Ajoutez un pokemon")
btn_add.pack()
btn_add.bind("<Button-1>", save_infos)

window.mainloop()