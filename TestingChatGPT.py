# Convert the data from counts to m/s
# To-do this, ObsPy offers a method that can be used on Trace objects: .remove_response()
from obspy import read, read_inventory
import matplotlib.pyplot as plt
import numpy as np

st = read("./M7.4R8095.mseed") 



inv = read_inventory("./R8095.xml") # the sample inv is the corresponding inv
                                     # for the sample trace

tr = st[0]
tr_disp = tr.remove_response(inventory=inv, output="DISP", water_level=60, plot=True)
# VEL for velocity, see other possible values # shows velocity in m/s

# Note on the right column of plots, the scale of y-axis changed.
# This is because the data values change from being counts-values to m/s values.

displacement_data = tr_disp.data
displacement_time = tr_disp.times()

plt.figure()
plt.plot(displacement_time, displacement_data)
plt.title("Ground Displacement vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Displacement m")
plt.show()

tr_vel = tr.remove_response(inventory=inv, output="VEL", water_level=60, plot=True)
velocity_data = tr_vel.data
velocity_time = tr_vel.times()

plt.figure()
plt.plot(velocity_time, velocity_data)
plt.title("Ground Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.show()

tr_acc = tr.remove_response(inventory=inv, output="ACC", water_level=60, plot=True)
acceleration_data = tr_acc.data
times = tr_acc.times()

plt.figure()
plt.plot(times, acceleration_data)
plt.title("Ground Acceleration vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.show()

