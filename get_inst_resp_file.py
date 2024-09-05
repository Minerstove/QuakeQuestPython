from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import argparse

def main(station_name):
  try:
    rs = Client('https://stationview.raspberryshake.org', _discover_services=False)

    inv = rs.get_stations(network='AM', station=station_name, level='RESP')

    fig = inv.plot_response(0.001, station=station_name, show=False, time=UTCDateTime.now())

    # Save the instrument response plot into a PNG file
    fig.set_size_inches(12, 8)  # Set the output size
    fig.savefig(station_name + "_inst_resp_file.png", dpi=300) 

    # Save the instrument response information into an XML file
    inv.write(station_name + "_inst_resp_file.xml", format="STATIONXML")

    # Print a message indicating the successful retrieval and saving of the instrument response files
    print(f"[\033[92m OK \033[0m] ", end='')
    print(f"Instrument response files for station '{station_name}' have been successfully retrieved and saved")
    print(f"- PNG plot: {station_name}_inst_resp_plot.png")
    print(f"- XML metadata: {station_name}_inst_resp_file.xml")

  except Exception as e:
    # Handle any exceptions that occur during execution
    print(f"[\033[91m ERROR \033[0m] ", end='')
    print(f"{e}")


parser = argparse.ArgumentParser(description="Retrieve and save instrument response files for a specified station.")
parser.add_argument("station_name" , help="Name of the station you want to get the instrument response file of")
args = parser.parse_args()
main(args.station_name)