
  
from DataStructures.List.Tests.test_array_list import test_is_empty


def get_size(lst):
    tamaño_lista=lst["size"]
    return tamaño_lista
def get_element(lst, pos):
    return lst["elements"][pos]

def insert_element(lst, elem, pos):
    if is_empty==True:
       lst.append(elem)
       lst["Size"]+=1
    else:
       lst.insert(pos, elem)
       lst["Size"]+=1
    return lst

def change_info(lst, pos, new_info):
    lst["elements"][pos].append(new_info)
    return lst 