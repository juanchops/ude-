b = 5
n = 3

def solucion(b,n):
    counter = 0

    guess = eval(input('Ingrese un número: '))

    while guess != n or guess == n:

        if guess > b or guess < 0:
            print('¡Te saliste del intervalo!')
        elif guess > n and guess <= b:
            counter = counter + 1
            print ('¡Ups! Te pasaste')
        elif guess < n and guess >= 0:
            counter = counter + 1
            print ('¡Ups! Estás por debajo')
        elif guess == n:
            counter = counter + 1
            print(f'¡LO LOGRASTE! Usaste {counter} intentos')
            break
        
        guess = eval(input('Ingrese un número: '))



    
