def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    # Devuelve el monto del descuento
    return descuento

# Llamada 1: Solo monto total, usa el valor predeterminado de descuento (10%)
monto_compra_1 = 300
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

# Llamada 2: Monto total y porcentaje de descuento (20%)
monto_compra_2 = 400
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Mostrar los resultados
print(f"Compra 1 - Monto total: {monto_compra_1}, Descuento: {descuento_1}, Monto final a pagar: {monto_final_1}")
print(f"Compra 2 - Monto total: {monto_compra_2}, Descuento: {descuento_2}, Monto final a pagar: {monto_final_2}")