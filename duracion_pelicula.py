duracion_pelicula=int(input("Ingrese la duracion de la pelicula en minutos: "))
duracion_comerciales_previos=int(input("Ingrese la duracion de los comerciales previos: "))
cantidad_pausas_comerciales=int(input("Ingrese la cantidad de pausas comerciales durante la pelicula: "))
duracion_pausas_comerciales=int(input("Ingrese la duracion de cada pausa comercial: "))
total_comerciales=cantidad_pausas_comerciales*duracion_pausas_comerciales
duracion_total=duracion_pelicula+duracion_comerciales_previos+total_comerciales
print("Duracion original de la pelicula: ", duracion_pelicula)
print("Duracion total de los comerciales: ", total_comerciales)
print("Tiempo total de la proyeccion: ", duracion_total)