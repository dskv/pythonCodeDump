# to clear the screen

###############################################
#### Wiring for I2C
#### For Raspberry Pi Zero Wireless (RPiZW)
#### 4 pin OLED wiring
#### VCC --> Pin1,(VCC 3.3)
#### GND --> Pin9,(GROUND)
#### SCL --> Pin5,GPIO-03/(SCL1,I2C)
#### SDA --> Pin3,GPIO-02/(SDA1,I2C)
###############################################

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24

#disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()
