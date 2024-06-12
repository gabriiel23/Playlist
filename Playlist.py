
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def añadir_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    
    def eliminar(self, valor):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
        else:
            print("la canción no esta en la lista.")
    
    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return []
        canciones = []
        actual = self.cabeza
        while actual:
            canciones.append(actual.valor)
            actual = actual.siguiente
        return canciones

class Playlist:
    def __init__(self):
        self.playlist = ListaEnlazada()
    
    def añadir_cancion(self, cancion):
        self.playlist.añadir_al_final(cancion)
    
    def eliminar_cancion(self, cancion):
        self.playlist.eliminar(cancion)
    
    def mostrar_playlist(self):
        canciones = self.playlist.mostrar()
        if canciones:
            print("")
            print("------- Playlist actual: -------")
            for idx, cancion in enumerate(canciones, start=1):
                print(f"{idx}. {cancion}")
            print("")
        else:
            print("")
            print("La playlist está VACIA.")
            print("")

def mostrar_menu():
    print("--------------------------")
    print("     Menú de Playlist     ")
    print("--------------------------")
    print("")
    print("1. Añadir canción")
    print("2. Eliminar canción")
    print("3. Mostrar playlist")
    print("4. Salir")
    print("")

def main():
    mi_playlist = Playlist()
    while True:
        mostrar_menu()
        opcion = input("Eliga una opción: ")
        
        if opcion == '1':
            cancion = input("Nombre de la canción: ")
            mi_playlist.añadir_cancion(cancion)
            print("")
            print(f"La canción '{cancion}' fue añadida a la playlist.")
            print("")
        
        elif opcion == '2':
            cancion = input("Nombre de la canción a eliminar: ")
            mi_playlist.eliminar_cancion(cancion)
            print("")
        
        elif opcion == '3':
            mi_playlist.mostrar_playlist()
        
        elif opcion == '4':
            print("Gracias por usar este programa...")
            break
        
        else:
            print("Opción no válida, por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()
