import os
import mysql.connector
from menuestudiante import *
from menuasignatura import *
from menumatricula import *

myconexion = mysql.connector.connect(user="root",password="uts123",host="localhost",database="gestionuts",port="3306", auth_plugin='mysql_native_password')

try :

    mypuntero = myconexion.cursor()
    mypuntero.execute("create table asignatura (codigoasig VARCHAR (5) NOT NULL, nombreasig VARCHAR(45) NOT NULL, PRIMARY KEY (codigoasig));")
    print("se creo la tabla asignatura")
    mypuntero.execute("create table estudiante (codigoe VARCHAR (10) NOT NULL, nomestu VARCHAR(45) NOT NULL, PRIMARY KEY(codigoe));")
    print("se creo la tabla estudiante")
    mypuntero.execute("create table matricula (codmatri INT AUTO_INCREMENT, estudiante_codigoe VARCHAR (10) NOT NULL, asignatura_codigoasig VARCHAR(5) NOT NULL, PRIMARY KEY(codmatri), FOREIGN KEY (estudiante_codigoe) REFERENCES estudiante(codigoe), FOREIGN KEY(asignatura_codigoasig) REFERENCES asignatura(codigoasig));")
    print("se creo la tabla matricula")
except:
    print("La base de datos ya existe ")
finally:
    pass

terminar = False
while terminar != True:
    os.system("cls")
    print('\n')
    print("     UNIVERSIDAD UTS - Menu Principal")
    print('')
    print("OPCIONES GESTIÓN ACADEMICA\n")
    print("1...     GESTION ESTUDIANTE")
    print("2...     GESTION ASIGNATURA")
    print("3...     GESTION MATRICULA")
    print("4...     TERMINAR")
    print("Por favor ingrese una opción:    ",end="")
    opcion = input()

    if opcion == "1":
        menuestudiante()

    elif opcion == "2":
        menuasignatura()

    elif opcion == "3":
        menumatricula()

    elif opcion=='4':

        print("Finalizo el programa")
        terminar=True
    else:
        print("\n¡¡Entrada invalida!!\n")

