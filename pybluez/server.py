from bluetooth import *

hostMACAddress = 'a8:64:f1:69:9f:82' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
size = 1024
s = BluetoothSocket( RFCOMM )
s.bind((hostMACAddress, port))
s.listen(1)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
client.close()
s.close()