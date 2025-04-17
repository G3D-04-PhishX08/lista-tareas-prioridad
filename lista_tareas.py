import json
import os
from colorama import Fore, Style

# Configuración
ARCHIVO_TAREAS = "tareas.json"
PRIORIDADES = {
    "alta": Fore.RED,
    "media": Fore.YELLOW,
    "baja": Fore.GREEN
}

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            return json.load(f)
    return []

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=2)

def mostrar_tareas(tareas):
    """Muestra las tareas con colores según prioridad."""
    if not tareas:
        print(Fore.CYAN + "No hay tareas pendientes." + Style.RESET_ALL)
        return

    print(Fore.BLUE + "\n📝 Lista de Tareas:" + Style.RESET_ALL)
    for i, tarea in enumerate(tareas, 1):
        color = PRIORIDADES.get(tarea["prioridad"], Fore.WHITE)
        print(f"{i}. {color}{tarea['nombre']} ({tarea['prioridad']}){Style.RESET_ALL}")

def agregar_tarea(tareas):
    """Añade una nueva tarea."""
    nombre = input("Nombre de la tarea: ")
    print("Prioridades: alta, media, baja")
    prioridad = input("Prioridad: ").lower()
    
    if prioridad not in PRIORIDADES:
        prioridad = "media"

    tareas.append({"nombre": nombre, "prioridad": prioridad})
    guardar_tareas(tareas)
    print(Fore.GREEN + "✅ Tarea añadida." + Style.RESET_ALL)

def eliminar_tarea(tareas):
    """Elimina una tarea."""
    mostrar_tareas(tareas)
    try:
        num = int(input("Número de tarea a eliminar: ")) - 1
        if 0 <= num < len(tareas):
            tarea_eliminada = tareas.pop(num)
            guardar_tareas(tareas)
            print(Fore.GREEN + f"✅ Tarea '{tarea_eliminada['nombre']}' eliminada." + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Número inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "❌ Ingresa un número válido." + Style.RESET_ALL)

def main():
    tareas = cargar_tareas()
    while True:
        print(Fore.MAGENTA + "\n--- MENÚ ---" + Style.RESET_ALL)
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print(Fore.CYAN + "¡Hasta luego! 👋" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ Opción no válida." + Style.RESET_ALL)

if __name__ == "__main__":
    from colorama import init
    init()  # Inicializa Colorama
    main()