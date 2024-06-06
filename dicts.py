def create_inventory(items):
    inventory = dict()
    for element in items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory[element] = 1
    return inventory 

def add_items(inventory, items):
    for element in items:
        if element in inventory:
            inventory[element] += 1
        else:
            inventory[element] = 1
    return inventory 


def decrement_items(inventory, items):
    for element in items:
        if element in inventory and inventory[element] > 0:
            inventory[element] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    else:
        return inventory
    return inventory


def list_inventory(inventory):
    inventory_list = []
    for key in list(inventory.keys()):
        if inventory[key] > 0:
            inventory_tuple = key, inventory[key]
            inventory_list.append(inventory_tuple) 
        else:  
            del inventory[key]
    return inventory_list 

