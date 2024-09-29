from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import argparse
station_list = ["R3B2D","R1EFC","RBD68","RF8C0"]

def main(stations):
  try:
    rs = Client('https://stationview.raspberryshake.org', _discover_services=False)
    for station in stations:    
      inv = rs.get_stations(network='AM', station=station, level='RESP')

      # Save the instrument response information into an XML file
      inv.write(station + ".xml", format="STATIONXML")

      # Print a message indicating the successful retrieval and saving of the instrument response files
      print(f"[\033[92m OK \033[0m] ", end='')
      print(f"Instrument response files for station '{station}' have been successfully retrieved and saved")
      print(f"- XML metadata: {station}_inst_resp_file.xml")

  except Exception as e:
    # Handle any exceptions that occur during execution
    print(f"[\033[91m ERROR \033[0m] ", end='')
    print(f"{e}")

main(station_list)

"""parser = argparse.ArgumentParser(description="Retrieve and save instrument response files for a specified station.")
parser.add_argument("station_name" , help="Name of the station you want to get the instrument response file of")
args = parser.parse_args()
main(args.station_name)"""