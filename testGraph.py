import geopandas as gpd
import matplotlib.pyplot as plt
import random

# Load the shapefile (replace with your actual file path)
shapefile_path = './moShape.shp'
missouri = gpd.read_file(shapefile_path)

print(missouri.head(10))

# Add a column for custom colors
# Here, we'll assign a random color to each county
missouri['color'] = [
    f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
    for _ in range(len(missouri))
]

# Plot the shape of Missouri with individual county colors
fig, ax = plt.subplots(figsize=(10, 8))
missouri.plot(ax=ax, color=missouri['color'], edgecolor='black')

ax.set_title('Graph Shaped Like Missouri with Individual County Colors', fontsize=16)

plt.show()
