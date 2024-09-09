
medida_en_cm = input("Por favor ingresá la medida de la pieza en centímetros: ").replace(',', '.')
medida_en_cm = float(medida_en_cm)

medida_en_pulgadas = medida_en_cm / 2.54

print(f"La medida en pulgadas es: {medida_en_pulgadas:.2f}")

