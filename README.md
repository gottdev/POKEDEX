<h1>Pokédex App</h1>

<p>Este proyecto utiliza la API de Pokémon para mostrar información detallada de cada Pokémon y guardarla localmente en archivos JSON.</p>

<h2>Librerías Utilizadas</h2>
<ul>
<h3>customtkinter:</h3> <h4>Para crear la interfaz gráfica de usuario.</h4>
<h3>PIL:</h3> <h4>Para manejar y mostrar imágenes.</h4>
<h3>requests:</h3> <h4> Para realizar peticiones a la API de Pokémon.</h4>
<h3>io.BytesIO:</h3> <h4>Para almacenar imágenes en memoria.</h4>
<h3>json:</h3> <h4>Para leer y escribir archivos JSON.</h4>
<h3>pathlib.Path:</h3> <h4>Para gestionar rutas y directorios.</h4>
</ul>
<h2>Funciones Principales</h2>
<ul>
<h3>get_type(dic)</h3>
<p>Obtiene los tipos de un Pokémon a partir de un diccionario.</p>
<h3>get_stats(dic)</h3>
<p>Obtiene las estadísticas base de un Pokémon a partir de un diccionario.</p>
<h3>get_abilitis(dic)</h3>
<p>Obtiene las habilidades de un Pokémon a partir de un diccionario.</p>
<h3>get_moves(dir)</h3>
<p>Obtiene los movimientos de un Pokémon a partir de un directorio, limitados a un máximo de tres.</p>
<h3>cargar_imagen_desde_url(url)</h3>
<p>Descarga y carga una imagen desde una URL proporcionada.</p>
<h3>auto_label(master, arr, row, col)</h3>
<p>Genera etiquetas automáticamente en una interfaz gráfica.</p>
<h3>save_info(response_json, pokemon_name)</h3>
<p>Guarda la información de un Pokémon en un archivo JSON en la carpeta pokedex.</p>
<h3>window_info_pokemon(pokemon)</h3>
<p>Muestra la información detallada de un Pokémon en una interfaz gráfica, incluyendo nombre, número, imágenes, tipo, peso, altura, movimientos y habilidades.</p>
</ul>
<h2>Uso</h2>
<h3>Ejecuta el script.</h3>
<p>Ingresa el nombre o ID de un Pokémon cuando se solicite.</p>
<p>La aplicación mostrará una ventana con la información del Pokémon.</p>
