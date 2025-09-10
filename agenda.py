# La clase Contacto encapsula los datos de un solo contacto.
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    # Este metodo define cómo se muestra el objeto Contacto cuando se imprime.
    def __str__(self):
        return f"{self.nombre}: {self.telefono}"

# La clase Agenda gestiona la colección de objetos Contacto.
class Agenda:
    def __init__(self):
        # Usamos un diccionario para guardar los contactos por su nombre.
        self.contactos = {}

    def agregar_contacto(self):
        nombre = input("Ingresa el nombre del contacto: ")
        # Verificamos si el contacto ya existe.
        if nombre in self.contactos:
            print("❌ Este contacto ya existe.")
            return

        telefono = input("Ingresa el número de teléfono: ")
        # Creamos una instancia de la clase Contacto.
        nuevo_contacto = Contacto(nombre, telefono)
        self.contactos[nombre] = nuevo_contacto
        print(f"✅ Contacto '{nombre}' agregado con éxito.")

    def buscar_contacto(self):
        nombre = input("Ingresa el nombre del contacto a buscar: ")
        if nombre in self.contactos:
            # Accedemos al objeto Contacto y usamos su método __str__.
            print(f"📞 Contacto encontrado: {self.contactos[nombre]}")
        else:
            print(f"❌ Contacto '{nombre}' no encontrado.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
            return

        print("\n--- Agenda de Contactos ---")
        # Obtenemos los nombres (claves) y los ordenamos.
        nombres_ordenados = sorted(self.contactos.keys())
        for nombre in nombres_ordenados:
            # Accedemos a cada objeto Contacto y lo mostramos.
            print(self.contactos[nombre])
        print("-------------------------")

def main():
    # Creamos una instancia de la clase Agenda para gestionar el proyecto.
    mi_agenda = Agenda()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mi_agenda.agregar_contacto()
        elif opcion == '2':
            mi_agenda.buscar_contacto()
        elif opcion == '3':
            mi_agenda.mostrar_contactos()
        elif opcion == '4':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()