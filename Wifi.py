def connect():
    import network
 
    ssid = "Lucas"
    password =  "984323674"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
