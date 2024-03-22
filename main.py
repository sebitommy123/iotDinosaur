from gpiozero import LED
from time import sleep

pin = LED(17)
while True:
  print("ON")
  pin.on()
  sleep(1)
  print("OFF")
  pin.off()
  sleep(10)