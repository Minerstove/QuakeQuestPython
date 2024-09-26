from obspy import read

# Load the seismic waveform data from the MiniSEED file
st = read("./M7.4.mseed")  # Replace with your file path

# Get the first Trace object from the Stream
tr = st[0]

# Access the start time (UTCDateTime object)
event_start_time = tr.stats.starttime
event_end_time = tr.stats.endtime

# Print the event start time
print(f"Event Start Time (UTC): {event_start_time}")
print(f"Event End Time (UTC): {event_end_time}")