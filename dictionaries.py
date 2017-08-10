#Fanatasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(str(v)+ " " + k)
        item_total += 1
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

#List to Dictionary Function For Fantasy Game Inventory
def addToInventory(inventory, addedItems):
    for i in addedItems:
    	if i in inventory:
    		inventory[i] += 1
    	else:
    		inventory[i] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)