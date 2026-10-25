#print('Hola') Será mi recuerdo para mi primer proyecto 

tareas = ['entrenar', 'meditar', 'dormir']

#print(tareas)
#Gracias Claude
print("menú:\n1. salir\n2. agregar\n3. ver\n4. eliminar\n")

while True: 
  pregunta = input("¿Qué quieres hacer primero?")
  if pregunta == "salir":
    print("Nos vemos para la proxima tarea!")
    break
  elif pregunta == "agregar":
    nueva_tarea = input("¿Qué quieres agregar?")
    tareas.append(nueva_tarea)
  elif pregunta == "ver":
    for indice, tarea in enumerate(tareas):
      print(f"{indice + 1}. {tarea}")
      '''
      Índice va tomando los valores 0, 1, 2...
      Tarea va tomando 'entrenar', 'meditar', 'dormir'...
      El f"{indice + 1}. {tarea}" es un f-string: te deja meter variables directamente dentro de un texto usando {}. La f antes de las comillas es lo que activa ese poder. índice + 1 es solo para que empiece en 1 en vez de 0.
      '''
    #print(enumerate(tareas))
    #<enumerate object at 0x7fe5a179fd30> 
    #no es un error pero no da el resultado deseado
  elif pregunta == "eliminar":
    eliminar_tarea = input("¿Qué quieres eliminar?")
    try:
      eliminar_tarea = int(eliminar_tarea)-1
      del tareas[eliminar_tarea]
    except:
      print("Eso no es un número válido, intenta de nuevo")
  else: 
    print("Intenta de nuevo, elige una opción del menú")

#for tarea in tareas:
#    print(tarea)