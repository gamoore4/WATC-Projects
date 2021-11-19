import time 

import analogio
import board
import digitalio
import storage

"""

"""
def get_voltage(pin):
    return(pin.value * 5)/


vbat_voltage = analogio.AnalogIn(board.D9)
multiplex1 = analogio.AnalogIn(board.D)
# Setup the AM2320
i2c = board.I2C()
am2320 = adafruit_am2320.AM2320(i2c)

SD_CS = board.D10
spi = board.SPI()
cs = digitalio.DigitalInOut(SD_CS)
sd_card = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sd_card)
storage.mount(vfs, "/sd_card")



while True:
    try:
        with open("/sd_card/log.txt", "a") as sdc:
            temperature = am2320.temperature 
            humidity = am2320.relative_humidity 
            battery_voltage = get_voltage(vbat_voltage)



        time.sleep(100)
    except OSError:
        pass
    except RuntimeError:
        pass