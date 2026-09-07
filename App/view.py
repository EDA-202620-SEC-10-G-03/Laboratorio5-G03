"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones
 *
 * Dario Correal
 * Lina Ojeda
 """

import sys
import App.logic as logic
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as lt

data_structure = None

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada selección
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic(data_structure):
    """
    Se crea una instancia del controlador
    """
    control = logic.new_logic(data_structure)
    return control


def print_menu():
    """
    Menu de usuario
    """
    print("Bienvenido")
    #TODO: agregar opción 0 para escoger el tipo de estructura de datos y opción 5 para seleccionar el algoritmo de ordenamiento
    print("1- Cargar información en el catálogo")
    print("2- Consultar la información de un libro")
    print("3- Consultar los libros de un autor")
    print("4- Libros por género")
    print("5- Seleccionar el algoritmo de ordenamiento")
    print("6- Seleccionar muestra de libros")
    print("7- Ordenar los libros por rating") #para ejecutar esta opción debe haber ejecutado previamente la opción 5 y 6
    print("8- Salir")

def select_data_structure():
    """
    Vista: Captura la selección del usuario y retorna
    la estructura de datos elegida.
    """
    print("\nEscoge la estructura de datos a usar:")
    print("1 - Array_list")
    print("2 - Single_linked_list")
    
    sub_input = ""
    
    while sub_input == "":
        sub_input = input("\nSeleccione una opción: ")
        global data_structure
        # Encapsulamos la estructura de datos seleccionada en la variable `data_structure`
        if sub_input == "1":
            data_structure = al
            print("Has elegido Array_list")
            return sub_input
        elif sub_input == "2":
            data_structure = lt
            print("Has elegido Single_linked_list")
            return sub_input
        else:
            print("Opción no válida en el submenú")
            sub_input = ""

def load_data(control):
    """
    Solicita al controlador que cargue los datos en el modelo
    """
    books, authors, tags, book_tags= logic.load_data(control)
    return books, authors, tags, book_tags

def print_author_data(author):
    """
    Recorre la lista de libros de un autor, imprimiendo
    la información solicitada.
    """
    if author:
        print("Autor encontrado: " + author["name"])
        print("Promedio: " + str(author["average_rating"]))
        print("Total de libros: " + str(data_structure.size(author["books"])))
        for book_pos in range(0, data_structure.size(author['books'])):
            book = data_structure.get_element(author['books'], book_pos)
            print("Titulo: " + book["title"] + "  ISBN: " + book["isbn"])
    else:
        print("No se encontró el autor")
        
        
def print_book_info(book):
    """
    Imprime los mejores libros solicitados
    """
    if book:
        print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'] +
                    ' Work text reviews count : ' + book['work_text_reviews_count'])
    else:
        print('No se encontraron libros')



def print_sort_results(sort_books, sample=3):
    """
    Imprime la información de una muestra de libros ordenados.

    Args:
    sort_books (data_structure): La estructura de datos que contiene los libros ordenados.
    sample (int): El número de libros a imprimir. Por defecto, 3.
    
    Se espera que la función imprima la información de 'sample' libros usando la función
    print_book_info(). 
    """
    # Recorrer los elementos de la estructura de datos 'sort_books'.
    sorted_books=  sort_books[0]

    for book_pos in range(0, data_structure.size(sorted_books)):
        # Si todavía hay libros que imprimir en la muestra.
        if sample > 0:
            # Obtener el libro en la posición actual.
            book = data_structure.get_element(sorted_books, book_pos)
            # TODO: Completar la lógica para imprimir la información del libro.
            # Disminuir el contador de la muestra.
            sample -= 1

# variables utiles para el programa

data_str="""Seleccione el algoritmo de estructura de datos:
1. Array_list
2. Linked_list
"""

algo_str = """Seleccione el algoritmo de ordenamiento recursivo:
1. Selection Sort
2. insertion Sort
3. shell Sort
"""
                 
exit_opt_lt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")


# main del ejercicio
def main():
    """
    Menú principal
    """
    # bandera para controlar el ciclo del menu
    working = True
    control = None
    # tamaño de la muestra para pruebas
    size = 0.0

    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        
        if int(inputs[0]) == 0:
            # Capturamos la estructura de datos seleccionada
            user_data_structure = select_data_structure()
        
            # Se crea el controlador asociado a la vista
            control = new_logic(user_data_structure)
            
        elif int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            bk, at, tg, bktg = load_data(control)
            #TODO: imprimir la cantidad de libros, autores, géneros y asociaciones de géneros a libros cargados

        elif int(inputs[0]) == 2:
            number = input("Ingrese el id del libro que desea buscar: ")
            book = logic.get_book_info_by_book_id(control, int(number))
            print_book_info(book)

        elif int(inputs[0]) == 3:
            authorname = input("Nombre del autor a buscar: ")
            author = logic.get_books_by_author(control, authorname)
            print_author_data(author)

        elif int(inputs[0]) == 4:
            label = input("Etiqueta a buscar: ")
            book_count = logic.count_books_by_tag(control, label)
            print('Se encontraron: ', book_count, ' Libros')
                 
        elif int(inputs[0]) == 5:
            algo_opt = input(algo_str)
            algo_opt = int(algo_opt)
            algo_msg = logic.select_sort_algorithm(algo_opt)
            print(algo_msg[1])
            
        elif int(inputs[0]) == 6:
            size = input("Indique tamaño de la muestra: ")
            size = int(size)
            logic.set_book_sublist(control, size)

        elif int(inputs[0]) == 7:
            print("Ordenando los libros por rating ...")
            result = logic.sort_books(control)
            #TODO:imprimir el resultado del ordenamiento 
            print("Tiempo de ejecución:", f"{result[1]:.3f}", "[ms]")

        elif int(inputs[0]) == 8:
            # confirmar salida del programa
            end_str = "¿Desea salir del programa? (s/n): "
            opt_usr = input(end_str)
            # diferentes opciones de salida
            if opt_usr in exit_opt_lt:
                working = False
                print("\nGracias por utilizar el programa.")

        else:
            continue
    sys.exit(0)
