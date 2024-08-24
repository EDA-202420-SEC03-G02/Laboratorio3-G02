def new_list():
    lst={
        "elements":[],
        "size":0
        }
    return lst
def add_last(lst, elem):
    lst["elements"].append(elem)  
    lst["size"] += 1
    return lst
def get_first_element(lst):
    
    return lst["elements"][0]
    
    
def remove_first(lst):
    if lst["size"] > 0:
        first_element = lst["elements"].pop(0)  
        lst["size"] -= 1 
        return first_element
    else:
        return None   
    
def is_present(lst,elem, cmp_function):
    size=lst["size"]
    if size>0:
        keyexist= False
        for keypos in range(0, size):
            info= lst["elements"][keypos]
            if(cmp_function(elem, info)==0):
                keyexist= True
                break
        if keyexist:
            return keypos
    return -1        
                
def exchange(lst, pos1, pos2):   
    if pos1 >= 0 and pos2 >= 0 and pos1 < lst["size"] and pos2 < lst["size"]:
        lst["elements"][pos1], lst["elements"][pos2] = lst["elements"][pos2], lst["elements"][pos1]
        return lst     

def add_first(lst, elem):
    lst["elements"].insert(0,elem)
    lst["size"]+=1
    return lst

def is_empty (lst):
    return len(lst)==0

def last_element(lst):
    if not lst: 
        return None
    return lst[-1]
 

def remove_last(lst):
    if not lst:
        return None
    else:
        last_element=lst.pop()
        return last_element
        
def delete_element(lst,pos):
    if 0 <= pos < len(lst):
        lst.pop(pos) 
    else:
        return None
    
def sub_list(lst,pos,numelem):
    if pos < len(lst) and numelem <= len(lst)-pos:
        copia = lst[pos:pos + numelem] 
        return copia
    else:
        raise Exception("Posición o número de elementos no válidos.")
    
    

  
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
