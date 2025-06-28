"""
Archivo principal main.py
Interfaz de usuario por consola para gestionar tareas.
Utiliza la librería 'rich' para mejorar la experiencia visual.
"""

# Importaciones necesarias de rich
from rich.console import Console # Consola para imprimir mensajes
from rich.table import Table # Tabla para mostrar tareas
from rich.prompt import Prompt # Entrada de usuario con prompts
from rich import box # Estilos para tablas

# Importaciones del módulo propio tareas
import tareas 

console = Console()  # Crear una instancia de consola para imprimir mensajes

def mostrar_menu():
    """
    Muestra el menú principal con opciones disponibles.
    """
    console.print("\n[bold cyan]Gestor de Tareas con Prioridad[/bold cyan]") # Imprime el título del gestor de tareas en negrita y color cian
    console.print("1. Ver todas las tareas")
    console.print("2. Agregar tarea")
    console.print("3. Completar tarea")
    console.print("4. Eliminar tarea")
    console.print("5. Salir")


def mostrar_tareas():
    """
    Muestra todas las tareas en una tabla formateada.
    """
    # Cargar las tareas desde el módulo tareas
    tareas_lista = tareas.listar_tareas()
    if not tareas_lista:
        # Si no hay tareas, muestra un mensaje y termina la función
        console.print("[yellow]No hay tareas para mostrar.[/yellow]") 
        return
    
    # Crear una tabla para mostrar las tareas
    tabla = Table(title="Tareas", box=box.ROUNDED) 
    tabla.add_column("ID", justify="right") 
    tabla.add_column("Título", style="bold")
    tabla.add_column("Descripción")
    tabla.add_column("Prioridad")
    tabla.add_column("Estado")

    # Diccionario para asignar colores a las prioridades
    colores_prioridad = { 
        "alta": "red",
        "media": "yellow",
        "baja": "green"
    }
    
    # Iterar sobre cada tarea y agregarla a la tabla
    for t in tareas_lista:
        prioridad_color = colores_prioridad.get(t['prioridad'], "white")
        estado_color = "green" if t['estado'] == "completada" else "red"

        # Agregar una fila a la tabla con los datos de la tarea
        tabla.add_row(
            str(t['id']),
            t['titulo'],
            t['descripcion'],
            f"[{prioridad_color}]{t['prioridad']}[/{prioridad_color}]",
            f"[{estado_color}]{t['estado']}[/{estado_color}]"
            )
    console.print(tabla)  # Imprime la tabla con las tareas


def agregar_tarea():
    """
    Solicita al usuario los datos para crear una nueva tarea y la agrega.
    """
    titulo = Prompt.ask("Ingrese el título de la tarea")  # Solicita el título de la tarea
    descripcion = Prompt.ask("Ingrese la descripción de la tarea")  # Solicita la descripción de la tarea
    prioridad = Prompt.ask("Ingrese la prioridad", choices = ["alta", "media", "baja"])  # Solicita la prioridad de la tarea

    # Llama a la función agregar_tarea del módulo tareas para agregar la nueva tarea
    nueva_tarea = tareas.agregar_tarea(titulo, descripcion, prioridad)  
    console.print(f"[green]Tarea agregada: {nueva_tarea['titulo']}[/green]")  # Imprime un mensaje confirmando que se agregó la tarea

def completar_tarea():
    """
    Solicita un ID para marcar una tarea como completada.
    """
    id_str = Prompt.ask("ID de la tarea a completar")
    if not id_str.isdigit():
        console.print("[red]ID inválido[/red]")
        return
    id_tarea = int(id_str) # Convierte el ID ingresado a entero
    if tareas.completar_tarea(id_tarea):
        console.print("[green]Tarea marcada como completada[/green]")
    else:
        console.print("[red]No se encontró la tarea o ya estaba completada[/red]")

def eliminar_tarea():
    """
    Solicita un ID para eliminar una tarea.
    """
    id_str = Prompt.ask("ID de la tarea a eliminar")
    if not id_str.isdigit():
        console.print("[red]ID inválido[/red]")
        return
    id_tarea = int(id_str)
    if tareas.eliminar_tarea(id_tarea):
        console.print("[green]Tarea eliminada[/green]")
    else:
        console.print("[red]No se encontró la tarea[/red]")

def main():
    """
    Bucle principal que muestra el menú y procesa las opciones del usuario.
    """
    while True:
        mostrar_menu()  # Muestra el menú principal

        # Pedir opción válida manualmente
        opcion = Prompt.ask("Seleccione una opción (1-5)").strip()
        while opcion not in ["1", "2", "3", "4", "5"]:
            console.print("[red]Opción inválida. Por favor, elija entre 1 y 5.[/red]")
            opcion = Prompt.ask("Seleccione una opción (1-5)").strip()

        if opcion == "1":
            mostrar_tareas() 
        elif opcion == "2":
            agregar_tarea() 
        elif opcion == "3":
            completar_tarea()  
        elif opcion == "4":
            eliminar_tarea()  
        elif opcion == "5":
            console.print("[bold cyan]Saliendo del gestor de tareas...[/bold cyan]")  # Mensaje de salida
            break  

if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa