# Author: Matthew Baker
# GitHub: https://github.com/mbaker92

# omxplayer filename

from time import sleep
import RPi.GPIO as gpio
import datetime
import subprocess
import time
import paho.mqtt.client as mqtt

# Initialize Camera and Set Exposure Mode
gpio.setmode(gpio.BCM)
# Button Connected to GPIO Pin 18 (Put other Pin in some GND Pin)
gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

# Setup MQTT Client
client = mqtt.Client("DoorBellSensor")
# Connect client to broker
client.connect("192.168.1.11")

# Ctrl + c in Terminal to Get Out of Infinite Loop   
while True:
    
    #Get values from button presses
    inputCamera = gpio.input(18)

    if inputCamera == False:
        print('Camera Button Pressed')
        # If The Camera Button is Pressed Take a Photo and Save With Current Date and Time
        subprocess.run(["raspistill", "-t"," 1000", "-o", "/home/pi/Documents/PiProjects/SmartHome/Photos/" +  datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + ".png"])
        # Publish picture
        client.publish("DoorBell", "Hi Niki")



