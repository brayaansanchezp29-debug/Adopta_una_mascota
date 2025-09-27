# AdoptaUnaMascota - Sistema de Adopción de Mascotas

def crear_mascotas():
    """
    Crea y retorna una lista de mascotas disponibles para adopción
    """
    mascotas = [
        {
            "nombre": "Luna",
            "especie": "perro",
            "edad": 3,
            "energia": "media",
            "compatible_ninos": True
        },
        {
            "nombre": "Max",
            "especie": "perro", 
            "edad": 2,
            "energia": "alta",
            "compatible_ninos": False
        },
        {
            "nombre": "Coco",
            "especie": "perro",
            "edad": 5,
            "energia": "media",
            "compatible_ninos": True
        },
        {
            "nombre": "Mimi",
            "especie": "gato",
            "edad": 1,
            "energia": "baja",
            "compatible_ninos": True
        },
        {
            "nombre": "Whiskers",
            "especie": "gato",
            "edad": 7,
            "energia": "baja",
            "compatible_ninos": False
        },
        {
            "nombre": "Bella",
            "especie": "gato",
            "edad": 4,
            "energia": "media",
            "compatible_ninos": True
        },
        {
            "nombre": "Copito",
            "especie": "conejo",
            "edad": 2,
            "energia": "media",
            "compatible_ninos": True
        },
        {
            "nombre": "Rocky",
            "especie": "perro",
            "edad": 6,
            "energia": "alta",
            "compatible_ninos": True
        },
        {
            "nombre": "Nala",
            "especie": "gato",
            "edad": 3,
            "energia": "alta",
            "compatible_ninos": False
        },
        {
            "nombre": "Oreo",
            "especie": "conejo",
            "edad": 1,
            "energia": "baja",
            "compatible_ninos": True
        }
    ]
    return mascotas

def obtener_preferencias_usuario():
    """
    Solicita y retorna las preferencias del usuario
    """
    print("=== BIENVENIDO A ADOPTAUNAMASCOTA ===")
    print("Vamos a encontrar tu mascota ideal!\n")
    
    # Obtener especie preferida
    
    while True:
        especie = input("¿Qué especie te interesa? (perro/gato/conejo): ").lower().strip()
        if especie in ["perro", "gato", "conejo"]:
            break
        else:
            print("Error: Por favor selecciona una opción válida: 'perro', 'gato' o 'conejo'.")
    
    # Obtener rango de edad
    while True:
        try:
            edad_min = int(input("Edad mínima preferida (en años): "))
            edad_max = int(input("Edad máxima preferida (en años): "))
            if edad_min ==1 and edad_max <=15:
                break
            else:
                print("Error: La edad debe estar en el rango de 1 a 15 años")
        except ValueError:
            print("Error: Por favor ingresa números válidos para la edad.")
    
    # Obtener nivel de energía
    while True:
        energia = input("¿Nivel de energía preferido? (alta/media/baja): ").lower().strip()
        if energia in ["alta", "media", "baja"]:
            break
        else:
            print("Error: Por favor ingresa 'alta', 'media' o 'baja'.")
    
    # Verificar si tiene niños
    while True:
        tiene_ninos = input("¿Tienes niños en casa? (sí/no): ").lower().strip()
        if tiene_ninos in ["sí", "si", "yes", "s"]:
            tiene_ninos = True
            break
        elif tiene_ninos in ["no", "n"]:
            tiene_ninos = False
            break
        else:
            print("Error: Por favor responde 'sí' o 'no'.")
    
    return {
        "especie": especie,
        "edad_min": edad_min,
        "edad_max": edad_max,
        "energia": energia,
        "tiene_ninos": tiene_ninos
    }

def filtrar_mascotas(mascotas, preferencias):
    """
    Filtra las mascotas según las preferencias del usuario
    """
    mascotas_compatibles = []
    
    for mascota in mascotas:
        # Verificar especie
        if mascota["especie"] != preferencias["especie"]:
            continue
            
        # Verificar edad
        if not (preferencias["edad_min"] <= mascota["edad"] <= preferencias["edad_max"]):
            continue
            
        # Verificar energía
        if mascota["energia"] != preferencias["energia"]:
            continue
            
        # Verificar compatibilidad con niños
        if preferencias["tiene_ninos"] and not mascota["compatible_ninos"]:
            continue
            
        mascotas_compatibles.append(mascota)
    
    return mascotas_compatibles

def mostrar_mascota(mascota):
    """
    Muestra la información de una mascota
    """
    compatible_texto = "amigable con niños" if mascota["compatible_ninos"] else "no amigable con niños"
    
    print(f"\n--- {mascota['nombre']} ---")
    print(f"Especie: {mascota['especie'].capitalize()}")
    print(f"Edad: {mascota['edad']} años")
    print(f"Energía: {mascota['energia'].capitalize()}")
    print(f"Niños: {compatible_texto}")

def proceso_adopcion(mascotas_compatibles):
    """
    Maneja el proceso de selección y adopción de mascotas
    """
    if not mascotas_compatibles:
        print("\nLo sentimos, no encontramos mascotas que coincidan exactamente con tus preferencias.")
        print("Te recomendamos ampliar tus criterios de búsqueda.")
        return False
    
    print(f"\n¡Genial! Encontramos {len(mascotas_compatibles)} mascota(s) perfecta(s) para ti!")
    print("Vamos a mostrarlas una por una:\n")
    
    for i, mascota in enumerate(mascotas_compatibles, 1):
        print(f"=== MASCOTA {i} ===")
        mostrar_mascota(mascota)
        
        while True:
            decision = input(f"\n¿Quieres adoptar a {mascota['nombre']}? (sí/no): ").lower().strip()
            if decision in ["sí", "si", "yes", "s"]:
                print(f"\n ¡FELICIDADES! Has adoptado a {mascota['nombre']}!")
                print(f"¡{mascota['nombre']} estará muy feliz en su nuevo hogar!")
                print("Gracias por usar AdoptaUnaMascota 🐾")
                return True
            elif decision in ["no", "n"]:
                if i == len(mascotas_compatibles):
                    print("\n Has visto todas las opciones disponibles.")
                    print("¡Vuelve pronto cuando estés listo para adoptar!")
                else:
                    print(f"Entendido. Veamos la siguiente opción...")
                break
            else:
                print("Por favor responde 'sí' o 'no'.")
    
    return False

def main():
    """
    Función principal que ejecuta el programa
    """
    # Crear lista de mascotas
    mascotas = crear_mascotas()
    
    # Obtener preferencias del usuario
    preferencias = obtener_preferencias_usuario()
    
    # Filtrar mascotas compatibles
    mascotas_compatibles = filtrar_mascotas(mascotas, preferencias)
    
    # Proceso de adopción
    proceso_adopcion(mascotas_compatibles)

# Ejecutar el programa
if __name__ == "__main__":
    main()