import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load your cleaned CSV file
df = pd.read_csv("cleaned_music_data.csv")

# Create a folder to store the charts
output_dir = "more_charts"
os.makedirs(output_dir, exist_ok=True)

# 1. Top 10 albums with most songs
plt.figure(figsize=(10, 6))
df['release'].value_counts().head(10).plot(kind='bar', color='lightgreen')
plt.title("Top 10 Albums with Most Songs")
plt.ylabel("Number of Songs")
plt.xlabel("Album Title")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_dir}/top_albums.png")
plt.close()

# 2. Boxplot: Artist hotttnesss distribution for top 5 artists
top_artists = df['artist_name'].value_counts().head(5).index
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[df['artist_name'].isin(top_artists)],
            x='artist_name', y='artist_hotttnesss')
plt.title("Artist Hotttnesss Distribution (Top 5 Artists)")
plt.xlabel("Artist")
plt.ylabel("Hotttnesss")
plt.tight_layout()
plt.savefig(f"{output_dir}/artist_hotttnesss_boxplot.png")
plt.close()

# 3. Histogram of artist familiarity
plt.figure(figsize=(10, 6))
df['artist_familiarity'].plot(kind='hist', bins=20, color='orange', edgecolor='black')
plt.title("Distribution of Artist Familiarity")
plt.xlabel("Familiarity")
plt.ylabel("Number of Entries")
plt.tight_layout()
plt.savefig(f"{output_dir}/artist_familiarity_histogram.png")
plt.close()

# 4. Scatter plot: Familiarity vs Hotttnesss
plt.figure(figsize=(10, 6))
plt.scatter(df['artist_familiarity'], df['artist_hotttnesss'], alpha=0.5, color='purple')
plt.title("Familiarity vs Hotttnesss")
plt.xlabel("Artist Familiarity")
plt.ylabel("Artist Hotttnesss")
plt.tight_layout()
plt.savefig(f"{output_dir}/familiarity_vs_hotttnesss_scatter.png")
plt.close()

print(f"✅ Charts generated successfully! Check the folder: {output_dir}")