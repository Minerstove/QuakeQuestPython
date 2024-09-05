from obspy import read
import matplotlib.pyplot as plt

st = read('your_seismic_data.mseed')
st.plot(type="dayplot", title="Seismic Data", vertical_scaling_range=2000, color="black", size=(800, 600))
plt.show() 