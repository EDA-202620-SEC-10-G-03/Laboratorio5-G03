def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def new_list():
    newlist = {
        "elements": [],
        "size" : 0,
    }
    return newlist


def add_first(new_list, element):
    """Agrega un elemento al inicio de la lista."""
    new_list["elements"].insert(0, element)
    new_list["size"] += 1
    return new_list


def add_last(new_list, element):
    """Agrega un elemento al final de la lista."""
    new_list["elements"].append(element)
    new_list["size"] += 1
    return new_list

def size(newlist):
    return newlist["size"]


def is_empty(new_list):
    return new_list["size"] == 0


def first_element(new_list):
    if is_empty(new_list):
        raise IndexError("list index out of range")
    return new_list["elements"][0]

def last_element(new_list):
    if is_empty(new_list):
        raise IndexError("list index out of range")
    return new_list["elements"][-1]


def change_info(new_list, pos, new_element):
    if pos < 0 or pos >= new_list["size"]:
        raise IndexError("list index out of range")
    new_list["elements"][pos] = new_element
    return new_list

def get_element(new_list,pos):
    if pos >= new_list["size"] or pos < 0:
        raise IndexError("list index out of range")
    variable = new_list["elements"][pos]
    return variable

def remove_last(new_list):
    if is_empty(new_list):
        raise IndexError("list index out of range")
    remove = new_list["size"] -1 
    new_list["elements"].pop(-1)
    return remove

def remove_first(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    
    element = my_list["elements"].pop(0)
    my_list["size"] -= 1  # <-- ESTA LÍNEA ES VITAL
    return element

def insert_element(new_list,element,pos):
    if pos < 0 or pos > new_list["size"]:
        raise IndexError("list index out of range")
    new_list["elements"].insert(pos,element)
    new_list["size"] += 1
    return new_list

def is_present(new_list,element,cmp_function):
    """
    Invocamos cmp_function para que realice la comparación con el elemnt y si se encuentra igual da 0 mayor da 1 menor -1.
    """
    pos = -1
    centi = False
    i = 0
    while i < new_list["size"] and centi == False:  
        if cmp_function(new_list["elements"][i],element) == 0:
            centi = True
            pos = i
        i += 1
    return pos   

def delete_element(new_list,pos):
    if 0 > pos or pos > new_list["size"] :
        raise IndexError("list index out of range")
    new_list["elements"].pop(pos) #mismo espacio de memoria
    new_list["size"] -= 1
    return new_list

def exchange(my_list,pos_1,pos_2):
    if (pos_1 < 0 ) or (pos_2 < 0) or (pos_1 >= my_list["size"]) or (pos_2 >= my_list["size"]):
        raise IndexError("list out index of range")
    temp = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = temp
    return my_list

def sub_list(my_list,pos_i,num_elements):
    if (pos_i < 0 ) or (pos_i >= my_list["size"]) or (pos_i + num_elements > my_list["size"]): 
        raise IndexError("list index out of range")
    nueva_lista = new_list()
    for i in range(pos_i, pos_i + num_elements):
        add_last(nueva_lista,my_list["elements"][i])

    return nueva_lista



def insertion_sort(my_list, sort_crit):
    for i in range(1, size(my_list)):
        j = i
        while j > 0 and sort_crit(get_element(my_list, j), get_element(my_list, j-1)):
            exchange(my_list, j-1, i)
            j -= 1
    return my_list

def shell_sort(my_list,cmp_function):
    n = my_list["size"]
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = my_list["elements"][i]
            j = i
            while j >= gap and cmp_function(my_list["elements"][j - gap], temp) > 0:
                my_list["elements"][j] = my_list["elements"][j - gap]
                j -= gap
            my_list["elements"][j] = temp
        gap //= 2
    return my_list