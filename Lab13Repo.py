from gpiozero import LED, Button
from time import sleep
import random
led = LED(21)
right_button = Button(16)
left_button = Button(20)
left_name = ("Player1")
right_name= ('PLayer2')


def pressed(button):
    global right_name
    global left_name
    if button.pin.number == 20:
        print(left_name + 'pressed first!')
       
        led.off()
    elif button.pin.number == 16:
        print(right_name + ' pressed first!')
        
        led.off()
        

for i in range (0, 10):
    sleep(4)
    led.on()
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    
    