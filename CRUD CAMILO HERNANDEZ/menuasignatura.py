from CRUD import *
import os
def menuasignatura():
    os.system("cls")
    terminar = False
    while terminar != True:
        print("\n     UNIVERSIDAD UTS\n")
        print("OPCIONES ASIGNATURAS\n")
        print("1...     CREAR ASIGNATURAS")
        print("2...     ELIMINAR ASIGNATURAS")
        print("3...     IMPRIMIR ASIGNATURAS")
        print("4...     REGRESAR")
        opcion = input("Por favor ingrese una opción:    ")
        
        if opcion == "1":

            insertarAsignatura()

        elif opcion == "2":

            eliminarAsignatura()

        elif opcion == "3":
            imprimirAsignatura()

        elif opcion == "4":
            terminar=True
        else:
            print("\n¡¡Entrada invalida!!\n")


