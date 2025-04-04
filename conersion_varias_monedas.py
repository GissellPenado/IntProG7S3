dolares=float(input("Ingrese la cantidad en dolares: "))
cambio_euro=(float(input("Ingrese la tasa de cambio de dolares a euros: ")))
cambio_libras=float(input("Ingrese la tasa de cambio de dolares a libras: "))
cambio_yenes=float(input("Ingrese la tasa de cambio de dolares a yenes: "))
cantidad_euro=dolares*cambio_euro
cantidad_libras=dolares*cambio_libras
cantidad_yenes=dolares*cambio_yenes
print("Dolares: ", dolares)
print("Euros: ",cantidad_euro)
print("Libras: ", cantidad_libras)
print("Yenes: ", cantidad_yenes)