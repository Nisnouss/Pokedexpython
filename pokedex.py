import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

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
menu.place(x=100, y=100)
menu.bind("<Button-1>", Afficher_selection)

options = ["Rondoudou", "Salamèche", "Pikachu"]
for option in options:
    menu.insert(tk.END, option)

# Bouton permettant d'ouvrir une nouvelle fenêtre affichant les informations sur les pokemons
print_button = tk.Button(window, text="Afficher les informations", bg="light blue")
print_button.place(x=100, y=270)
print_button.bind("<Button-1>", Display_infos)

Informations_pokemon = tk.Label(window, text= "Voici les informations sur le pokemon selectionné : ")
Informations_pokemon.place(x=100, y=300)

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
label_name.place(x=360, y=100)

add_pokemon_name = tk.Entry(window)
add_pokemon_name.place(x=520, y=100)

label_type = tk.Label(window, text="Type de Pokemon")
label_type.place(x=360, y=130)

add_pokemon_type = tk.Entry(window)
add_pokemon_type.place(x=520, y=130)

label_ability = tk.Label(window, text="Capacités du Pokemon")
label_ability.place(x=360, y=160)

add_pokemon_ability = tk.Entry(window)
add_pokemon_ability.place(x=520, y=160)

label_strenght = tk.Label(window, text="Force du Pokemon")
label_strenght.place(x=360, y=190)

add_pokemon_strenght = tk.Entry(window)
add_pokemon_strenght.place(x=520, y=190)

btn_add = tk.Button(window, text="Ajoutez un pokemon", bg="light green")
btn_add.place(x=430, y=230)
btn_add.bind("<Button-1>", save_infos)

# Fonctions permettant de modifier ou supprimer
def Delete_menu(self):
    try:
        To_delete = option
        option_to_delete = menu.get(tk.END).index(To_delete)
        menu.delete(option_to_delete)
    except:
        messagebox.showerror("Erreur", "Veuillez selectionner un élément du menu à supprimer.")
        window.quit

def Modify_menu(self):
    try:
        selection = menu.get(menu.curselection())
        print(selection)
        selection[0] = add_pokemon_name.get()
        menu.insert(selection)
    except:
        messagebox.showerror("Erreur", "Veuillez selectionner un élément du menu à modifier.")
        window.quit

# Supprimer ou modifier des pokemons
label_mod_del = tk.Label(window, text="Si vous souhaitez modifier ou supprimer un élément du menu, veuillez cliquer sur le bouton correspondant : ")
label_mod_del.place(x=100, y=360)

btn_modify = tk.Button(window, text="Modifier", bg="yellow")
btn_modify.place(x=305, y=400)
btn_modify.bind("<Button-3>", Modify_menu)

btn_delete = tk.Button(window, text="Supprimer", bg="red")
btn_delete.place(x=370, y=400)
btn_delete.bind("<Button-1>", Delete_menu)

window.mainloop()