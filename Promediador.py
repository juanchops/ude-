print ("""¡Bienvenido! En esta aplicación los estudiantes 
podrán gestionar las notas de su materia.""")

student = input('Por favor ingrese su nombre: ')
subject = input('Ingrese el nombre de la materia: ')

subjectPercentage = 0
finalGrade = 0
faltaAñadir = 'S'

while faltaAñadir == 'S':

    gradePercentage = 0

    grade = eval(input('Ingrese la nota obtenida: '))
    gradePercentage = eval(input('Ingrese el porcentaje de la nota: '))
     
    if (subjectPercentage + gradePercentage) <= 100:
        subjectPercentage = subjectPercentage + gradePercentage
        finalGrade = finalGrade + ((grade * gradePercentage)/100)
   
        if subjectPercentage == 100:
            
            finalGrade = round(finalGrade,2)
            student = student.capitalize()
            subject = subject.capitalize()

            if finalGrade >= 3:
                outcome = "aprobado"
            elif finalGrade < 3:
                outcome = "reprobado"
            
            print(f'El estudiante {student} cursó la materia {subject} y obtuvo {finalGrade} resultando en {outcome}')
            break
            
        faltaAñadir = input('¿Falta añadir notas? S/N ')
        if faltaAñadir == 'N':

            finalGrade = round(finalGrade,2)
            student = student.capitalize()
            subject = subject.capitalize()

            if finalGrade >= 3:
                outcome = "aprobado"
            elif finalGrade < 3:
                outcome = "reprobado"
            
            print(f'El estudiante {student} cursó la materia {subject} y obtuvo {finalGrade} resultando en {outcome}')
            break
    else:
        print('El porcentaje evaluado de una materia no puede ser mayor a 100')

    
