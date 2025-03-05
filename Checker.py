#Checker Program is the specific battery checker that reads a tag
#before and after the battery is to be used

import time
from mfrc522 import SimpleMFRC522

class BatteryChecker:
    def __init__(self, sensorAddress):
        self.BatteryID = None
        self.currentVoltage = None
        self.Reader = SimpleMFRC522()
        self.sensorAddress = sensorAddress

    def addBattery(self):
        self.BatteryID = self.Reader.read()

    def removeBattery(self):
        self.BatteryID = None
        self.currentVoltage = None

    def readVoltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            self.currentVoltage = self.bus.read_word_data(self.sensorAddress, 0x02) * 0.001  # Convert to volts
        except Exception as e:
            print(f"Error reading sensor {self.sensorAddress}: {e}")
            return None

    def log_battery_data(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data = [timestamp, "Battery Checker", self.BatteryID, self.currentVoltage]
        sheet.append_row(data)
        print(f"Logged data: {data}")