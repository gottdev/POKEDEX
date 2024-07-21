<h1>Pokédex App</h1>
Este proyecto utiliza la API de Pokémon para mostrar información detallada de cada Pokémon y guardarla localmente en archivos JSON.
Librerías Utilizadas
customtkinter: Para crear la interfaz gráfica de usuario.
PIL: Para manejar y mostrar imágenes.
requests: Para realizar peticiones a la API de Pokémon.
io.BytesIO: Para almacenar imágenes en memoria.
json: Para leer y escribir archivos JSON.
pathlib.Path: Para gestionar rutas y directorios.
Funciones Principales
get_type(dic)
Obtiene los tipos de un Pokémon a partir de un diccionario.
get_stats(dic)
Obtiene las estadísticas base de un Pokémon a partir de un diccionario.
get_abilitis(dic)
Obtiene las habilidades de un Pokémon a partir de un diccionario.
get_moves(dir)
Obtiene los movimientos de un Pokémon a partir de un directorio, limitados a un máximo de tres.
cargar_imagen_desde_url(url)
Descarga y carga una imagen desde una URL proporcionada.
auto_label(master, arr, row, col)
Genera etiquetas automáticamente en una interfaz gráfica.
save_info(response_json, pokemon_name)
Guarda la información de un Pokémon en un archivo JSON en la carpeta pokedex.
window_info_pokemon(pokemon)
Muestra la información detallada de un Pokémon en una interfaz gráfica, incluyendo nombre, número, imágenes, tipo, peso, altura, movimientos y habilidades.
Uso
Ejecuta el script.
Ingresa el nombre o ID de un Pokémon cuando se solicite.
La aplicación mostrará una ventana con la información del Pokémon.
