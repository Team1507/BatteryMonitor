import time
from enum import Enum

class BatteryStatus(Enum):
    #status for charging battery
    # 0 => Charger not active
    # 1 => Charger has battery, but not charging
    # 2 => Charger has battery, is charging
    # 3 => Charger has battery, completed charging
    NOT_ACTIVE = 0
    NOT_CHARGING = 1
    CHARGING = 2
    COMPLETED_CHARGING = 3
    CHECKING_BATTERY = 4

class Battery:
    def __init__(self, battery_id, slot):
        self.data = {
            "battery_id": battery_id,
            "slot": slot,
            "current_voltage": None,
            "charge_start_voltage": None,
            "charge_end_voltage": None,
            "charge_start_time": None,
            "charge_end_time": None,
            "match_start_voltage": None,
            "match_end_voltage": None,
            "match_start_time": None,
            "match_end_time": None
        }

    def updateVoltage(self, voltage):
        self.data["current_voltage"] = voltage
    
    def getCurrentVoltage(self):
        return self.data["current_voltage"]
    
    def startCharging(self, voltage):
        self.data["charge_start_voltage"] = voltage
        self.data["charge_start_time"] = get_timestamp()
    
    def endCharging(self, voltage):
        self.data["charge_end_voltage"] = voltage
        self.data["charge_end_time"] = get_timestamp()
    
    def startMatch(self, voltage):
        self.data["match_start_voltage"] = voltage
        self.data["match_start_time"] = get_timestamp()
    
    def endMatch(self, voltage):
        self.data["match_end_voltage"] = voltage
        self.data["match_end_time"] = get_timestamp()
    
    def getBatteryData(self):
        return self.data
    
    def __str__(self):
        return f"Battery {self.batteryID} | Slot {self.slot} | Start Voltage: {self.startVoltage}V | End Voltage: {self.endVoltage}V"
    
def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")
