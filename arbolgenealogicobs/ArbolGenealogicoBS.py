class Persona:
    def __init__(self, nombre, padre=None, madre=None, conyuge=None, fallecido=False):
        self.nombre = nombre
        self.padre = padre
        self.madre = madre
        self.conyuge = conyuge
        self.hijos = []
        self.fallecido = fallecido

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def mostrar_arbol(self, nivel=0, visitados=None):
        if visitados is None:
            visitados = set()
        if id(self) in visitados:
            return
        visitados.add(id(self))

        sangria = "  " * nivel
        estado = " (†)" if self.fallecido else ""
        print(f"{sangria}- {self.nombre}{estado}")
        if self.conyuge:
            print(f"{sangria}  Cónyuge: {self.conyuge.nombre}")
        if self.padre:
            print(f"{sangria}  Padre:")
            self.padre.mostrar_arbol(nivel + 2, visitados)
        if self.madre:
            print(f"{sangria}  Madre:")
            self.madre.mostrar_arbol(nivel + 2, visitados)

# ==== CREACIÓN DEL ÁRBOL GENEALÓGICO ====

# Abuelos (todos fallecidos)
abuelo_materno = Persona("Jose Manuel Aguilar", fallecido=True)
abuela_materna = Persona("Sara Carlota Hernandez", fallecido=True)
abuelo_paterno = Persona("Jose Manuel Sanchez", fallecido=True)
abuela_paterna = Persona("Eulalia Betancourt", fallecido=True)

# Padres
padre = Persona("Bienvenido Napoleon Sanchez Betancourt", padre=abuelo_paterno, madre=abuela_paterna)
madre = Persona("Lucina Haydee Aguilar Hernandez", padre=abuelo_materno, madre=abuela_materna)

# Hermanas
vasco = Persona("Vasco Hernán Baruco")
carolina = Persona("Carolina Mariela Sanchez Aguilar", padre=padre, madre=madre, conyuge=vasco)
anabel = Persona("Anabel Sanchez Aguilar", padre=padre, madre=madre, fallecido=True)

# Beatriz
beatriz = Persona("Beatriz Gisela Sanchez Aguilar", padre=padre, madre=madre)

# Hijos (relaciones descendentes, no impresas)
padre.agregar_hijo(beatriz)
padre.agregar_hijo(carolina)
padre.agregar_hijo(anabel)
madre.agregar_hijo(beatriz)
madre.agregar_hijo(carolina)
madre.agregar_hijo(anabel)

# ==== FUNCIÓN AUXILIAR: obtener hermanas de Beatriz ====

def obtener_hermanas(persona):
    hermanas = []
    for hija in persona.madre.hijos:
        if hija != persona and hija.madre == persona.madre and hija.padre == persona.padre:
            hermanas.append(hija)
    return hermanas

# ==== MENÚ INTERACTIVO ====

def menu():
    while True:
        print("\n=== CONSULTAS SOBRE LA FAMILIA DE BEATRIZ GISELA SÁNCHEZ AGUILAR ===")
        print("1. Mostrar árbol genealógico ascendente con hermanas")
        print("2. ¿Quiénes son sus padres?")
        print("3. ¿Quiénes son sus abuelos maternos y paternos?")
        print("4. ¿Tiene hermanas? ¿Con quién está casada alguna?")
        print("5. ¿Hay familiares fallecidos?")
        print("0. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\nÁrbol genealógico de Beatriz (ascendente):\n")
            beatriz.mostrar_arbol()

            hermanas = obtener_hermanas(beatriz)
            if hermanas:
                print("\nHermanas de Beatriz:")
                for h in hermanas:
                    estado = " (†)" if h.fallecido else ""
                    conyuge = f", casada con {h.conyuge.nombre}" if h.conyuge else ""
                    print(f"  - {h.nombre}{estado}{conyuge}")
            else:
                print("No se encontraron hermanas registradas.")
        elif opcion == "2":
            print(f"\nPadre: {beatriz.padre.nombre}")
            print(f"Madre: {beatriz.madre.nombre}")
        elif opcion == "3":
            print("\nAbuelos Maternos:")
            print(f"  - Abuelo: {madre.padre.nombre} (†)")
            print(f"  - Abuela: {madre.madre.nombre} (†)")
            print("Abuelos Paternos:")
            print(f"  - Abuelo: {padre.padre.nombre} (†)")
            print(f"  - Abuela: {padre.madre.nombre} (†)")
        elif opcion == "4":
            hermanas = obtener_hermanas(beatriz)
            if hermanas:
                print("\nHermanas de Beatriz:")
                for h in hermanas:
                    estado = " (†)" if h.fallecido else ""
                    conyuge = f", casada con {h.conyuge.nombre}" if h.conyuge else ""
                    print(f"  - {h.nombre}{estado}{conyuge}")
            else:
                print("No se encontraron hermanas registradas.")
        elif opcion == "5":
            print("\nFamiliares fallecidos:")
            fallecidos = [p for p in [
                abuelo_materno, abuela_materna, abuelo_paterno, abuela_paterna, anabel
            ] if p.fallecido]
            if fallecidos:
                for persona in fallecidos:
                    print(f"  - {persona.nombre}")
            else:
                print("  No hay familiares fallecidos registrados.")
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# ==== EJECUCIÓN SEGURA ====

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido manualmente. Hasta luego.")