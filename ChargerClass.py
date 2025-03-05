import smbus2 as smbus
from mfrc522 import SimpleMFRC522

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
        self.hasBattery = False
        self.batteryID = None

    def addBattery(self):
        self.hasBattery = True
        self.batteryID = self.Reader.read()

    def getBatteryID(self):
        return self.batteryID
    
    def removeBattery(self):
        self.hasBattery = False
        self.batteryID = None
        self.status = 0

    def read_voltage(self):
        try:
            self.bus.write_byte(self.sensorAddress, 0x02)  # Register for bus voltage
            voltage = self.bus.read_word_data(self.sensorAddress, 0x02) * 0.001  # Convert to volts
            return round(voltage, 2)
        except Exception as e:
            print(f"Error reading sensor {self.sensorAddress}: {e}")
            return None
        
    def is_charging(self, previous_voltage):
        current_voltage = self.read_voltage()
        if current_voltage is None:
            return None  # Unable to read voltage
        
        if current_voltage > previous_voltage:
            self.status = 2
            return True  # Battery is charging
        else:
            return False  # Battery is not charging