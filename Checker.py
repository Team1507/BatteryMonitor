#Checker Program is the specific battery checker that reads a tag
#before and after the battery is to be used

import time
from mfrc522 import SimpleMFRC522
from BatteryClass import Battery

class BatteryChecker:
    def __init__(self, sensorAddress):
        self.battery = Battery("Battery Checker")
        self.Reader = SimpleMFRC522()
        self.sensorAddress = sensorAddress

    def addBattery(self):
        self.battery.updateCurrentVoltage(self.readVoltage())

    def batteryBeforeMatch(self):
        self.battery.startMatch(self.readVoltage())
        if self.battery.getCurrentVoltage() < 12:
            print("Battery is less than 12V do not use!")

    def batteryAfterMatch(self):
        self.battery.endMatch(self.readVoltage())

    def removeBattery(self):
        self.battery = None
        self.currentVoltage = None

    def readVoltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            self.currentVoltage = self.bus.read_word_data(self.sensorAddress, 0x02) * 0.001  # Convert to volts
        except Exception as e:
            print(f"Error reading sensor {self.sensorAddress}: {e}")
            return None

    def getBatteryDataLog(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data = [timestamp, "Battery Checker", self.battery.getBatteryData(), self.currentVoltage]
        return data