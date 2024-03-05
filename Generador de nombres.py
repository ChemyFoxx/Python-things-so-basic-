import random

def generar_nombre():
   
    prefijos = ['name1', 'name2', 'name3', 'name4', 'name5']
    sufijos = ['ap1', 'ap2', 'ap3', 'ap4']

   
    nombre = random.choice(prefijos) + ' ' + random.choice(sufijos)
    return nombre


print("Nombre generado:", generar_nombre())