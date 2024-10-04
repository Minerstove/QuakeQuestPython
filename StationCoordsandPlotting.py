import csv
from obspy import read_inventory
import matplotlib.pyplot as plt
import os
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

# Specify the directory where all the inventory files are stored
directory = input("What directory in the Earthquake Data Folder are you accessing? ")
inventory_dir = f'./EarthquakeData/{directory}'  # Directory containing station inventory files

# Initialize lists to store station names and coordinates
station_data = {}  # Dictionary to store unique stations with their coordinates

# Loop through all the XML files in the directory (assuming .xml files)
for file in os.listdir(inventory_dir):
    if file.endswith(".xml"):
        # Load each inventory file
        inv = read_inventory(os.path.join(inventory_dir, file))
        
        # Extract coordinates for each station in the inventory
        for network in inv:
            for station in network:
                # Only add unique stations
                if station.code not in station_data:
                    station_data[station.code] = (station.latitude, station.longitude)

# Print the station names and coordinates
for name, (lat, lon) in station_data.items():
    print(f"Station: {name}, Latitude: {lat}, Longitude: {lon}")

# Assuming earthquake data is stored in a file called 'earthquake_data.csv' in the same directory
earthquake_file = os.path.join(inventory_dir, 'EQData.csv')

# Initialize earthquake_lat and earthquake_lon
earthquake_lat = None
earthquake_lon = None

# Read the CSV file to extract earthquake latitude and longitude
with open(earthquake_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the columns are named 'Latitude' and 'Longitude'
        earthquake_lat = float(row['Latitude'])
        earthquake_lon = float(row['Longitude'])
        break  # Assuming you only need the first earthquake event

# Print the extracted earthquake coordinates
print(f"Extracted Earthquake Location: Latitude={earthquake_lat}, Longitude={earthquake_lon}")

# Generate a colormap with as many colors as there are stations
num_stations = len(station_data)
colors = plt.cm.rainbow(np.linspace(0, 1, num_stations))

# Plot using Cartopy
plt.figure(figsize=(12, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([115, 130, 5, 20], crs=ccrs.PlateCarree())

# Add coastlines and other features
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='aqua')

# Plot unique station locations as red dots with varying colors and label with station names
for (name, (lat, lon)), color in zip(station_data.items(), colors):
    plt.scatter(lon, lat, color=color, marker='o', s=50, transform=ccrs.PlateCarree(), label=name)

# Plot earthquake location as a blue star
earthquake = plt.scatter(earthquake_lon, earthquake_lat, color='blue', marker='*', s=200, transform=ccrs.PlateCarree(), label='Earthquake Event')

# Add a legend to distinguish stations from the earthquake
plt.legend()

# Add a title and show the map
plt.title("Station Locations and Earthquake Event")
plt.show()
