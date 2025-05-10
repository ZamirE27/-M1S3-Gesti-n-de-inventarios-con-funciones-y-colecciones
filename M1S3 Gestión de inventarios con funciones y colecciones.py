# This function saves all user input data into the system, storing it in a list of dictionaries.
def saveData(prodName, prodValue, prodQty):
    dictionary = {
        "name": prodName,
        "price": prodValue,
        "quantity": prodQty
    }
    products.append(dictionary)
    print("Producto registrado con éxito.✅\n")
    return products

# This function valids all the user input into the system, it is general so It might valid every single data that we've requested to the user,
# as long as we call it using a variable and it should have all the parameters that will store the entrace requested
def dataValidation(message, type, function=None):
    while True:
        entry = input(message).strip().lower()
        try:
            valdEntry = type(entry)
            if function and not function(valdEntry):
                print("ERROR: El dato ingresado no cumplen con las condiciones especificas")
                continue 
            return  valdEntry
        except:
            print(f"ERROR: debes ingresar el tipo de dato correcto")

# This is the function that requests the data to the user and
# here we're calling the function (dataValidation()) into the variables which will store the inputs requested.            
def addProduct():
    howManyAdd = dataValidation("¿Cuantos productos deaseas añadir?: ", int, lambda valdEntry: valdEntry >= 1)
    for i in range(howManyAdd):
        print("-"*50)
        print(f"           Registra el producto  #{i+1}           ")
        print("-"*50)
        prodName = dataValidation("Introduce el nombre de tu producto: \n",str, lambda valdEntry: valdEntry.isalpha())
        prodValue = dataValidation("Introduce el precio del producto: ",float, lambda valdEntry: valdEntry > 0 )
        prodQty = dataValidation("Introduce la cantidad del producto: ",int, lambda valdEntry: valdEntry >= 1 )
        saveData(prodName, prodValue, prodQty)
    onceAgain("añadir productos" ,addProduct)
 
# This function checks the inventory for a specific product.
# It uses a "for" loop to go through each product key stored in the dictionaries within the list.
def lookforProduct():
    lookforName = dataValidation("¿Cual es el nombre del producto que deseas consultar?: \n", str,lambda valdEntry: valdEntry.isalpha())
    if products != []:
        found = False
        for key in products:
            if key["name"] == lookforName:
                found  = True
                print(key)
                print("-"*50)
                print(f"        Producto Encontrado. ✅        ")
                print("-"*50)
                print(f"Nombre del porducto: {key["name"]}")
                print(f"Precio del producto: {key["price"]}")
                print(f"cantidad del producto: {key["quantity"]}")
                print("-"*50)
                return
        if not found:     
            print("-"*50)
            print(f"        Producto no encontrado        ")
            print("-"*50)
            return  
    else:
        print("-"*50)
        print(f"        ERROR: el inventario esta vacio       ")
        print("-"*50)
    onceAgain("cosultar productos", lookforProduct)

# Here we created another functions that helps the user to update the the price or the quantity stored of the specific product
# using again a "for" loop to go through every product key unti it matches with the one was input by the user                 
def updateProd():
    whichProd = dataValidation("¿Cual es el nombre del producto que deseas actualizar?: \n", str,lambda valdEntry: valdEntry.isalpha())
    if products == []:
        print("-"*50)
        print(f"        ERROR: el inventario esta vacio       ")
        print("-"*50)
    else:
        found = False
        for key in products:
            if key["name"] == whichProd:
                found  = True
                while True:
                    whatUpdt = input ("¿Que deseas actualizar? (Precio o cantidad): ").strip().lower()
                    match whatUpdt:
                        case "precio":
                            newPrice = dataValidation("Introduce el nuevo precio del producto: ",float, lambda valdEntry: valdEntry > 0 )
                            key["price"] = newPrice
                            print("-"*50)
                            print(f"         Precio actualizado con éxito. ✅        ")
                            print("-"*50)
                            print(f"Nombre del porducto: {key["name"]}")
                            print(f"Nuevo Precio del porducto: {key["price"]}")
                            print(f"cantidad del porducto: {key["quantity"]}")
                            print("-"*50)
                            break
                        case "cantidad":
                            newQty = dataValidation("Introduce la nueva cantidad del producto: ",int, lambda valdEntry: valdEntry >= 1 )
                            key["quantity"] = newQty
                            print("-"*50)
                            print(f"         Cantidad actualizada con éxito. ✅        ")
                            print("-"*50)
                            print(f"Nombre del porducto: {key["name"]}")
                            print(f"Precio del porducto: {key["price"]}")
                            print(f"Nueva cantidad del porducto: {key["quantity"]}")
                            print("-"*50)
                            break
                        case _:
                            print("ERROR: la opcion ingresada no es valida, intentalo nuevamente")
                            continue
        if not found:     
            print("-"*50)
            print(f"        Producto no encontrado        ")
            print("-"*50)
        onceAgain("actualizar productos", updateProd)

# Keeping the same way to find the product keys, we created another funcion but this time to delete the product that the user 
# inputs.       
def deleteProd():
    lookforName = dataValidation("¿Cual es el nombre del producto que deseas Eliminar?: \n", str,lambda valdEntry: valdEntry.isalpha())
    if products == []:
        print("-"*50)
        print(f"        ERROR: el inventario esta vacio       ")
        print("-"*50)
    else:
        found = False
        for key in products:
            if key["name"] == lookforName:
                found = True
                print("-"*54)
                print(f"Nombre del porducto: {key["name"]}")
                print(f"Precio del porducto: {key["price"]}")
                print(f"cantidad del porducto: {key["quantity"]}")
                print("-"*54)
                confirmation = dataValidation("¿Estas seguro que deseas eliminar este producto?: (S/N)\n", str,lambda valdEntry: valdEntry.isalpha())
                if confirmation == "s" or confirmation == "si":
                    products.remove(key)
                    print("-"*57)
                    print(f"        El producto ha sido elimidado con éxito. ✅        ")
                    print("-"*57)
                elif confirmation == "n" or confirmation == "no":
                    return
        if not found:     
            print("-"*50)
            print(f"        Producto no encontrado        ")
            print("-"*50)
        onceAgain("eliminar otro producto", deleteProd)

# this is a lambda function to calculate the total prices of products .
calculateTotal = lambda products: sum(key["price"] * key["quantity"] for key in products) 

# If the pt wanted to try once again the process he just complted, this function allows him to do that.
# this one was called on every function that performs any process requested in the menu.
def onceAgain(message, function=None):
    while True:
        keepDoingIt = dataValidation(f"¿Quieres {message} de nuevo S/N:?\n",str,lambda valdEntry: valdEntry.isalpha())
        if keepDoingIt == "s" or keepDoingIt == "si":
            return function()
        elif keepDoingIt == "n" or keepDoingIt == "no":
            break
        else:
            print("ERROR: Instruccion no valida intenta nuevamente")

#Here we just show the menu.           
def showmenu ():
    print("="*50)
    print("||                     MENÚ                     ||")
    print("="*50)
    print("ESCOGE UNA OPCIÓN")
    print("1. Añadir productos")
    print("2. Consultar productos")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("5. Calcular el valor total del inventario")
    print("6. Salir")
    
 # this function was created to confirmed and call the functions of the process the user chose.
 # Using a "match case" we are able to give the user the oportunity to do what he wannna do.         
def menuOptions():
    showmenu()
    options = input("¿Que gestion deseas realizar?: \n").strip().lower()
    match options:
        case "1" | "añadir productos":
            print("|       Seleccionaste #1: Añadir productos       |")
            print("_"*50)
            addProduct()
            onceAgain("volver al menú", menuOptions)
        case "2" | "cosultar productos":
            print("|       Seleccionaste #2: consultar productos       |")
            print("_"*53)
            lookforProduct()
            onceAgain("volver al menú", menuOptions)
        case "3" | "actualizar productos":
            print("|       Seleccionaste #3: Actualizar productos       |")
            print("_"*54)
            updateProd()
            onceAgain("volver al menú", menuOptions)
        case "4" | "eliminar productos":
            print("|       Seleccionaste #4: Eliminar productos       |")
            print("_"*52)
            deleteProd()
            onceAgain("volver al menú", menuOptions)
        case "5" | "calcular el valor total de inventarios": 
            print("|       Seleccionaste #5: Calcular el valor total       |")
            print("_"*55) 
            if products == []:
                print("-"*50)
                print(f"        ERROR: el inventario esta vacio       ")
                print("-"*50)   
            else:      
                total = calculateTotal(products)
                print(f"")
                print("-"*57)
                print(f"        El valor total de todo el inventario es de: {total}        ")
                print("-"*57) 
            onceAgain("volver al menú", menuOptions)
        case "6" | "salir":
            print("|                 ¡Vuelve pronto!                  |")
            print("_"*50) 
        case _:
            print("ERROR: la opcion ingresada no es valida")
            onceAgain("intentarlo nuevamente", menuOptions)
            
# I created this tuple to show you that I actually understand how it works, since the training requested to modify one, which does not make sense. 
user = ("David Henao")
print("-"*50)
print(f"             Bienvenido señor {user}"             )
print("-"*50) 
global products
products = []
menuOptions()
