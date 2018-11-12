import json 

print("Obteniendo información")

obtenerProfesores = json.loads(open("profesores.json").read())
obtenerAsignaturas = json.loads(open("asignaturas.json").read())
obtenerGrupos = json.loads(open("grupos.json").read())

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

class grupo:
    def __init__(self, id, grado, grupo):
        self.id = id
        self.grado = grado
        self.grupo = grupo
    
    def __str__(self):
        return "id: %s,\ngrado: %s,\ngrupo: %s \n\n" % (self.id, self.grado, self.grupo)

    def get_Id(self):
        return self.id    

    def get_Grado(self):
        return self.grado
    
    def get_Grupo(self):
        return self.grupo

def agregar_Profesor(lista_profesores, profesor):
    lista_profesores.append(profesor)
    print ("Añadido a %s exitosamente" % profesor.nombre)

def agregar_Asignatura(lista_asignatura, asignatura):
    lista_asignatura.append(asignatura)
    print ("Se añadio la asignatura de %s exitosamente" % asignatura.nombre)

def agregar_Grupo(lista_grupos, grupo):
    lista_grupos.append(grupo)
    print ("Añadido los grupos de %s exitosamente" % grupo.grado)

profesoresList = []
asignaturasList = []
gruposList = []

for x in range(len(obtenerProfesores)):
    agregar_Profesor(profesoresList, profesor(
        obtenerProfesores[x]['id'], 
        obtenerProfesores[x]['profesor'],
        obtenerProfesores[x]['nombre'],
        obtenerProfesores[x]['asignaturas'],
        obtenerProfesores[x]['disponibilidad']))

for x in range(len(obtenerAsignaturas)):
    agregar_Asignatura(asignaturasList, asignatura(
        obtenerAsignaturas[x]['id'],
        obtenerAsignaturas[x]['nombre'],
        obtenerAsignaturas[x]['grado'],
        obtenerAsignaturas[x]['horas_semana']))

for x in range(len(obtenerGrupos)):
    agregar_Grupo(gruposList, grupo(
        obtenerGrupos[x]['id'], 
        obtenerGrupos[x]['grado'],
        obtenerGrupos[x]['grupo']))

for x in range(len(profesoresList)):
    print(profesoresList(x))
