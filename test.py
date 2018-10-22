import json
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
# define example
#data = ['Arturo', 'Ezreal', 'Beto', 'Carlitos', 'Donovan']
leerProfesores = json.loads(open('profesores.json').read())
class profesor:
    def __init__(self, idProfesor, tipoProfesor, nombre, asignaturas, disponibilidad):
        self.idProfesor = idProfesor
        self.tipoProfesor = tipoProfesor
        self.nombre = nombre
        self.asignaturas = asignaturas
        self.disponibilidad = disponibilidad

    def __str__(self):
        return "id: %s,\ntipo: %s,\nnombre: %s,\nasignaturas: %s,\ndisponibilidad:\n%s\n\n" % (self.idProfesor, self.tipoProfesor,
         self.nombre, self.asignaturas, self.disponibilidad)

    def __eq__(self, y):
        if self.idProfesor == y:
            return True
        return False

    def get_Id(self):
        return self.idProfesor

    def get_Nombre(self):
        return self.nombre
    
    def get_TipoProfesor(self):
        return self.tipoProfesor
    
    def get_Asignaturas(self):
        return self.asignaturas

    def get_Disponibilidad(self):
        return self.disponibilidad

def agregar_Profesor(lista_profesores, profesor):
    lista_profesores.append(profesor)
    print ("Añadido a %s exitosamente" % profesor.nombre)

profesoresList = []
lista_nombres = []

for x in range(len(leerProfesores)):
    agregar_Profesor(profesoresList, profesor(
        leerProfesores[x]['id'], 
        leerProfesores[x]['profesor'],
        leerProfesores[x]['nombre'],
        leerProfesores[x]['asignaturas'],
        leerProfesores[x]['disponibilidad']))

for y in range(len(profesoresList)):
    lista_nombres.append(profesor.get_Nombre(profesoresList[y]))
        
values = array(lista_nombres)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)
# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# invert first example
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[13, :])])
print(inverted)