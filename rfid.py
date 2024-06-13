# Required modules are inserted and configured
import time
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

def rfid_anzeige():
    # Create object rfid for the module
    rfid = SimpleMFRC522()

    # Modify this if you have a different sized Character LCD
    lcd_columns = 16
    lcd_rows = 2

    # Initialise I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA

    # Initialise the lcd class
    lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)
    
    try:
        while True:
            lcd.backlight = True
            lcd.message = "Halte den RFID\nan den Reader"
            print("Hold a tag near reader")
            # get ID and text from the tag and write text#
            id, text = rfid.read()
            
            time.sleep(5)
            lcd.clear
            lcd.message = text
            # wait 30 seconds for next
            time.sleep(30)
    except KeyboardInterrupt:
        #clean up after programm terminated
        lcd.clear
        lcd.backlight = False
        GPIO.cleanup()
