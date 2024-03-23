from gpiozero import LED
from time import sleep

import requests
from time import sleep

last_number = None

stop_pin = LED(2)
dance_pin = LED(3)

send_every = 60 # seconds
s = 0

while True:
    response = requests.get("https://zubatomic.com/dinosaur/info")
    response_text = response.text
    try:
        number = float(response_text)
        if last_number != number and last_number is not None:
            print("New number:", number)  
            print("DANCE PIN ON")
            dance_pin.on()
            sleep(1)
            s += 1
            print("DANCE PIN OFF")
            dance_pin.off()
            sleep(5)
            s += 5
        last_number = number
    except ValueError:
        print("Received text could not be converted to a number:", response_text)
    
    if s >= send_every:
        s = 0
        print("STOP PIN ON")
        stop_pin.on()
        sleep(1)
        s += 1
        print("STOP PIN OFF")
        stop_pin.off()
        sleep(1)
        s += 1
    
    sleep(2)
