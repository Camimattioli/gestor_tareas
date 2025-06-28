"""
Módulo tareas.py
Para gestionar tareas con funcionalidades de agregar, eliminar, listar y marcar como completadas.

Funciones:
- cargar_tareas: Carga las tareas desde un archivo JSON.
- guardar_tareas: Guarda las tareas en un archivo JSON.
- generar_id: Genera un ID único para cada tarea.
- agregar_tarea: Agrega una nueva tarea a la lista.
- eliminar_tarea: Elimina una tarea por su índice.
- completar_tarea: Marca una tarea como completada por su índice.
- listar_tareas: Lista todas las tareas con su estado (completada o pendiente).
"""

# Importaciones necesarias
import json #módulo para manejar archivos JSON
import logging #módulo para manejar logs
from pathlib import Path #módulo para manejar rutas de archivos

# Archivo donde se guardan las tareas
TAREAS_FILE = Path("tareas.json")

# Configuración del logger para registrar acciones
logging.basicConfig(
    filename = 'registro.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

########################################################################
# Funciones para manejar tareas:

# Funciones para cargar tareas
def cargar_tareas():
    """
    Carga las tareas desde un archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.

    Retorna:
    list: Lista de tareas (cada tarea es un dict).
    """
    # Verifica si el archivo de tareas existe
    if not TAREAS_FILE.exists():
        guardar_tareas([])
        return []
    # Si el archivo existe, intenta cargar las tareas
    try:
        with open(TAREAS_FILE, "r", encoding = "utf-8") as f:
            return json.load(f)
    # Si ocurre un error al cargar, registra el error y devuelve una lista vacía
    except Exception as e:
        logging.error(f"Error al cargar tareas: {e}")
        return []
    
# Funcion para guardar tareas.
def guardar_tareas(tareas):
    """
    Guarda las tareas en un archivo JSON.

    Parámetros:
    tareas (list): Lista de tareas a guardar.
    """
    try: 
        with open(TAREAS_FILE, "w", encoding = "utf-8") as f: # Abre el archivo en modo escritura
            json.dump(tareas, f, indent = 4, ensure_ascii = False) # Escribe las tareas en formato JSON.
        logging.info("Tareas guardadas correctamente.") # Registra que las tareas se guardaron correctamente
    # Si ocurre un error al guardar, registra el error
    except Exception as e:
        logging.error(f"Error al guardar tareas: {e}")

# Funcion para generar ID de tareas.
def generar_id(tareas):
    """
    Genera un ID único para una nueva tarea.

    Parámetros:
    tareas (list): Lista de tareas existentes.

    Retorna:
    int: Un ID único.
    """
    if not tareas: # Si no hay tareas, el ID comienza en 1
        return 1
    else:
        return max(tarea["id"] for tarea in tareas) + 1 # Genera un ID basado en el máximo ID existente + 1

# Funcion para agregar tareas.
def agregar_tarea(titulo, descripcion, prioridad):
    """
    Agrega una nueva tarea a la lista con los datos proporcionados.

    Parámetros:
    titulo (str): Título de la tarea.
    descripcion (str): Descripción de la tarea.
    prioridad (str): Prioridad de la tarea ("alta", "media", "baja").

    Retorna:
    dict: La tarea agregada.
    """
    tareas = cargar_tareas() # Carga las tareas existentes
    nueva_tarea = {
        "id": generar_id(tareas),
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea) # Agrega la nueva tarea a la lista de tareas
    guardar_tareas(tareas)
    logging.info(f"Tarea agregada: {nueva_tarea}") # Registra que la tarea fue agregada
    return nueva_tarea 

# Funcion para eliminar tareas.
def eliminar_tarea(id_tarea):
    """
    Elimina una tarea por su ID.

    Parámetros:
    id_tarea (int): ID de la tarea a eliminar.
    Retorna:
    bool: True si la tarea fue eliminada, False si no se encontró.
    """
    tareas = cargar_tareas()
    tarea = next((t for t in tareas if t['id'] == id_tarea), None) # Busca la tarea por su ID
    if tarea:
        tareas.remove(tarea) # Si la tarea existe, la elimina de la lista
        guardar_tareas(tareas) # Guarda la lista actualizada de tareas
        logging.info(f"Tarea eliminada: {tarea}") # Registra que la tarea fue eliminada
        print(f"Tarea eliminada: {tarea['titulo']}") # Imprime el título de la tarea eliminada
        return True
    return False # Si no se encontró la tarea, devuelve False

# Funcion para completar tareas
def completar_tarea(id_tarea):
    """
    Marca una tarea como completada por su ID.

    Parámetros:
    id_tarea (int): ID de la tarea a completar.
    
    Retorna:
    bool: True si la tarea fue marcada como completada, False si no se encontró.
    """
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            if tarea['estado'] == 'completada':
              logging.warning(f"Tarea ya está completada: {tarea}")
              return False
            tarea['estado'] = 'completada'
            guardar_tareas(tareas)
            logging.info(f"Tarea completada: {tarea}")
            return True
    return False

# Funcion para listar tareas
def listar_tareas():
    """
    Devuelve la lista completa de tareas.

    Returns:
        list: Lista de tareas (puede estar vacía).
    """
    tareas = cargar_tareas()
    logging.info(f"Se consultaron {len(tareas)} tareas.")
    return tareas