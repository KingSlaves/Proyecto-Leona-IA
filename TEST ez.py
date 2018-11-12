import numpy 
import random as ran

class asignatura:
    def __init__(self, id, nombre, grado, horasSemana, grupo):
        self.id = id
        self.nombre = nombre
        self.grado = grado
        self.grupo = grupo
        self.horasSemana = horasSemana

    def __str__(self):
        return "id: %s,\nasignatura: %s,\ngrado: %s,\nhoras por semana: %s,\ngrupo: %s \n\n" % (self.id, self.nombre, self.grado, self.horasSemana, self.grupo)

    def get_Id(self):
        return self.id

    def get_Grupo(self):
        return self.grupo

    def get_Nombre(self):
        return self.nombre

    def get_Grado(self):
        return self.grado
    
    def get_HorasSemana(self):
        return self.horasSemana
asignaturas_lista = [[],[],[],[]]
asignaturas_lista[0].append(asignatura("Qu1","quimica",1,4,1))
asignaturas_lista[0].append(asignatura("Qu2","quimica",1,4,2))
asignaturas_lista[0].append(asignatura("Qu3","quimica",1,4,3))
asignaturas_lista[1].append(asignatura("Al1","algebra",1,5,1))
asignaturas_lista[1].append(asignatura("Al2","algebra",1,5,2))
asignaturas_lista[1].append(asignatura("Al3","algebra",1,5,3))
asignaturas_lista[2].append(asignatura("Rs1","inteligencia",1,6,1))
asignaturas_lista[2].append(asignatura("Rs2","inteligencia",1,6,2))
asignaturas_lista[2].append(asignatura("Rs3","Inteligencia",1,6,3))
asignaturas_lista[3].append(asignatura("MatD1","matematicas discretas",1,4,1))
asignaturas_lista[3].append(asignatura("MatD2","matematicas discretas",1,4,2))
asignaturas_lista[3].append(asignatura("MatD2","matematicas discretas",1,4,3))


lista_final = [
    [
        "josue",
        [
            asignatura("Qu1","quimica",1,4,1),
            asignatura("Qu1","quimica",1,4,2),
            asignatura("Qu1","quimica",1,4,3)
        ],
        [
            [0,0,0,0,0],#1
            [1,1,1,1,1],#2
            [1,1,1,1,1],#3
            [1,1,1,1,1],#4
            [1,1,1,1,1]#4
        ]
    ], 
    [
        "kevin",
        [
            asignatura("Al1","algebra",1,4,1),
            asignatura("Al2","algebra",1,4,2),
            asignatura("Al3","algebra",1,4,3)
        ],
        [
            [0,0,0,0,0],#1
            [1,1,1,1,1],#2
            [1,1,1,1,1],#3
            [1,1,1,1,1],#4
            [1,1,1,1,1]#4
        ]
    ], 
]

lista_profesor =  [
    [#profesor 2
        [1,1,1,1,1],#1
        [0,0,0,0,0],#2
        [1,1,1,1,1],#3
        [1,1,1,1,1],#4
        [1,1,1,1,1]#4   
    ],
    [#profesor 3
        [1,1,1,1,1],#1
        [1,1,1,1,1],#2
        [1,1,1,1,1],#3
        [1,1,1,1,1],#4
        [1,1,1,1,1]#4
       
    ],
    [#profesor 4
        [1,1,1,1,1],#1
        [1,1,1,1,1],#2
        [1,1,1,1,1],#3
        [1,1,1,1,1],#4
        [1,1,1,1,1]#4
    ]
] 
lista_disponibilidad_salon = [
    [#salon 1

        [1,1,1,1,1],#1
        [1,1,1,1,1],#2
        [1,1,1,1,1],#3
        [0,0,0,1,1],#4
        [1,1,1,1,1]#4
    ],
    [#salon 2
        [1,1,0,0,0],#1
        [1,1,1,1,1],#2
        [1,1,1,1,1],#3
        [1,1,1,1,1],#4
        [1,1,1,1,1]#4
    ],
    [#salon 3
        [1,1,1,1,1],#1
        [1,1,1,1,1],#2
        [1,1,1,1,1],#3
        [1,1,0,0,0],#4
        [1,1,1,1,1]#4
    ]
] 

lista_horario_salon = [
    [#salon 1
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ],
    [#salon 2
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ],
    [#salon 3
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ]
]
lista_horario_profesor = [
    [#profesor 1
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ],
    [#profesor 2
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ],
    [#profesor 3
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ],
    [#profesor 4
        [0,0,0,0,0],#1
        [0,0,0,0,0],#2
        [0,0,0,0,0],#3
        [0,0,0,0,0],#4
        [0,0,0,0,0]#4
    ]
] 
a = 0
for x in range(len(asignaturas_lista)):
    for y in range(len(asignaturas_lista[x])):
        n = 0
        materia = asignatura.get_Nombre(asignaturas_lista[x][y])
        id = asignatura.get_Id(asignaturas_lista[x][y])
        horas = asignatura.get_HorasSemana(asignaturas_lista[x][y])
        grupo = asignatura.get_Grupo(asignaturas_lista[x][y])-1
        while int(n) < int(horas):
            a += 1
            x1 = ran.randrange(len(lista_profesor[x]))
            x2 = ran.randrange(len(lista_profesor[x][x1]))
            if(lista_disponibilidad_salon[grupo][x1][x2] == 1 and lista_profesor[x][x1][x2] == 1 and lista_horario_profesor[x][x1][x2] == 0 and lista_horario_salon[grupo][x1][x2] == 0 ):
                lista_horario_profesor[x][x1][x2] = "%s %s" %(materia, (grupo+1)) 
                lista_horario_salon[grupo][x1][x2] = "%s %s" %(materia, (grupo+1))
                n += 1
            if (a == 10000):
                n = horas
                print("no se encontro horario en esta ocasion")   
if (a < 10000):
    print("horarios profesores")
    for x in range(len(lista_horario_profesor)):
        print("profesor: %s"%(x+1))
        for y in range(len(lista_horario_profesor[x])):
            print(lista_horario_profesor[x][y])
        print("")

    for x in range(len(lista_disponibilidad_salon)):
        print("Grupo: %s" %(x+1))
        for y in range(len(lista_disponibilidad_salon[x])):
            print(lista_horario_salon[x][y])
        print("")
