import serial

ser = serial.Serial('/dev/serial/by-id/usb-Arduino_Srl_Arduino_Uno_7543134333435161B042-if00',9600)
if ser is None:
    ser = serial.Serial('/dev/ttyUSB1',9600)
while True:
    cmd = ("R%d\n" % 30).encode('ascii')
    print("My cmd is %s" % cmd)
    ser.write(cmd)
#   For debugging, read cmd from arduino and print it    
    read_serial=ser.readline()
    print (read_serial)
