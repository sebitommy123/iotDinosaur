from gpiozero import LED
from time import sleep

import requests
from time import sleep

last_number = None

stop_pin = LED(2)
dance_pin = LED(3)

while True:
    response = requests.get("https://zubatomic.com/dinosaur/info")
    response_text = response.text
    try:
        number = float(response_text)
        if last_number != number:
            print("New number:", number)  
            print("DANCE PIN ON")
            dance_pin.on()
            sleep(1)
            print("DANCE PIN OFF")
            dance_pin.off()
            sleep(5)
        last_number = number
    except ValueError:
        print("Received text could not be converted to a number:", response_text)
    
    print("STOP PIN ON")
    stop_pin.on()
    sleep(1)
    print("STOP PIN OFF")
    stop_pin.off()
    sleep(1)
