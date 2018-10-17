import json
import sys

print ("Leer archivos")
leer = json.loads(open('grupos.json').read())


class grupos:
    def __init__(self, id, grado, grupos):
        self.id = id
        self.grado = grado
        self.grupos = grupos
    
    def __str__(self):
        return "id: %s, grado: %s, grupos: %s" % (self.id, self.grado, self.grupos)

def agregarGrupo(lista_grupos, grupos):
    lista_grupos.append(grupos)
    print ("Añadido el grupo de %s exitosamente" % grupos.grado)

def imprimir(lista):
    for x in range(len(lista)):
        print (lista[x])

l = []

for x in range(len(leer)):
    agregarGrupo(l,grupos(leer[x]['id'],leer[x]['grado'],leer[x]['grupos']))

imprimir(l)


