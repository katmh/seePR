import serial

ser = serial.Serial("/dev/cu.usbmodem1421", 9600)
port = '/dev/ttyACM0'

#msg = ard.read(ard.inWaiting())

while True:
    x = ser.readline()
    #print(x)
        
        
    
