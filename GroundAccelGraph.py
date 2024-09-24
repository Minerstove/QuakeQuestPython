import obspy
from obspy import read
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the seismic waveform data
# Load example data from a file or web service
st = read("./M7.4.mseed")  # You can also use web services to load data
tr = st[0]

#print(tr.stats) print metadata

# Step 2: Check the data to ensure it's in velocity (or displacement) form
st.plot()  #visualize the original data (velocity)

# Step 3: Differentiate the velocity data to get acceleration
st_acc = st.copy().differentiate()
tr_acc=st_acc[0]
print(tr_acc.data[:10])

# Step 4: Find Peak Ground Acceleration
st_acc.plot()  # Plot the acceleration data
pga = np.max(np.abs(tr_acc.data))

# Step 5: Access the acceleration trace data if needed for further analysis
acceleration_data = st_acc[0].data
times = st_acc[0].times()

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
velocity_data = st[0].data
velocity_time=st[0].times()

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