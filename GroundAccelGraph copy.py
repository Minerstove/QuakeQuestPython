from obspy import read, read_inventory
import matplotlib.pyplot as plt
import numpy as np
from obspy.signal.freqattributes import peak_ground_motion

#st = read("./M7.4.mseed")  # You can also use web services to load data
#inv = read_inventory("./R1382.xml")
st = read("./EarthquakeData/SurigaoEarthquakeDataM74/M7.4R8D68.mseed")
inv = read_inventory("./EarthquakeData/SurigaoEarthquakeDataM74/R8D68.xml")
#st = read("./M7.4R8095.mseed")
#inv = read_inventory("./R8095.xml")

tr1 = st[0]
tr2 = st[0]

tr_vel = tr1.remove_response(inventory=inv, output="VEL") # shows velocity in m/s # VEL for velocity, see other possible values
tr_acc = tr2.remove_response(inventory=inv, output="ACC") # shows accel in m/s^2

pga = np.max(np.abs(tr_acc.data))

pgm = peak_ground_motion(tr1, 0.01, 1.0) #PGA returned is what is at the frequency value

acceleration_data = tr_acc.data
times = tr_acc.times()

print(f"Peak Ground Acceleration (PGA): {pga} m/s^2")
print(f"Peak Ground Acceleration (PGA) in g: {pga / 9.81} g") #Measured in g (standard)

print(f"Peak Ground Acceleration (PGA): {pgm[1]} m/s^2")
print(f"Peak Ground Acceleration (PGA) in g: {pgm[1] / 9.81} g") #Measured in g (standard)

plt.figure()
plt.plot(times, acceleration_data)
plt.title("Ground Acceleration vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.grid()
plt.show()

velocity_data = tr_vel.data
velocity_time = tr_vel.times()

plt.figure()
plt.plot(velocity_time, velocity_data)
plt.title("Ground Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.show()

"""
To do:
Find relationship between PGA and Intensity using Philippine sources
Find intensity impact
"""