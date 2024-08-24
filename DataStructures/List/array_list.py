def new_list():
    lst={
        "elements":[],
        "size":0
        }
    return lst

def add_first(lst, elem):
    lst["elements"].insert(0,elem)
    lst["size"]+=1
    return lst

def add_last(lst, elem):
    lst["elements"].append(elem)  
    lst["size"] += 1
    return lst

def is_empty (lst):
    return len(lst)==0

def get_size(lst):
    tamaño_lista=lst["size"]
    return tamaño_lista

def get_first_element(lst): 
    if not lst: 
        return None
    return lst["elements"][0]

def last_element(lst):
    if not lst: 
        return None
    return lst[-1] 

def get_element(lst, pos):
    return lst["elements"][pos]  
    
def remove_first(lst):
    if lst["size"] > 0:
        first_element = lst["elements"].pop(0)  
        lst["size"] -= 1 
        return first_element
    else:
        return None  
    
def remove_last(lst):
    if lst["size"] == 0:
        return None
    else:
        last_element = lst["elements"].pop()  
        lst["size"] -= 1 
        return last_element

def insert_element(lst, elem, pos):
    if lst["size"] == 0 or pos == lst["size"]:  
        lst["elements"].append(elem)
    else:
        lst["elements"].insert(pos, elem) 
    
    lst["size"] += 1
    return lst
       
    
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

def delete_element(lst,pos):
    if 0 <= pos < len(lst):
        lst.pop(pos) 
    else:
        return None 
    
def change_info(lst, pos, new_info):
    lst["elements"][pos] = new_info  
    return lst          
                
def exchange(lst, pos1, pos2):   
    if pos1 >= 0 and pos2 >= 0 and pos1 < lst["size"] and pos2 < lst["size"]:
        lst["elements"][pos1], lst["elements"][pos2] = lst["elements"][pos2], lst["elements"][pos1]
        return lst     
  
def sub_list(lst,pos,numelem):
    if pos < len(lst) and numelem <= len(lst)-pos:
        copia = lst[pos:pos + numelem] 
        return copia
    else:
        raise Exception("Posición o número de elementos no válidos.")
    
    

  







 
