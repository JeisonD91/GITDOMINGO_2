"""
frutas =("fresa", "papaya", "naranja","papaya") #TUPLA
frutas2 = ["fresa", "papaya", "naranja"]

print(frutas.count("papaya"))
print(frutas.index("papaya"))

temporal = list(frutas)

print(frutas)
print(temporal)

temporal.pop(2)
print(temporal)

frutas = tuple(temporal)
print(frutas)
"""

# DICCIONARIOS
"""
lista = ["Mazda", "renault", "Chevrolet"] #lista
lista = ("Mazda", "renault", "Chevrolet") #tupla
conjunto = {"Mazda", "renault", "Chevrolet"} #conjunto

conjunto.add("Audi")
print(conjunto)

conjunto.add(True)
print(conjunto)

conjunto.add(0)
print(conjunto)

print(len(conjunto))
#conjunto.clear()

conjunto2 = conjunto.copy()
print(conjunto2)
conjunto2.add("Mercedez")
print(conjunto2)
"""

carros = {"Mazda", "renault", "Chevrolet"}
colores = {"Rojo", "Verde", "Mazda"} 
print(carros.difference(colores)) #diferencia, el unico comun es mazda, ese sale del conjunto
print(carros.intersection(colores)) # solo me imprime el elemento común
print(carros.issubset(colores))
print(colores.issuperset(carros))

#carros.remove("Mazda")
print(carros.union(colores))