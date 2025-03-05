import time

class Battery:
    def __init__(self, battery_id, slot):
        self.batteryID = battery_id  # Unique RFID tag ID
        self.slot = slot  # Charging station slot number
        self.currentVoltage = None
        self.startVoltage = None  # Voltage before match
        self.endVoltage = None  # Voltage after match
        self.chargeStartVoltage = None # Voltage before charging
        self.chargeEndVoltage = None # Voltage after charging
        self.chargeStartTime = None
        self.chargeEndTime = None
        self.matchStartTime = None
        self.matchEndTime = None

    def updateCurrentVoltage(self, voltage):
        self.currentVoltage = voltage

    def getCurrentVoltage(self):
        return self.currentVoltage
    
    def startCharging(self, voltage):
        self.chargeStartVoltage = voltage
        self.chargeStartTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.batteryID} started charging at {self.startVoltage}V on {self.chargeStartTime}")
    
    def endCharging(self, voltage):
        self.chargeEndVoltage = voltage
        self.chargeEndTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.batteryID} finished charging at {self.endVoltage}V on {self.chargeEndTime}")
    
    def startMatch(self, voltage):
        self.startVoltage = voltage
        self.matchStartTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.batteryID} started match at {self.startVoltage}V on {self.matchStartTime}")
    
    def endMatch(self, voltage):
        self.endVoltage = voltage
        self.matchEndTime = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.batteryID} ended match at {self.endVoltage}V on {self.matchEndTime}")
    
    def getBatteryData(self):
        return {
            "battery_id": self.batteryID,
            "slot": self.slot,
            "start_voltage": self.startVoltage,
            "end_voltage": self.endVoltage,
            "charge_start_time": self.chargeStartTime,
            "charge_end_time": self.chargeEndTime,
            "match_start_time": self.matchStartTime,
            "match_end_time": self.matchEndTime
        }
    
    def __str__(self):
        return f"Battery {self.batteryID} | Slot {self.slot} | Start Voltage: {self.startVoltage}V | End Voltage: {self.endVoltage}V"
