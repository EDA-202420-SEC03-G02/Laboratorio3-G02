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