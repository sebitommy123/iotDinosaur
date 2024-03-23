from gpiozero import LED
from time import sleep

import requests
from time import sleep

last_number = None

dino_pin = LED(2)

send_every = 60 # seconds
s = 0

while True:
    response = requests.get("https://zubatomic.com/dinosaur/info")
    response_text = response.text
    try:
        number = float(response_text)
        if last_number != number and last_number is not None:
            print("New number:", number)  
            print("PIN ON")
            dino_pin.on()
            sleep(5)
            print("PIN OFF")
            dino_pin.off()
        last_number = number
    except ValueError:
        print("Received text could not be converted to a number:", response_text)

    sleep(2)
