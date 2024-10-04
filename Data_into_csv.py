import os
import pandas as pd
from obspy import read

# Define the directory containing the mseed files
chosen_directory = input("Choose a directory: ")
mseed_directory = f'./EarthquakeData/{chosen_directory}'
output_csv_file = f'{chosen_directory}.csv'

# Initialize an empty DataFrame to store the data
all_data = pd.DataFrame()

# Loop through all mseed files in the directory
for filename in os.listdir(mseed_directory):
    if filename.endswith(".mseed"):
        file_path = os.path.join(mseed_directory, filename)
        
        # Read the mseed file using obspy
        stream = read(file_path)
        
        # Loop through traces in the stream
        for trace in stream:
            # Get the trace data
            data = trace.data
            times = trace.times('timestamp')
            
            # Create a DataFrame for this trace
            trace_df = pd.DataFrame({
                'timestamp': times,
                'amplitude': data,
                'station': trace.stats.station,
                'network': trace.stats.network,
                'location': trace.stats.location,
                'channel': trace.stats.channel
            })
            
            # Append to the main DataFrame
            all_data = pd.concat([all_data, trace_df])

# Save the collected data to a CSV file
all_data.to_csv(output_csv_file, index=False)

print(f"Data from all mseed files saved to {output_csv_file}")
