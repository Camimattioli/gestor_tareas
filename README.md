# Gestor de Tareas con Prioridad
Este proyecto es un gestor de tareas hecho en Python que permite:
- Agregar tareas con prioridad (alta, media, baja)
- Listar tareas pendientes o completadas
- Marcar tareas como completadas
- Eliminar tareas
- Guardar las tareas en un archivo `.json`
- Registrar acciones importantes en un archivo de logs

# Características

- Guardado persistente de tareas en archivo JSON (`tareas.json`).
- Registro de acciones importantes en un archivo de logs (`registro.log`).
- Manejo de errores comunes (IDs inválidos, problemas con archivos).
- Uso de la librería externa [Rich](https://github.com/Textualize/rich), que ayuda en la presentación de la interfaz del usuario.
- Código modular y fácil de mantener (separación entre lógica y presentación).
- Archivo `requirements.txt` para gestionar dependencias.

# Estructura del Proyecto
gestor_tareas/
- │
- ├── main.py # Archivo principal con menú interactivo
- ├── tareas.py # Funciones para manejar tareas
- ├── tareas.json # Archivo JSON para persistencia de datos
- ├── registro.log # Archivo para registro de logs
- ├── requirements.txt # Librerías externas necesarias
- └── README.md # Documentación del proyecto

# Requisitos
- Python 3.x
- Librería externa: `rich` 

# Instalacion desde consola
1. Crear entorno virtual: python -m venv nombre_del_entorno

2. Activar entorno: 
- source venv/bin/activate  # En Linux/macOS
- venv\Scripts\activate     # En Windows

3. Instalar dependencias: pip install -r requirements.txt

# Uso
1. Ejecutar el programa principal: python main.py
2. Se mostrará un menú con opciones para:
- Ver todas las tareas
- Agregar una tarea nueva
- Completar una tarea existente
- Eliminar una tarea
- Salir del programa

Las tareas se almacenan en tareas.json y cada acción queda registrada en registro.log.

# Ejemplos:
Ejemplo de tareas en tareas.json:
- [
-       {
-       "id": 1,
-       "titulo": "Hacer la cama",
-       "descripcion": "Lavar las sábanas primero",
-       "prioridad": "alta",
-       "estado": "pendiente"
-   }
- ]

Ejemplo de registro de acciones (registro.log):
- 2025-06-28 16:00:00,123 - INFO - Tarea agregada: {'id': 3, 'titulo': 'Pagar facturas', ...}
- 2025-06-28 16:05:00,456 - INFO - Tarea completada: {'id': 1, 'titulo': 'Comprar comida', ...}

