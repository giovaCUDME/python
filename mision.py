# sacara el dinero del banco

tareas = ['🏦 sacar dinero del banco.',
          '🪣 hacer la colada.',
          '🌳 dar un paseo.',
          '💈 cortarse el cabello',
          '🍵 preparar un te.',
          '💻 terminbar el capitulo de listas.',
          '💖 llamar a mama.',
          '📺 ver dragon ball.']

#1 acceder a la primera tarea de la lista
print(tareas[0])

#2 encontrar la segunda tarea de la lista
print(tareas[1])

#3 obtener un subconjunto de tareas usando slicing (rebanando)
print(tareas[1:4])

#4 error detectado
indice = tareas.index("llamar a papa")

#5 modofica la lista para añadir una nueva tarea
tareas.insert(3,"admirar el paisaje 🏙️")
print(tareas)