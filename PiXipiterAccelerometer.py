# Steven Coltharp - MSUCubeSat - Pi Xipiter Project - 4/29/2025

import time
import board
import busio
import adafruit_adxl34x
import RPi.GPIO as GPIO

i2c = busio.I2C(board.SCL, board.SDA)

# GPIO Setups for LED
GPIO.setmode(GPIO.BCM)
# led_pin = (Decide which pin is led pin)
# GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)


accelerometer = adafruit_adxl34x.ADXL343(i2c)
data_file = open("file_name.txt", "w")

while True:
    if any( a > 5 for a in accelerometer.acceleration) : # Checks if accelerometer is working for status LED pin
        GPIO.output(led_pin, GPIO.HIGH)
    else: 
        GPIO.output(led_pin, GPIO.LOW)

    print("%f %f %f" % accelerometer.acceleration) # Print it to test
    data_file.write(str(accelerometer.acceleration) + '\n') # Print it to file
    data_file.flush()
    time.sleep(0.1) # 0.1 Seconds
    



