counter = 'S'
subtotal = 0

while counter == 'S':
    vUnit = eval(input('Ingrese el valor unitario: '))
    iva = input('¿El valor cuenta con IVA?: ')
    cant = eval(input('Ingrese la cantidad que lleva el cliente del producto a registrar: '))
 
    if iva == "S" :
        subtotal = subtotal + (cant * (vUnit + (vUnit * 0.19)))
        print ('IVA incluído')
        print (f'SUBTOTAL: {subtotal}')
    elif iva == 'N' :
        subtotal = subtotal + (cant * vUnit)
        print ('PRODUCTO SIN IVA')
        print (f'SUBTOTAL: {subtotal}')

    counter = input ('Falta productos por comprar: ')
    if counter == 'N':
        break

print (f'TOTAL A COBRAR: {subtotal}')

