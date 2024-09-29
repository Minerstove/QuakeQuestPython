from obspy.clients.fdsn import Client
from obspy import UTCDateTime

client = Client("RASPISHAKE", _discover_services=False)

start_time=UTCDateTime(2024,8,1)
end_time=UTCDateTime()

class PhilippineTerritory:
    minlatitude = 5
    maxlatitude = 21
    minlongitude = 114
    maxlongitude = 130

def stationDataGrabber():
    inventory = client.get_stations(network="AM",station="R*",
                                    minlatitude=PhilippineTerritory.minlatitude,
                                    maxlatitude=PhilippineTerritory.maxlatitude,
                                    minlongitude=PhilippineTerritory.minlongitude,
                                    maxlongitude=PhilippineTerritory.maxlongitude,level="channel",
                                    starttime=start_time,endtime=end_time)
    print(inventory)

def waveFormfunc():
    st = client.get_waveforms("AM", "R3B2D", "00", "EHZ", start_time, start_time + 60 * 60)
    st.plot() 

def testingshit():
    client = Client("IRIS")
    t = UTCDateTime("2010-02-27T06:45:00.000")
    st = client.get_waveforms("IU", "ANMO", "00", "LHZ", t, t + 60 * 60)
    st.plot() 

#testingshit()
#stationDataGrabber()
waveFormfunc()