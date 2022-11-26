from CRUD import *
import os

def menuestudiante():
    os.system("cls")
    terminar = False
    while terminar != True:
        print("\n     UNIVERSIDAD UTS\n")
        print("OPCIONES estudiante\n")
        print("1...     CREAR ESTUDIANTE")
        print("2...     ELIMINAR ESTUDIANTES")
        print("3...     IMPRIMIR ESTUDIANTES")
        print("4...     REGRESAR")
        opcion = input("Por favor ingrese una opción:    ")
        
        if opcion == "1":

            insertarEstudiante()

        elif opcion == "2":

            eliminarEstudiante()

        elif opcion == "3":

            impimirEstudiantes()

        elif opcion == "4":
            terminar=True
        else:
            print("\n¡¡Entrada invalida!!\n")


