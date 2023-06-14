# to find the address of bluetooth device
import bluetooth
target_name = 'dell'
target_address = None
# list of detected address
detected_address = bluetooth.discover_devices()
for address in detected_address:
    # lookup is to connect to user defined bluetooth name
    if target_name == bluetooth.lookup_name(address):
        target_address = address
        break
if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")
