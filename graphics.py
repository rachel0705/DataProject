import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta al CSV limpio
csv_path = 'cleaned_music_data.csv'

# Cargar los datos
df = pd.read_csv(csv_path)

# Crear carpeta para guardar las gráficas
output_dir = 'graficas_generadas'
os.makedirs(output_dir, exist_ok=True)

# 1. Top 10 artists con más canciones
plt.figure(figsize=(10, 6))
df['artist_name'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Artistas con Más Canciones")
plt.ylabel("Número de Canciones")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/top_artistas.png")
plt.close()

# 2. Mapa de calor de correlaciones (variables numéricas)
correlation = df.select_dtypes(include=['float64', 'int64']).corr()
if not correlation.empty:
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Mapa de Calor de Correlaciones")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/correlaciones_heatmap.png")
    plt.close()

print(f"✅ ¡Gráficas generadas con éxito! Revisa la carpeta: {output_dir}")
