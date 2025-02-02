#print("hola mundo")
""""
print("Vamos a hacer una suma")
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("El resultado de la suma es", suma)
print("El resultado de la resta es",resta)
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división es: ", division)

nombre = input("Cual es su nombre? ")
print("Su nombre es:", nombre)
"""
"""
nombre_cliente = input("Cual es su nombre?: ")
valor1 = int(input("Cual es el valor de su primer producto?: "))
valor2 = int(input("Cual es el valor de su segundo producto?: "))
valor3 = int(input("Cual es el valor de su tercer producto?: "))

suma = valor1 + valor2 + valor3

print("Querido", nombre_cliente, "el valor de su compra es", suma)

pago = int(input("Con cuanto va a pagar? "))
devuelta = pago - suma
print ("Su devuelta es:", devuelta)

tmultiplicar = int(input("Cual tabla de multiplciar quiere que le muestre? "))
print(tmultiplicar, "x", "1", "=", tmultiplicar*1,)
print(tmultiplicar, "x", "2", "=", tmultiplicar*2,)
print(tmultiplicar, "x", "3", "=", tmultiplicar*3,)
print(tmultiplicar, "x", "4", "=", tmultiplicar*4,)
print(tmultiplicar, "x", "5", "=", tmultiplicar*5,)
print(tmultiplicar, "x", "6", "=", tmultiplicar*6,)
print(tmultiplicar, "x", "7", "=", tmultiplicar*7,)
print(tmultiplicar, "x", "8", "=", tmultiplicar*8,)
print(tmultiplicar, "x", "9", "=", tmultiplicar*9,)
print(tmultiplicar, "x", "10", "=", tmultiplicar*10,)"""

#Listas
"""
frutas = ["naranjas", "papayas", "pera"]
tamaño = len(frutas)
frutas.append("manzana")
print(frutas)
frutas[1] = "fresas"
print(frutas)
frutas.insert(1, "mandarina")
print(frutas)

frutas.clear()
print(frutas)
#del frutas

frutas2 = frutas.copy()
print(frutas2)
frutas2.append("durazno")
print(frutas)
print(frutas2)

#frutas3 = frutas
#frutas3.append("mango")
#print(frutas3)
cantidad = frutas.count("fresas")
print(cantidad)
carros = ["renault", "mazda", "chevrolet"]
frutas.extend(carros)
print(frutas)
indice = frutas.index("pera")
print(indice)
frutas.pop()#si no se pone nada, saca el ultimo, si no, le ponemos el numero de posición del elemento
print(frutas)
frutas.pop(5)
print(frutas)
frutas.remove("fresas") #remueve en caso que haya mas de 1 elemento, el primero
print(frutas)
frutas.reverse()
print(frutas)
frutas.sort() #ordena alfabeticamente
print(frutas)
"""


#lista1 = []
#precio = int(input("ingrese el precio: "))
#lista1.append(precio)
#print(lista1)
#nombre = input("ingrese el nombre: ")
lista1.append(nombre)
print(lista1)

palabra = "amigos"
print(palabra[0])
print(len(palabra))

