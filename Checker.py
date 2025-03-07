#Checker Program is the specific battery checker that reads a tag
#before and after the battery is to be used

import time
import logging
import smbus2 as smbus
from mfrc522 import SimpleMFRC522
from BatteryClass import Battery

class BatteryChecker:
    def __init__(self, sensorAddress):
        self.battery = None
        self.Reader = SimpleMFRC522()
        self.bus = smbus.SMBus(1)  # Default I2C bus
        self.sensorAddress = sensorAddress
        
    def addBattery(self):
        self.battery = Battery(self.Reader.read_id(), "Battery Checker")

    def removeBattery(self):
        self.battery = None
        
    def batteryBeforeMatch(self):
        if not self.battery:
            print("Error: No battery detected!")
            return
        self.battery.startMatch(self.readVoltage())

    def batteryAfterMatch(self):
        if not self.battery:
            print("Error: No battery detected!")
            return
        self.battery.endMatch(self.readVoltage())

    def readVoltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            raw_data = self.bus.read_word_data(self.sensorAddress, 0x02)
            self.battery.updateVoltage(round(raw_data * 0.001, 2))
            return self.battery.getCurrentVoltage()
        except Exception as e:
            logging.error(f"Voltage read error at {self.sensorAddress}: {e}")
            return None

    def getBatteryDataLog(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        data = [timestamp, "Battery Checker", self.battery.getBatteryData(), self.currentVoltage]
        return data