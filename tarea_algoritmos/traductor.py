# elaborar un programa que tenga la capacidad de : 1: agregar nuevas traducciones al
# diccionario 2: traducir de la siguiente forma codigo origen, codigo destino y
# palabra EN-ES dog -> perro ES-EN perro -> dog
PALABRAS_A_TRADUCIR = {
    "azul": "blue",
    "agua": "water",
    "despues": "after",
    "trabajo": "work",
    "libro": "book"
}

menu_de_opciones = 0
while menu_de_opciones != 4:
    print("\n Seleccione la opcion que necesite \n")
    print("1. Traducir palabras de Español a Ingles \n")
    print("2. Traducir palabras de Ingles a Español \n")
    print("3. Ingresar Nueva Palabra al diccionario \n")
    print("4. Salir \n")
    menu_de_opciones = int(
        input("Ingrese el numero de la accion que quiere realizar"))
    if menu_de_opciones == 1:
        palabra_español = input(
            "Ingrese la palabra en español para traducirla a ingles ")
        if PALABRAS_A_TRADUCIR.get(palabra_español) != None:
            print(f"{palabra_español} = {PALABRAS_A_TRADUCIR.get(palabra_español)}")
        else:
            print("La palabra no existe en el diccionario")
    elif menu_de_opciones == 2:
        palabra_ingles = input(
            "Ingrese la palabra en ingles para traducirla al español")
        encontrar = False
        for key in PALABRAS_A_TRADUCIR.keys():
            if palabra_ingles == PALABRAS_A_TRADUCIR[key]:
                print(f"{palabra_ingles} = {key}")
                encontrar = True
                break
        if encontrar == False:
            print("La palabra es inexistente")
    elif menu_de_opciones == 3:
        nueva_palabra = input(
            "Ingrese la palabra en español que desea agregar")
        if PALABRAS_A_TRADUCIR.get(nueva_palabra) == None:
            nueva_palabra_ingles = input("Escribe su traduccion en ingles")
            PALABRAS_A_TRADUCIR.update({nueva_palabra: nueva_palabra_ingles})
            print("La palabra ha sido agregada exitosamente")
        else:
            print("Esta palabra ya ha sido agregada con anterioridad")
