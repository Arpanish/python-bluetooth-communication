import socket

serverMACAddress = '5C:BA:EF:AF:DD:5E'
port = 4
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print(s, 888888)
try:
    s.connect((serverMACAddress,port))
    while 1:
        print("ENter input: \n")
        text = input() # Note change to the old (Python 2) raw_input
        if text == "quit":
            break
        s.send(bytes(text, 'UTF-8'))
    s.close()
except Exception as e:
    print("Exception: ", e)