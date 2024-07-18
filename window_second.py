# IMPORTACION DE LIBRERIAS NECESARIAS

import customtkinter as ctk # PARA CREAR GUI 
from PIL import Image # PARA PODER MOSTRAR LA IMAGEN 
import requests # USO DE API 
from io import BytesIO # ALMACENA IMAGEN 
import json # PARA LEER ARCHIVOS JSON
from pathlib import Path # OBTENER DIRECCION 

# FUNCIONES QUE OBTIENEN LA INFORMACION DE LOS POKEMON

def get_type(dic): 

    # Obtiene los tipos de un Pokémon
    
    type = []

    for x in dic:
        type.append(x['type']['name'])

    return type

def get_stats(dic):

    # Obtiene las estadísticas base de un Pokémon
    
    stats = []

    for x in dic:
        stats.append(x['base_stat'])

    return stats

def get_abilitis(dic):

    # Obtiene las habilidades de un Pokémon

    abilitis = []

    for x in dic:
        abilitis.append(x['ability']['name'])
    
    return abilitis

def get_moves(dir):

    # Obtiene las habilidades de un Pokémon

    move = []
    if len(dir) > 1:
        for x in range(0,3):     
            move.append(dir[x]['move']['name'])
    else:
         move.append(dir[0]['move']['name'])
    return move
 
def get_abilitis(dir):

    # Obtiene los movimientos de un Pokémon (máximo 3) ya que los pokemones tienen muchas habilidades

    abilitis = []

    for x in dir:
        abilitis.append(x['ability']['name'])
    
    return abilitis


def cargar_imagen_desde_url(url): 
    
    # ALMACENA IMAGEN EN MEMORIA 
    
    try:
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        return img
    except Exception as e:
        print(f"No se pudo cargar la imagen desde la URL: {e}")
        return None


    cont = 0
    for move in arr:
        label_about = ctk.CTkLabel(master = master, 
                                   text = move ,
                                   padx = 5,
                                  ).pack()
    cont += 1

def auto_label(master, arr, row , col):  
    
    # GENERADOR DE ETIQUETAS AUTOMATICAS
    
    cont_grid = row
    for dat in arr:
        label = ctk.CTkLabel(master = master,
                             text= dat,
                            ).grid(row = cont_grid , column = col , padx = 10, pady = 10)
        cont_grid += 1

def save_info(response_json, pokemon_name): # GUARDA EL ACHIVO EN LA CARPETA POKEDEX
        base_dir = Path(__file__).resolve().parent
        pokedex_dir = base_dir / "pokedex"
        path = pokedex_dir / f"{pokemon_name}.json"
 
        with open(path, "w") as fh:
            json.dump(response_json, fh, indent=4)

def window_info_pokemon(pokemon): # MUESTRA LA INFORMACION EN UNA GUI
    
     
    datos_pokemon = pokemon
    name = datos_pokemon['name']
    id = datos_pokemon['id']
    sprites_front = datos_pokemon['sprites']['front_default']
    img_pokemon_front = cargar_imagen_desde_url(sprites_front)
    sprites_back = datos_pokemon['sprites']['front_shiny']
    img_pokemon_back = cargar_imagen_desde_url(sprites_back)
    type = get_type(datos_pokemon['types'])
    weight = datos_pokemon['weight']
    height = datos_pokemon['height']
    moves = get_moves(datos_pokemon['moves'])
    abilities = get_abilitis(datos_pokemon['abilities'])
    #stats = get_stats(datos_pokemon['stats'])



    root = ctk.CTk()
    root.title('POKEDEX')
    root.resizable(False,False)
    root.iconbitmap('resources/icon_pokedex.ico')


    def save_info(response_json, pokemon_name):
        base_dir = Path(__file__).resolve().parent
        pokedex_dir = base_dir / "pokedex"
        path = pokedex_dir / f"{pokemon_name}.json"
 
        with open(path, "w") as fh:
            json.dump(response_json, fh, indent=4)

    label_name = ctk.CTkLabel(master = root,
                              text = name.upper(),
                              font = ('Arial Blod',50),
                              anchor = 'sw'
                             ).grid(row = 0 , column = 0 , padx = 10 , pady = 10)

    label_id = ctk.CTkLabel(master = root,
                            text = f"#{id}",
                            font = ('Arial ',24),
                            anchor = 'e'
                           ).grid(row = 0 , column = 1 , padx = 10, pady = 10)


    img_sprite_front = ctk.CTkLabel(master = root,
                                    width = 144,
                                    height = 144,
                                    text = ' ',
                                    image = ctk.CTkImage(dark_image=img_pokemon_front,
                                               light_image=img_pokemon_front,
                                               size = (144,144),
                                               )
                                   ).grid(row = 1 , column = 0 , padx = 10, pady = 10)
    
    img_sprite_back = ctk.CTkLabel(master = root,
                                   width = 144,
                                   height = 144,
                                   text = ' ',
                                   image = ctk.CTkImage(dark_image=img_pokemon_back,
                                                        light_image=img_pokemon_back,
                                                        size = (144,144),
                                                       )
                                  ).grid(row = 1 , column = 1 , padx = 10, pady = 10)
    
    label_about = ctk.CTkLabel(master = root,
                               text= 'ABOUT',
                              ).grid(row = 2 , column = 0 , padx = 10, pady = 10)
    
    
    label_height = ctk.CTkLabel(master = root,
                                compound="left",
                                text = f'height: {height}',
                                padx = 5,
                               ).grid(row = 3 , column = 0 , padx = 10, pady = 10)
    
    label_weight = ctk.CTkLabel(master = root,
                                compound = 'left',
                                text = f'height: {weight}',
                                padx = 5,
                               ).grid(row = 4 , column = 0 , padx = 10, pady = 10)
    
    label_Type = ctk.CTkLabel(master = root,
                              text= 'TYPE',
                             ).grid(row = 2 , column = 1 , padx = 10, pady = 10)
    
    auto_label(root, type , 3, 1)
    
    label_moves = ctk.CTkLabel(master = root,
                               text= 'MOVES',
                              ).grid(row = 5 , column = 0 , padx = 10, pady = 10)
    
    auto_label(root, moves , 6 , 0)
    
    label_abilities = ctk.CTkLabel(master = root,
                               text= 'ABILITIES',
                              ).grid(row = 5 , column = 1 , padx = 10, pady = 10)
    
    auto_label(root, abilities , 6 , 1)

    save_info(datos_pokemon, name)

    root.mainloop()

if __name__ == "__main__": 

    pokemon_name = input("Eligue un pokemon, Nombre o ID :")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    status_code = response.status_code
    
    if status_code >= 400 and status_code <= 599:

        print(f"El pokemon: '{pokemon_name}' no existe")

    else:
        
        response_json = response.json()
        
        window_info_pokemon(response_json)
        
 
    
