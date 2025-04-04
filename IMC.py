peso=float(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))
imc=peso/(altura*altura)
imc_redon=round(imc,2)
if imc_redon<18.5:
    clasificacion="Bajo peso"
elif 18.5<=imc_redon<24.9:
    clasificacion="Peso normal"
elif 24.9<=imc_redon<29.9:
    clasificacion="Sobrepeso"
else: clasificacion="Obesidad"
print("Su peso es de ", peso, "kg")
print("Su altura es de ", altura, "m")
print("Su índice de masa corporal es  ", imc_redon)
print("Clasificacion: ", clasificacion)