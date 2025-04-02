salario_bruto=float(input("Ingresar el salario bruto del empleado: "))
impuesto_renta=salario_bruto*0.1
seguro_social=salario_bruto*0.05
fondo_pensiones=salario_bruto*0.03
descuentos=impuesto_renta+seguro_social+fondo_pensiones
salario_neto=salario_bruto-descuentos
print("El salario bruto es: ", salario_bruto)
print("El total de los descuentos es de: ", descuentos)
print("El salario neto es de: ", salario_neto)