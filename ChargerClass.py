import time
import smbus2 as smbus
from mfrc522 import SimpleMFRC522
from BatteryClass import Battery

class Charger:
    def __init__(self, location, sensorAddress):
        #Charger Information
        self.location = location
        self.sensorAddress = sensorAddress
        self.bus = smbus.SMBus(1)  # Default I2C bus
        self.Reader = SimpleMFRC522()

        #status for charging battery
        # 0 => Charger not active
        # 1 => Charger has battery, but not charging
        # 2 => Charger has battery, is charging
        # 3 => Charger has battery, completed charging
        self.status = 0

        #Battery Information
        self.battery = Battery(self.Reader.read(), location)

    def addBattery(self):
        self.battery.startCharging(self.readVoltage())
        self.status = 1

    def getBatteryID(self):
        return self.battery.getBatteryData()
    
    def removeBattery(self):
        self.battery.endCharging(self.readVoltage())
        self.status = 0

    def readVoltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            self.batteryVoltage = self.bus.read_word_data(self.sensorAddress, 0x02) * 0.001  # Convert to volts
            return round(self.batteryVoltage, 2)
        except Exception as e:
            print(f"Error reading sensor {self.sensorAddress}: {e}")
            return None
    
    def readCurrent(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus current
            self.batteryCurrent = self.bus.read_word_data(self.sensorAddress, 0x02) * 0.001  # Convert to amps
            return round(self.batteryCurrent, 2)
        except Exception as e:
            print(f"Error reading sensor {self.sensorAddress}: {e}")
            return None
        
    def isCharging(self, previous_voltage):
        current_voltage = self.readVoltage()
        if current_voltage is None:
            return None  # Unable to read voltage
        
        if current_voltage > previous_voltage:
            self.status = 2
            return True  # Battery is charging
        else:
            return False  # Battery is not charging