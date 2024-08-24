def new_list():
    lst={
        "elements":[]
        "size":0
        }
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
    
    