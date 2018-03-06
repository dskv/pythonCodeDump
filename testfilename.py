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
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,disp.width-1,disp.height-1), outline=1, fill=0)

font = ImageFont.load_default()
draw.text((3, 0),'Hello Denis |',  font=font, fill=255)
draw.text((3, 20),'OLED TEST CODE', font=font, fill=255)

disp.image(image)
disp.display()

