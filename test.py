import json
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import OneHotEncoder
# define example
#data = ['Arturo', 'Ezreal', 'Beto', 'Carlitos', 'Donovan']
leerProfesores = json.loads(open('profesores.json').read())
leerAsignaturas = json.loads(open('asignaturas.json').read())

#Pedimos solo nombres de los profesores y disponibilidad de los profesores
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
lista_disponibilidad = []

for x in range(len(leerProfesores)):
    agregar_Profesor(profesoresList, profesor(
        leerProfesores[x]['id'], 
        leerProfesores[x]['profesor'],
        leerProfesores[x]['nombre'],
        leerProfesores[x]['asignaturas'],
        leerProfesores[x]['disponibilidad']))

for y in range(len(profesoresList)):
    lista_nombres.append(profesor.get_Nombre(profesoresList[y]))

for z in range(len(profesoresList)):
    lista_disponibilidad.append(profesor.get_Disponibilidad(profesoresList[z]))
#Fin de bloque de código

#Traemos solo asignaturas
class asignatura:
    def __init__(self, id, nombre, grado, horasSemana):
        self.id = id
        self.nombre = nombre
        self.grado = grado
        self.horasSemana = horasSemana

    def __str__(self):
        return "id: %s,\nasignatura: %s,\ngrado: %s,\nhoras por semana: %s \n\n" % (self.id, self.nombre, self.grado, self.horasSemana)

    def get_Id(self):
        return self.id
    
    def get_Nombre(self):
        return self.nombre

    def get_Grado(self):
        return self.grado
    
    def get_HorasSemana(self):
        return self.horasSemana

def agregar_Asignatura(lista_asignatura, asignatura):
    lista_asignatura.append(asignatura)
    print ("Se añadio la asignatura de %s exitosamente" % asignatura.nombre)
    
asignaturasList = []
lista_asignaturas = []

for x in range(len(leerAsignaturas)):
    agregar_Asignatura(asignaturasList, asignatura(
        leerAsignaturas[x]['id'],
        leerAsignaturas[x]['nombre'],
        leerAsignaturas[x]['grado'],
        leerAsignaturas[x]['horas_semana']))

for y in range(len(asignaturasList)):
    lista_asignaturas.append(asignatura.get_Nombre(asignaturasList[y]))
#Fin bloque asignaturas
values = array(lista_asignaturas)
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
inverted = label_encoder.inverse_transform([argmax(onehot_encoded[1, :])])
print(inverted)
