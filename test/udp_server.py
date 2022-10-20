
import socket
from datetime import datetime
import json
import http.client

localIP       = "173.212.212.124"
localPort     = 20001
bufferSize    = 1024
msgFromServer = "Hello GPS"
bytesToSend   = str.encode(msgFromServer)

 

def extractGPSData(gpsInfo):
    if(len(gpsInfo.hex())>24):
        gps = gpsInfo.decode("ASCII")
        gps = gps.split(",")
        # print(gps)
        timestamp = int(gps[5])
        gpsDateTime = datetime.fromtimestamp(timestamp).__str__()

        timestamp = int(gps[6])
        rtcDateTime = datetime.fromtimestamp(timestamp).__str__()

        timestamp = int(gps[7])
        sendDateTime = datetime.fromtimestamp(timestamp).__str__()

        longitude = int(gps[8])*0.000001
        latitude = int(gps[9])*0.000001

        heading = int(gps[10])

        reportID = int(gps[11])

        odometer = float(gps[12])*100

        hdop = int(gps[13])*0.1

        inputs = int(gps[14])

        speed = int(gps[15])

        ouputs = int(gps[16])

        analogInputValue = int(gps[17])

        driveID = gps[18]

        ftsv = int(gps[19])

        stsv = int(gps[20])

        message = gps[21]

        gpsdata = "GPS DateTime: {},RTC DateTime: {},SEND DateTime: {}, Longitude :{}, Latitude {}".format(gpsDateTime, rtcDateTime, sendDateTime, longitude, latitude)
        print(gpsdata)
        url = "173.212.212.124:8080"

        conn = http.client.HTTPConnection(url)

        headers = {'Content-type': 'application/json'}

        foo = {
            "gpsDateTime":gpsDateTime,
            "rdcDateTime":rtcDateTime,
            "sendDateTime":sendDateTime,
            "longitude":longitude,
		"latitude":latitude
              }
        json_data = json.dumps(foo)
        print(json_data)
        conn.request('POST', '/back/gps',json_data,headers)

        response = conn.getresponse()
        print(response.read().decode())
        
    else:
        clientMsg = "EMEI:{}".format(int(gpsInfo.hex()[4:20],16))
        print(clientMsg)
        # other = "Message Normal:{}".format(gps)
def send(UDPServerSocket, message, address):
    UDPServerSocket.sendto(message,address)
    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)

def runServer():
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")
    # Listen for incoming datagrams
    while(True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]
        extractGPSData(message)
        send(UDPServerSocket, message, address)
        
if __name__ == "__main__":
    runServer()