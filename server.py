import RPi.GPIO as GPIO



# first of all import the socket library 

import socket
import serial  #not needed kept for future upgrade ;) incase i connect arduino(foolish of me to do so but learned a big lesson)
import time	
import struct


GPIO.setmode(GPIO.BOARD)    #set the rpi board numbering
GPIO.setup(11, GPIO.OUT)    #set number 11 to output
pwm1 = GPIO.PWM(11, 50)    #set number 11 pin to 50 HZ(this is the standard frequency servo like to operate on)
pwm1.start(7)		   #initially set first servo to middle 7% duty cycle

GPIO.setup(13, GPIO.OUT)	#set number 13 to output
pwm2 = GPIO.PWM(13, 50)		#set numer 13 pin to 50Hz 
pwm2.start(7)			#initially set second servo to middle 7% duty cycle


# next create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	 
print ("Socket successfully created")
serverip = '192.168.1.10'

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12346				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 

s.bind((serverip, port))		 
print("socket binded to %s" %(port)) 

# put the socket into listening mode 
s.listen(5)	 
print("socket is listening")			

# a forever loop until we interrupt it or 
# an error occurs 
c, addr = s.accept()
print('Got connection from', addr)
while True: 

    data = c.recv(1024)				#serial data will recieve in data
    #print(data.decode().split()		#for debugging ;)
    data1 = data.decode().split()		#split() function " " default use
    servo1 = int(data1[0])			#first index as int value put in servo1 
    servo2 = int(data1[1])			#second index as int value put in servo2

    print(servo1)				#debugging
    print(servo2)				#debugging

    x1 = ((1/18)*float(servo1))+2		#calculate duty cycle for x1
    pwm1.ChangeDutyCycle(x1)			#write the angle to servo 1


    x2 = ((1/18)*float(servo2))+2		#calculate duty cycle for x2
    pwm2.ChangeDutyCycle(x2)			#write the angle to servo 2

pwm1.stop()					#if the loop break stop the pwm1
pwm2.stop()					#if the loop break stop the pwm2
GPIO.cleanup()					#good practice to relase the pin of Rpi to eliminate the warnings

