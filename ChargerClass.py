import time
import logging
import smbus2 as smbus
from BatteryClass import Battery

class Charger:
    def __init__(self, location, sensorAddress):
        #Charger Information
        self.location = location
        self.sensorAddress = sensorAddress
        self.bus = smbus.SMBus(1)  # Default I2C bus

        #status for charging battery
        # 0 => Charger not active
        # 1 => Charger has battery, but not charging
        # 2 => Charger has battery, is charging
        # 3 => Charger has battery, completed charging
        self.status = 0

    def addBattery(self, id):
        self.battery = Battery(id, self.location)
        self.battery.startCharging(self.readVoltage())
        self.status = 1

    def getBatteryID(self):
        return self.battery.getBatteryData()["battery_id"]
    
    def removeBattery(self):
        self.battery.endCharging(self.readVoltage())
        self.battery = None
        self.status = 0

    def getStatus(self):
        return self.status

    def readVoltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            raw_data = self.bus.read_word_data(self.sensorAddress, 0x02)
            self.battery.updateVoltage(round(raw_data * 0.001, 2))
            return self.battery.getCurrentVoltage()
        except Exception as e:
            logging.error(f"Voltage read error at {self.sensorAddress}: {e}")
            return None

    def readCurrent(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x04)  # Correct register for current
            raw_data = self.bus.read_word_data(self.sensorAddress, 0x04)
            return round(raw_data * 0.001, 2)
        except Exception as e:
            logging.error(f"Current read error at {self.sensorAddress}: {e}")
            return None

    def isCharging(self, previous_voltage):
        voltage_delta = 0.05 # Small threshold to account for fluctuations
        current_voltage = self.readVoltage()
        if current_voltage is None or previous_voltage is None:
            return None  # Unable to determine
        if current_voltage > previous_voltage + voltage_delta:  
            self.status = 2
            return True
        elif current_voltage <= previous_voltage - voltage_delta:
            self.status = 3 if self.status == 2 else 1
            return False

def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")
