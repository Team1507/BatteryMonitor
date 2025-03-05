#Checker Program is the specific battery checker that reads a tag
#before and after the battery is to be used

class BatteryCart:
    def __init__(self):
        self.BatteryID = None
        self.currentVoltage = None

    def setBatteryID(self, batID):
        self.BatteryID = batID

    def setBatteryVoltage(self, Voltage):
        self.currentVoltage = Voltage
