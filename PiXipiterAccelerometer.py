# Steven Coltharp - MSUCubeSat - Pi Xipiter Project - 4/29/2025

import time
import board
import busio
import adafruit_adxl34x
import RPi.GPIO as GPIO
import math
#import smbus

i2c = busio.I2C(board.SCL, board.SDA)

# GPIO Setups for LED test
#GPIO.setmode(GPIO.BCM)
# led_pin = (Decide which pin is led pin)
# GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

#i2c Setup for UPS HAT ( Uncomment when ready to test ) 
#addr=0x10 #ups i2c address
#bus=smbus.SMBus(1) #i2c-1
#vcellH=bus.read_byte_data(addr,0x03)
#vcellL=bus.read_byte_data(addr,0x04)
#socH=bus.read_byte_data(addr,0x05)
#socL=bus.read_byte_data(addr,0x06)


accelerometer = adafruit_adxl34x.ADXL343(i2c)
data_file = open("/home/xipiter/PiXipiter/file_name.txt", "a+")

while True:
    x,y,z = accelerometer.acceleration # Assigns individual vector components of acceleration
    magAcc = math.sqrt(x**2 + y**2 + z**2) # Magnitude of acceleration
    
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    data_file.write(str(magAcc) + "   "  + current_time + '\n') # Print it to file
    print("%f" %magAcc) # Print it to test
    print(current_time)
    data_file.flush()
    time.sleep(0.1) # 0.1 Seconds
    



