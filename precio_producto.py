precio_original=float(input("Ingrese el precio original del producto: "))
porcentaje=float(input("Ingrese el porcentaje de descuento del producto: "))
precio_descuento=precio_original-((precio_original*porcentaje)/100)
iva=float(input("Ingresar el porcentaje de IVA: "))
precio_final=((precio_descuento*iva)/100)+precio_descuento
print("El precio original es de: ", precio_original)
print("El descuento aplicado es de: ", (precio_original*porcentaje)/100)
print("El IVA es de: ", (precio_descuento*iva)/100 )
print("El precio final es de: ", precio_final)