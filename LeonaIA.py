import json


import torch 
import numpy as np
import os
import torch.nn as nn
import torch.nn.functional as F 
import torch.optim as optim
import torch.autograd as autograd
from torch.autograd import Variable

print ("Leer archivos")
leerProfesores = json.loads(open('profesores.json').read())
leerGrupos = json.loads(open('grupos.json').read())
leerAsignaturas = json.loads(open('asignaturas.json').read())
leerHorariosGrupos = json.loads(open('horariosGrupos.json').read())

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

class grupo:
    def __init__(self, id, grado, grupos):
        self.id = id
        self.grado = grado
        self.grupos = grupos
    
    def __str__(self):
        return "id: %s,\ngrado: %s,\ngrupos: %s \n\n" % (self.id, self.grado, self.grupos)

    def get_Id(self):
        return self.id    

    def get_Grado(self):
        return self.grado
    
    def get_Grupos(self):
        return self.grupos

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

class horarioGrupo:
    def __init__(self, grado, grupo, horario):
        self.grado = grado
        self.grupo = grupo
        self.horario = horario
    
    def __str__(self):
        return "grado: %s,\nGrupo: %s,\nHorario: %s \n\n" % (self.grado, self.grupo, self.horario)

def agregar_Grupo(lista_grupos, grupo):
    lista_grupos.append(grupo)
    print ("Añadido los grupos de %s exitosamente" % grupo.grado)

def agregar_Profesor(lista_profesores, profesor):
    lista_profesores.append(profesor)
    print ("Añadido a %s exitosamente" % profesor.nombre)

def agregar_Asignatura(lista_asignatura, asignatura):
    lista_asignatura.append(asignatura)
    print ("Se añadio la asignatura de %s exitosamente" % asignatura.nombre)

def agregar_HorarioGrupo(lista, horarioGrupo):
    lista.append(horarioGrupo)
    print("Se añadio correctamente el horario del grupo %s del grado %s"% (horarioGrupo.grupo,horarioGrupo.grado))

def imprimir(lista):
    for x in range(len(lista)):
        print (lista[x])

def imprime_Disponible(lista):
    for x in range(len(lista)):
        profe = lista[x]
        print("profesor: %s,\nDisponibilidad:\n%s\n\n" % (profe.get_Nombre(), profe.get_Disponibilidad()))  

profesoresList = []
gruposList = []
asignaturasList = []
horariosGruposList = []  
  


for x in range(len(leerProfesores)):
    agregar_Profesor(profesoresList, profesor(
        leerProfesores[x]['id'], 
        leerProfesores[x]['profesor'],
        leerProfesores[x]['nombre'],
        leerProfesores[x]['asignaturas'],
        leerProfesores[x]['disponibilidad']))

for x in range(len(leerAsignaturas)):
    agregar_Asignatura(asignaturasList, asignatura(
        leerAsignaturas[x]['id'],
        leerAsignaturas[x]['nombre'],
        leerAsignaturas[x]['grado'],
        leerAsignaturas[x]['horas_semana']))

for x in range(len(leerGrupos)):
    agregar_Grupo(gruposList, grupo(
        leerGrupos[x]['id'], 
        leerGrupos[x]['grado'],
        leerGrupos[x]['grupos']))

for x in range(len(leerHorariosGrupos)):
    agregar_HorarioGrupo(horariosGruposList, horarioGrupo(
        leerHorariosGrupos[x]['grado'], 
        leerHorariosGrupos[x]['grupo'],
        leerHorariosGrupos[x]['horario']))

