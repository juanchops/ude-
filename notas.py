
estudiante1 = {'cédula': '001', 'nombre': 'Pepito', 'nota_fundamentos': 4.3}
estudiante2 = {'cédula': '002', 'nombre': 'Fulanito', 'nota_fundamentos': 3.2}
estudiante3 = {'cédula': '003', 'nombre': 'Pancho', 'nota_fundamentos': 5}
estudiante4 = {'cédula': '004', 'nombre': 'Rita', 'nota_fundamentos': 4.7}
estudiante5 = {'cédula': '005', 'nombre': 'Pablo', 'nota_fundamentos': 5}

grupo = [estudiante1, estudiante2, estudiante3, estudiante4]


def calcular_promedio_y_cuadro_honor(grupo):
    promedio = 0

    suma_de_notas = 0

    for nota in grupo:
        nota_estudiante = nota['nota_fundamentos']
            
        suma_de_notas = suma_de_notas + nota_estudiante

    promedio = suma_de_notas / len(grupo)

    primer_puesto = []
    sdo_puesto = []
    tcer_puesto = []
    mejor_nota = 0
    sda_mejor_nota = 0
    tra_mejor_nota = 0

    ## primer puesto
    for i in grupo:
        nota1 = i['nota_fundamentos']
        
        if nota1 > mejor_nota:
            mejor_nota = nota1
            cedula_student = i['cédula']
            primer_puesto = [cedula_student]
                
    for i in grupo:
        otra_nota = i['nota_fundamentos']
        cedula_student = i['cédula']

        if otra_nota == mejor_nota and cedula_student != primer_puesto[0]:
            primer_puesto += [cedula_student]

    ## segundo puesto
    for i in grupo:
        nota1 = i['nota_fundamentos']

        if nota1 < mejor_nota and nota1 > sda_mejor_nota:
            sda_mejor_nota = nota1
            cedula_student = i['cédula']
            sdo_puesto = [cedula_student]

    for i in grupo:
        otra_nota = i['nota_fundamentos']

        if otra_nota == sda_mejor_nota:
            cedula_student = i['cédula']

        if cedula_student != sdo_puesto[0]:
            sdo_puesto += [cedula_student]

    ## tercer puesto
    for i in grupo:
        nota1 = i['nota_fundamentos']

        if nota1 < sda_mejor_nota and nota1 > tra_mejor_nota:
            tra_mejor_nota = nota1
            cedula_student = i['cédula']
            tcer_puesto = [cedula_student]

    for i in grupo:
        otra_nota = i['nota_fundamentos']

        if otra_nota == tra_mejor_nota:
            cedula_student = i['cédula']
            
            if cedula_student != tcer_puesto[0]:
                tcer_puesto += [cedula_student]

    cuadro_honor = {1:primer_puesto, 2:sdo_puesto, 3:tcer_puesto}

    return (promedio, cuadro_honor)