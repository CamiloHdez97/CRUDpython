from CRUD import *
import os

def menumatricula():
    os.system("cls")
    terminar = False
    while terminar != True:
        print("\n       UNIVERSIDAD UTS\n")
        print("OPCIONES MATRICULA\n")
        print("1...     MATRICULAR ASIGNATURA A ESTUDIANTE")
        print("2...     ELIMINAR ASIGNATURA A ESTUDIANTE")
        print("3...     IMPRIMIR MATRICULAS")
        print("4...     REGRESAR")
        opcion = input("Por favor ingrese una opción:    ")
        
        if opcion == "1":

            insertarMatricula()

        elif opcion == "2":

            eliminarMatricula()

        elif opcion == "3":
            
            impimirMatricula()

        elif opcion == "4":
            terminar=True
        else:
            print("\n¡¡Entrada invalida!!\n")
            



