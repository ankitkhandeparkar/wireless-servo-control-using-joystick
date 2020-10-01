## Author : ANKIT V KHANDEPARKAR

# Import socket module 
import socket			 
import serial
import time
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
serverip = '192.168.1.10'	 

# Define the port on which you want to connect 
port = 12346				

# connect to the server on local computer 
s.connect((serverip, port)) 

ser = serial.Serial('COM4', 1200)

time.sleep(2)
while True:
    joystickValues = ser.readline().decode().strip('\r\n')
    #joystickValues = ser.readline()
    
    s.send(joystickValues.encode())
    
     
    #s.send(joystickValues)
    print(joystickValues)	 
