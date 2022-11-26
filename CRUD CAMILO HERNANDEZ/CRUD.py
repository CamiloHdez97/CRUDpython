import mysql.connector

global myconexion

myconexion = mysql.connector.connect(user="root",password="uts123",host="localhost",database="gestionuts",port="3306", auth_plugin='mysql_native_password')


#--------------------------------------ESTUDIANTES-----------------------------------


def impimirEstudiantes():

    mcursor=myconexion.cursor()
    mcursor.execute("SELECT * FROM estudiante")
    registros = mcursor.fetchall()
    myconexion.commit()
    print("\n----------Listado Estudiantes:---------\n\n    Codigo   |   Nombre\n")
    for row in registros:
        print(row)

def insertarEstudiante():

    mcursor = myconexion.cursor()
    CC=input("Ingrese el documento de identidad: ")
    print("")
    NOM = input("Ingrese el nombre: ")
    NOM = NOM.upper()
    mcursor.execute('insert into estudiante(codigoe,nomestu) values(%s,%s)',(CC,NOM))
    myconexion.commit()
    print("Se inserto el estudiante: "+NOM)

def eliminarEstudiante():

    mcursor = myconexion.cursor()  
    impimirEstudiantes()   
    CC=input("\nEliminar: para Cancelar oprima (C)\nDigite el codigo del estudiante: ")
    if CC.upper() != 'C':
        mcursor.execute("delete from estudiante where codigoe='"+str(CC)+"'")
        myconexion.commit()
        print("Se elimino el estudiante "+CC)
        impimirEstudiantes() 
    else:
        print('Cancelada eliminación por el usuario.')


#---------------------------------------ASIGNATURAS----------------------------------------
def imprimirAsignatura():

    mcursor=myconexion.cursor()
    mcursor.execute("SELECT * FROM asignatura")
    registros = mcursor.fetchall()
    myconexion.commit()
 
    print("\n----------Listado de Asignaturas:---------\n\n    Codigo   |   Nombre\n")
    for row in registros:
        print(row)


def insertarAsignatura():

    mcursor = myconexion.cursor()
    CODA=input("Ingrese el codigo de la asignatura: ")
    print("")
    NOMA= input("Ingrese el nombre de la asignatura: ")
    NOMA = NOMA.upper()
    mcursor.execute('insert into asignatura(codigoasig,nombreasig) values(%s,%s)',(CODA,NOMA))
    myconexion.commit()
    print("Se inserto la asignatura: "+NOMA)


def eliminarAsignatura():

    mcursor = myconexion.cursor()  
    imprimirAsignatura()   
    CODA=input("\nEliminar: para Cancelar oprima (C)\nIngrese el codigo de la asignatura: ")
    if CODA.upper() != 'C':
        mcursor.execute("delete from asignatura where codigoasig='"+str(CODA)+"'")
        myconexion.commit()
        print("Se elimino la asignatura: Cod:"+CODA)
        imprimirAsignatura()
    else:
        print('Cancelada eliminación por el usuario.')

#-----------------------------------------MATRICULA----------------------------------------------
def impimirMatricula():

    mcursor=myconexion.cursor()
    mcursor.execute("SELECT matricula.codmatri, estudiante.codigoe, estudiante.nomestu, asignatura.nombreasig from matricula inner join estudiante on estudiante.codigoe=matricula.estudiante_codigoe inner join asignatura on asignatura.codigoasig=matricula.asignatura_codigoasig;")
    registros = mcursor.fetchall()
    myconexion.commit()
    print("\n----------Listado Matriculas:---------\n\n ID | Cod Estud | Nombre Estudiante | Asignatura\n")
    for row in registros:
        print(row)

def insertarMatricula():

    mypuntero = myconexion.cursor()
    impimirEstudiantes() 
    CODA=input("\nIngrese el codigo del estudiante para matricular: ")
    print("")
    imprimirAsignatura()  
    NOMA= input("\nIngrese el codigo de la materia a matricular: ")
    NOMA = NOMA.upper()
    mypuntero.execute('insert into matricula(estudiante_codigoe, asignatura_codigoasig) values(%s,%s)',(CODA,NOMA))
    myconexion.commit()
    print("Se inserto la matricula: "+NOMA)

def eliminarMatricula():

    mypuntero = myconexion.cursor()  
    impimirMatricula()  
    CODM=input("\nEliminar: para Cancelar oprima (C)\nIngrese el ID Matricula : ")
    if CODM.upper() != 'C':
        mypuntero.execute("delete from matricula where codmatri='"+str(CODM)+"'")
        myconexion.commit()
        print("Se elimino la matricula: Cod:"+CODM)
    else:
        print('Cancelada eliminación por el usuario.')