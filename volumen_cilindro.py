radio=float(input("Ingrese el radio del cilindro: "))
altura=float(input("Ingrese la altura del cilindro: "))
area_base=(3.1416*radio**2)
volumen=area_base*altura
area_lateral=2*3.1416*radio*altura
area_superficial=area_lateral+(2*area_base)
print("/////////////////////////////////////////")
print("Radio ingresado: ", radio)
print("Altura ingresada: ", altura)
print("Volumen calculado: ", round(volumen,2))
print("Area superficial: ", round(area_superficial,2))