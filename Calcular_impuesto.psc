Proceso Calcular_impuesto
	definir precio, porc_impuesto, valor_imp, total_pago Como Real;
	escribir "Dime el precio del producto";
	leer precio;
	escribir "Dime el porcentaje de impuesto a aplicar";
	leer porc_impuesto;
	porc_impuesto=porc_impuesto/100;
	valor_imp=precio*porc_impuesto;
	total_pago=precio+valor_imp;
	escribir "Precio original: ",precio;
	escribir "Porcentaje del impuesto: ", porc_impuesto;
	escribir "Pago total: ", total_pago;
	
FinProceso
