from random import shuffle

tipos_cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
n_palos = 4

def generar_baraja(tipos_cartas, n_palos):

  baraja = tipos_cartas * n_palos

  shuffle(baraja)

  def convert(baraja):
    return tuple(baraja)

  baraja = convert(baraja)
  return baraja

print(generar_baraja(tipos_cartas, n_palos))