from gpiozero import LED
from time import sleep

import requests
from time import sleep

last_number = None

pin = LED(17)

while True:
    response = requests.get("https://zubatomic.com/dinosaur/info")
    response_text = response.text
    try:
        number = float(response_text)
        if last_number != number:
            print("New number:", number)  
            print("PIN ON")
            pin.on()
            sleep(1)
            print("PIN OFF")
            pin.off()
        last_number = number
    except ValueError:
        print("Received text could not be converted to a number:", response_text)

    sleep(2)
