from obspy import read, read_inventory
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the seismic waveform data
# Load example data from a file or web service
st = read("./M7.4.mseed")  # You can also use web services to load data
tr = st[0]
inv = read_inventory("./R1382.xml")
tr_vel = tr.remove_response(inventory=inv, output="VEL",  water_level=60, plot=True) # shows velocity in m/s # VEL for velocity, see other possible values
tr_acc = tr.remove_response(inventory=inv, output="ACC",  water_level=60, plot=True) #shows accel in m/s^2
#print(tr.stats) print metadata

# Step 2: Check the data to ensure it's in velocity (or displacement) form
#st.plot()  #visualize the original data (velocity)

# Step 3: Differentiate the velocity data to get acceleration
#tr_acc = tr.copy().differentiate()
#print(tr_acc.data[:10])

# Step 4: Find Peak Ground Acceleration
#st_acc.plot()  # Plot the acceleration data
pga = np.max(np.abs(tr_acc.data))

# Step 5: Access the acceleration trace data if needed for further analysis
acceleration_data = tr_acc.data
times = tr_acc.times()

#print peak ground acceleartion
print(f"Peak Ground Acceleration (PGA): {pga} m/s^2")
print(f"Peak Ground Acceleration (PGA) in g: {pga / 9.81} g") #Measured in g (standard)

# Step 6: Plot acceleration vs time (if needed)
plt.figure()
plt.plot(times, acceleration_data)
plt.title("Ground Acceleration vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.show()

#extra check plotting velocity vs time
velocity_data = tr_vel.data
velocity_time = tr_vel.times()

plt.figure()
plt.plot(velocity_time, velocity_data)
plt.title("Ground Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.show()

"""
To do:
Find relationship between PGA and Intensity using Philippine sources
Find intensity impact
"""