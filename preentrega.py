prodlist = [];
product= {};

print("***** CATALOGO DE PRODUCTOS ******* Emmanuel Carreón/carreonmail@gmail.com ")

while True:
    print("1. Crear un producto\n2. Listar productos registrados\n3. Salir")
    option = input("Ingresa una Opcion: ")

    if option == '1':
        productName = input("Ingresa el nombre del producto: ")
        productQuantity = int(input("Ingresa una cantidad: "))
        product = {
            'name': productName,
            'quantity': productQuantity
        }
        prodlist.append(product)
        print(f"Producto '{productName}' agregado con éxito.")

    elif option == '2':
        if len(prodlist) != 0:
            i = 0
            while  i < len(prodlist):
                print('Producto: ',prodlist[i]['name'],'\nCantidad: ',prodlist[i]['quantity'],'\n' )
                i +=1
        else:
            print('No agregaste ningun producto a la lista')

    elif option == '3':
        print("Saliendo del catálogo de productos. ¡Hasta luego!")
        break #salgo del while
    else:
        print("Opción no valida, pro favor elige una opción del menú")