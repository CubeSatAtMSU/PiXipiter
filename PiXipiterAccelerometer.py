# Steven Coltharp - MSUCubeSat - Pi Xipiter Project - 4/29/2025

import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)

accelerometer = adafruit_adxl34x.ADXL343(i2c)
data_file = open("file_name.txt", "w")

while True:
    print("%f %f %f" % accelerometer.acceleration) # Print it to test
    data_file.write(str(accelerometer.acceleration) + '\n') # Print it to file
    data_file.flush()
    time.sleep(0.1) # 0.1 Seconds
    



