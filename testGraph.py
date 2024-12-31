import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np

# Load the shapefile (replace with your actual file path)
shapefile_path = './moShape.shp'
missouri = gpd.read_file(shapefile_path)

# Plot the shape of Missouri
fig, ax = plt.subplots(figsize=(10, 8))
missouri.plot(ax=ax, color='lightblue', edgecolor='black')

ax.set_title('Graph Shaped Like Missouri', fontsize=16)
ax.legend()

plt.show()
