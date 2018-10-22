import json
import sys

print ("Leer archivos")
leer = json.loads(open('grupos.json').read())


class grupo:
    def __init__(self, id, grado, grupos):
        self.id = id
        self.grado = grado
        self.grupos = grupos
    
    def __str__(self):
        return "id: %s, grado: %s, grupos: %s" % (self.id, self.grado, self.grupos)

    def get_grado(self):
        return self.grado


def agregarGrupo(lista_grupos, grupo):
    lista_grupos.append(grupo)
    print ("Añadido el grupo de %s exitosamente" % grupo.grado)

def imprimir(lista):
    for x in range(len(lista)):
        print (lista[x])

l = []
l2 = []
for x in range(len(leer)):
    agregarGrupo(l,grupo(leer[x]['id'],leer[x]['grado'],leer[x]['grupos']))

for y in range(len(l)):
    l2.append(grupo.get_grado(l[y]))



imprimir(l2)


