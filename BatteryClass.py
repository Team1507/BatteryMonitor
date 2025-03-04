import time

class Battery:
    def __init__(self, battery_id, slot):
        self.battery_id = battery_id  # Unique RFID tag ID
        self.slot = slot  # Charging station slot number
        self.start_voltage = None  # Voltage before match
        self.end_voltage = None  # Voltage after match
        self.charge_start_voltage = None # Voltage before charging
        self.charge_end_voltage = None # Voltage after charging
        self.charge_start_time = None
        self.charge_end_time = None
        self.match_start_time = None
        self.match_end_time = None
    
    def start_charging(self, voltage):
        self.charge_start_voltage = voltage
        self.charge_start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.battery_id} started charging at {self.start_voltage}V on {self.charge_start_time}")
    
    def end_charging(self, voltage):
        self.charge_end_voltage = voltage
        self.charge_end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.battery_id} finished charging at {self.end_voltage}V on {self.charge_end_time}")
    
    def start_match(self, voltage):
        self.start_voltage = voltage
        self.match_start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.battery_id} started match at {self.start_voltage}V on {self.match_start_time}")
    
    def end_match(self, voltage):
        self.end_voltage = voltage
        self.match_end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Battery {self.battery_id} ended match at {self.end_voltage}V on {self.match_end_time}")
    
    def get_battery_data(self):
        return {
            "battery_id": self.battery_id,
            "slot": self.slot,
            "start_voltage": self.start_voltage,
            "end_voltage": self.end_voltage,
            "charge_start_time": self.charge_start_time,
            "charge_end_time": self.charge_end_time,
            "match_start_time": self.match_start_time,
            "match_end_time": self.match_end_time
        }
    
    def __str__(self):
        return f"Battery {self.battery_id} | Slot {self.slot} | Start Voltage: {self.start_voltage}V | End Voltage: {self.end_voltage}V"
