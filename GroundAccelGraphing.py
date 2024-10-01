import os
from obspy import read, read_inventory
import matplotlib.pyplot as plt
import numpy as np
from obspy.signal.freqattributes import peak_ground_motion

# Function to find matching pairs of .mseed and .xml files in the given directory
def find_file_pairs(directory):
    mseed_files = [f for f in os.listdir(directory) if f.endswith(".mseed")]
    xml_files = [f for f in os.listdir(directory) if f.endswith(".xml")]

    # Match files with the same name (without extensions)
    file_pairs = []
    for mseed_file in mseed_files:
        base_name = os.path.splitext(mseed_file)[0]
        xml_file = base_name + ".xml"
        if xml_file in xml_files:
            file_pairs.append((os.path.join(directory, mseed_file), os.path.join(directory, xml_file)))
    
    return file_pairs

# Main function to read data, process it, and generate plots for each pair of files
def process_seismic_data(directory):
    # Find matching pairs of MSEED and XML files
    file_pairs = find_file_pairs(directory)
    
    if not file_pairs:
        print("No matching MSEED and XML files found in the directory.")
        return
    
    # Loop through each file pair and process them
    for mseed_file, xml_file in file_pairs:
        print(f"Processing MSEED file: {mseed_file}")
        print(f"Using corresponding XML file: {xml_file}")
        
        # Load the seismic data and inventory
        st = read(mseed_file)
        inv = read_inventory(xml_file)

        # Process the first trace for analysis
        tr = st[0]

        # Make copies of the trace for each type of output (displacement, velocity, acceleration)
        tr_disp = tr.copy().remove_response(inventory=inv, output="DISP")
        tr_vel = tr.copy().remove_response(inventory=inv, output="VEL")
        tr_acc = tr.copy().remove_response(inventory=inv, output="ACC")

        # Calculate Peak Ground Acceleration (PGA) and use frequency-based peak ground motion
        pga = np.max(np.abs(tr_acc.data))
        pgm = peak_ground_motion(tr_vel, 0.01, 1.0)  # Can be tuned for your needs

        # Displacement data plotting
        displacement_data = tr_disp.data
        displacement_time = tr_disp.times()

        plt.figure()
        plt.plot(displacement_time, displacement_data)
        plt.title(f"Ground Displacement vs Time ({os.path.basename(mseed_file)})")
        plt.xlabel("Time (s)")
        plt.ylabel("Displacement (m)")
        plt.grid()

        # Velocity data plotting
        velocity_data = tr_vel.data
        velocity_time = tr_vel.times()

        plt.figure()
        plt.plot(velocity_time, velocity_data)
        plt.title(f"Ground Velocity vs Time ({os.path.basename(mseed_file)})")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.grid()

        # Acceleration data plotting
        acceleration_data = tr_acc.data
        acceleration_time = tr_acc.times()

        plt.figure()
        plt.plot(acceleration_time, acceleration_data)
        plt.title(f"Ground Acceleration vs Time ({os.path.basename(mseed_file)})")
        plt.xlabel("Time (s)")
        plt.ylabel("Acceleration (m/s²)")
        plt.grid()

        # Display Peak Ground Acceleration (PGA) results
        print(f"Peak Ground Acceleration (PGA): {pga} m/s²")
        print(f"Peak Ground Acceleration (PGA) in g: {pga / 9.81} g")
        print(f"Frequency-based Peak Ground Motion (PGA): {pgm[1]} m/s²")
        print(f"Frequency-based Peak Ground Motion (PGA) in g: {pgm[1] / 9.81} g")

        # Show plots for each file
        plt.show()

# Input the specific subdirectory within the parent directory
parent_directory = "./EarthquakeData"
subdirectory = input(f"Please enter the subdirectory within '{parent_directory}' where the seismic data is located: ")

# Construct the full path to the subdirectory
full_directory = os.path.join(parent_directory, subdirectory)

# Process the seismic data in the selected subdirectory
if os.path.exists(full_directory) and os.path.isdir(full_directory):
    process_seismic_data(full_directory)
else:
    print(f"Error: The directory '{full_directory}' does not exist or is not a valid directory.")
