productos = {"codigo": ["001", "002", "003", "004", "005"],
             "nombre": ["leche", "arroz", "azucar", "pera", "inka kola"],
             "precio": [5, 4, 3, 2, 6]}

listaproductos = []
totalCompra = 0
resp = "s"
while resp == "s":
    codigoIn = input("Ingresar el codigo del producto: ")
    cantidad = int(input("Ingresar la cantidad del producto: "))
    x = 0
    for i in productos["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = productos["nombre"][x]
            precioTemp = productos["precio"][x]
            totalTemp = cantidad * precioTemp
            totalCompra = totalCompra + totalTemp
            registro = codigoTemp, nombreTemp, precioTemp, cantidad, totalTemp
            listaproductos.append(registro)
        x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")

print("Cod Nombre Precio Cant Total")
for x in listaproductos:
    print(*x, end="\n")

print("El Total de la compra es: ", totalCompra)