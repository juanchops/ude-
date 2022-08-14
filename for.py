
estudiante1 = {'cédula': '001', 'nombre': 'Pepito', 'nota_fundamentos': 4.3}
estudiante2 = {'cédula': '002', 'nombre': 'Fulanito', 'nota_fundamentos': 3.2}
estudiante3 = {'cédula': '003', 'nombre': 'Pancho', 'nota_fundamentos': 5}
estudiante4 = {'cédula': '004', 'nombre': 'Rita', 'nota_fundamentos': 4.7}
estudiante5 = {'cédula': '005', 'nombre': 'Pablo', 'nota_fundamentos': 5}

grupo = [estudiante1, estudiante2, estudiante3, estudiante4]

promedio = 0

suma_de_notas = 0

for nota in grupo:
    nota_estudiante = nota['nota_fundamentos']
        
    suma_de_notas = suma_de_notas + nota_estudiante

promedio = suma_de_notas / len(grupo)

print(promedio)