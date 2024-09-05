from obspy import read_inventory
inv=read_inventory("your_station_metadata.xml")
print(inv)