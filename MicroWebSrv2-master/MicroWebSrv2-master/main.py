import network
from wifi_module import connect
sta_if = network.WLAN(network.STA_IF)

def ap_start():
    # Connect to Wi-Fi
    ssid = "C-IOT 2.4"
    password = "BrownOrange18#"
    connect(ssid, password)
    print('AP running at ' + str(sta_if.ifconfig()))

ap_start()

import uos

uos.chdir('/MicroWebSrv2-master/MicroWebSrv2-master')

import machine
from MicroWebSrv2  import *
from time          import sleep
import time
from _thread       import allocate_lock

# ============================================================================
# ============================================================================
# ============================================================================

@WebRoute(POST, '/open_garage')
def RequestHandler(self, request):
    pin = machine.Pin(0, machine.Pin.OUT)
    pin.on()  # Turn the relay on
    time.sleep_ms(300)  # Wait for 300ms
    pin.off()  # Turn the relay off

    # Return a response to the client
    return request.Response.ReturnOkJSON()


# Instanciates the MicroWebSrv2 class,
mws2 = MicroWebSrv2()

# SSL is not correctly supported on MicroPython.
# But you can uncomment the following for standard Python.
# mws2.EnableSSL( certFile = 'SSL-Cert/openhc2.crt',
#                 keyFile  = 'SSL-Cert/openhc2.key' )

# For embedded MicroPython, use a very light configuration,
mws2.SetEmbeddedConfig()

# All pages not found will be redirected to the home '/',
mws2.NotFoundURL = '/'

# Starts the server as easily as possible in managed mode,
mws2.StartManaged()

# Main program loop until keyboard interrupt,
try :
    while mws2.IsRunning :
        sleep(1)
except KeyboardInterrupt :
    pass

# End,
print()
mws2.Stop()
print('Bye')
print()

# ============================================================================
# ============================================================================
# ============================================================================
