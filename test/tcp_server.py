import socket
from datetime import datetime
import json
import http.client

LOCALHOST = "173.212.212.124"
PORT = 5044

print("Server started")
print("Waiting for client request..")

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
        url = "ptsv2.com"

        conn = http.client.HTTPConnection(url)

        headers = {'Content-type': 'application/json'}

        foo = {
            "gps_dt":gpsDateTime,
            "rtc_dt":rtcDateTime,
            "send_dt":sendDateTime,
            "ltd":latitude,
            "lng":longitude,
            "heading": heading,
            "reportID": reportID,
            "odometer": odometer,
            "hdop": hdop,
            "inputs":inputs,
            "speed": speed,
            "ouputs": ouputs,
            "analogInputValue": analogInputValue,
            "driveID": driveID,
            "ftsv": ftsv,
            "stsv": stsv,
            "message": message
        }
        json_data = json.dumps(foo)
        # print(json_data)
        conn.request('POST', '/t/7mey0-1662476783/post', json_data, headers)

        response = conn.getresponse()
        print(response.read().decode())
        
    else:
        clientMsg = "EMEI:{}".format(int(gpsInfo.hex()[4:20],16))
        print(clientMsg)
        # other = "Message Normal:{}".format(gps)
def send(serverSocket, message, address):
    serverSocket.send(message)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(10)
while True:
    clientConnection,clientAddress = server.accept()
    print("Connected client :" , clientAddress)
    # try:
    in_data = clientConnection.recv(1024)
    print("Client data:" , in_data)
    clientConnection.sendall(in_data)
    if(len(in_data.hex())>24):
        gps = in_data.decode("ASCII")
        print(gps)
        clientConnection.close()
    else:
        clientMsg = "EMEI:{}".format(int(in_data.hex()[4:20],16))
        print(clientMsg)
    
#   clientConnection.close()
  # extractGPSData(in_data)
  # send(clientConnection, in_data, clientAddress)
  # except:
  #   print("Disconnected client")
  # msg = in_data.decode()