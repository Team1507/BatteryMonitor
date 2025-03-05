import time
import RPi.GPIO as GPIO
import smbus
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from ChargingCart import BatteryCart
from Checker import BatteryChecker

#Setup the Battery Cart
teamCart = BatteryCart()

#Setup the Battery Checker
teamChecker = BatteryChecker()

# Initialize I2C bus for voltage sensors
I2C_BUS = 1  # Default I2C bus on Raspberry Pi
sensors = [0x40, 0x41, 0x42, 0x43, 0x44, 0x45]  # I2C addresses of INA219 sensors
bus = smbus.SMBus(I2C_BUS)

# Google Sheets Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPE)
client = gspread.authorize(CREDS)
sheet = client.open("FRC Battery Data").sheet1

def log_battery_data(slot, battery_id, voltage):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    data = [timestamp, slot, battery_id, voltage]
    sheet.append_row(data)
    print(f"Logged data: {data}")

def main():
    try:
        while True:
            print("Scan a battery...")
            battery_id, _ = reader.read()
            battery_id = str(battery_id).strip()
            
            for i in range(6):
                voltage = teamCart.Chargers[i].read_voltage()
                if voltage is not None:
                    log_battery_data(i + 1, battery_id, voltage)
            
            time.sleep(2)  # Small delay to prevent duplicate scans
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
