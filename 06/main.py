archivo = open("input.txt")


def find_start_of_packet4(data):
  pos = 0
  while pos <= len(data):
    pos += 1
	# Comprueba si el caracter es un inicio de paquete
	# Si es asi, devuelve la posicion en la que se encuentra
	# Si no, continua buscando 
	# set() devuelve un conjunto de elementos unicos
    if len(set(data[pos-4:pos])) == 4: 
       print(pos)
       return pos
  # Si no se encuentra ningun inicio de paquete, devuelve -1
  return -1

def find_start_of_packet14(data):
  pos = 0
  while pos <= len(data):
    pos += 1
	# Comprueba si el caracter es un inicio de paquete
	# Si es asi, devuelve la posicion en la que se encuentra
	# set() devuelve un conjunto de elementos unicos
    if len(set(data[pos-14:pos])) == 14: 
       print(pos)
       return pos
  # Si no se encuentra ningun inicio de paquete, devuelve -1
  return -1

data = archivo.read()

print("star1: ", find_start_of_packet4(data))
print("star2: ", find_start_of_packet14(data))
 

archivo.close()










	

