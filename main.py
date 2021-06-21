

#Dictionary
inventory = {"sword":{"value":50,"quantity":3},
             "shield":{"value":20, "quantity":6}, 
             "magic potion":{"value":20, "quantity":2}}
# Empty Tracking list
items = ["sword","shield", "magic potion"]

c="" #Runs the while loop as long as user wants

def menu():
    #Instructions
    print("Virtual Items Inventory")
    print("----------------------")
    print("A-Add an item")
    print("R-Remove an item")
    print("E-Edit details of an item")
    print("L-List all names of items")
    print("D-List all details of all items")
    print("Q-Quit")
    print()

while(c!= "q" or c!= "Q"):
    menu()
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):#Add an item
        item_name = input("Enter item name: ")
        
        exist=False
        #search dictionary
        for key, value in inventory.items():
            if(item_name in items):
                exist=True
        if(exist):
            print()
            print("That item already exists!")
        else:
            item_value = float(input("Enter item value: "))
            item_quantity = int(input("Enter item quantity: "))
            
            inventory[item_name]= {}
            inventory[item_name]["value"]=item_value
            inventory[item_name]["quantity"]= item_quantity
        
            #add item to tracking list
            items.append(item_name)
            print()
            print("Item was added successfully!")
        
    elif(c=="E" or c=="e"):#Edit item
        print()
        name = input("Enter item name: ")
        if(name in items):
            item_name = input("Enter item new name: ")
            item_value = float(input("Enter item value: "))
            item_quantity = int(input("Enter item quantity: "))

            del inventory[name]
            items.remove(name)
            
            inventory[item_name]= {}
            inventory[item_name]["value"]=item_value
            inventory[item_name]["quantity"]= item_quantity
        
            #add item to tracking list
            items.append(item_name)
            
        else:
            print("That item does not exist!")
        print()
    
            
    elif(c=="R" or c=="r"):#Remove an item
        print()
        name = input("Enter item name: ")
        if(name in items):
            del inventory[name]
            items.remove(name)
            
            print("Item successfully removed!")
        else:
            print("That item does not exist!")
        print()
        
    elif(c=="L" or c=="l"):#List all the names
        print("\nItems in Inventory: ")
        for i in items:
            print(i)
        print()
    elif(c=="D" or c=="d"):#List all the details
        print("Details of all Items in Inventory: \n")
        for key, value in inventory.items():
            print("Item: ", key)
            for key in value:
                print(key + ':', value[key])
            print()
    else:
        print()
        print("ERROR! Choice not valid!")
        print()

print()
print("Goodbye! Inventory System Closed!")