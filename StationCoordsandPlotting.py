from obspy import read_inventory, read
import matplotlib.pyplot as plt
import os
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Specify the directory where all the inventory files are stored
inventory_dir = './'  # Directory containing station inventory files

# Initialize lists to store station names and coordinates
station_names = []
lats = []
lons = []

# Loop through all the XML files in the directory (assuming .xml files)
for file in os.listdir(inventory_dir):
    if file.endswith(".xml"):
        # Load each inventory file
        inv = read_inventory(os.path.join(inventory_dir, file))
        
        # Extract coordinates for each station in the inventory
        for network in inv:
            for station in network:
                station_names.append(station.code)
                lats.append(station.latitude)
                lons.append(station.longitude)

# Print the station names and coordinates
for name, lat, lon in zip(station_names, lats, lons):
    print(f"Station: {name}, Latitude: {lat}, Longitude: {lon}")

#input Earthquake Latitude and Longhitude
earthquake_lon = 126.59
earthquake_lat = 8.44

# Plot using Cartopy
plt.figure(figsize=(12, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([115, 130, 5, 20], crs=ccrs.PlateCarree())

# Add coastlines and other features
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='aqua')

# Plot station locations as red dots
plt.scatter(lons, lats, color='red', marker='o', s=50, transform=ccrs.PlateCarree())
# Plot earthquake location as a blue star
earthquake = plt.scatter(earthquake_lon, earthquake_lat, color='blue', marker='*', s=200, transform=ccrs.PlateCarree(), label='Earthquake Event')

# Add a legend to distinguish stations from the earthquake
plt.legend()

# Add a title and show the map
plt.title("Station Locations and Earthquake Event")
plt.show()