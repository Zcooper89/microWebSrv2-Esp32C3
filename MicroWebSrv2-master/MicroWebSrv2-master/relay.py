import machine
import time

class Relay:
    def __init__(self, pin_num):
        self.pin = machine.Pin(pin_num, machine.Pin.OUT)

    def run(self):
        self.pin.on()  # Turn the relay on
        time.sleep_ms(300)  # Wait for 300ms
        self.pin.off()  # Turn the relay off
        pass
