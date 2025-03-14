import pandas as pd

# Leer el archivo Excel original
df = pd.read_excel('Pedidos (21).xlsx')

# Eliminar todas las columnas excepto 'pedido', 'nombre', 'seller' y 'telefono'
df.drop(columns=df.columns.difference(['pedido', 'nombre', 'seller', 'telefono']), inplace=True)

# Guardar el DataFrame filtrado en un nuevo archivo Excel
output_file = 'Pedidos_filtrado.xlsx'
df.to_excel(output_file, index=False)

print(f"Archivo generado: {output_file}. Ábrelo desde la carpeta de trabajo para descargarlo.")
