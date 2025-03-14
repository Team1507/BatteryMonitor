#Checker cart has 6 slots to charge 6 batteries at a time

from ChargerClass import Charger
from mfrc522 import SimpleMFRC522

class BatteryCart:
    def __init__(self):
        self.Chargers = [Charger(1,1), Charger(2,2), Charger(3,3), Charger(4,4), Charger(5,5), Charger(6,6)]
        self.Readers = [SimpleMFRC522(), SimpleMFRC522(), SimpleMFRC522(), SimpleMFRC522(), SimpleMFRC522(), SimpleMFRC522()]

    def getActiveChargers(self):
        return [charger.location for charger in self.Chargers if charger.status > 0]

    def getAllBatteryData(self):
        return [charger.getBatteryID() for charger in self.Chargers if charger.battery]
    
    def addBattery(self, location):
        self.Chargers[location].addBattery(self.Readers[location].read_id())
        if self.Chargers[location].getStatus() > 0:
            return True
        else: return False

    def removeBattery(self, location):
        self.Chargers[location].removeBattery()
        if self.Chargers[location].getStatus() == BatteryStatus.NOT_ACTIVE:
            return True
        else: return False

    def updateCharge(self):
        for i in range(6):
            if self.Chargers[i].getStatus() > 0:
                print( "Charger #", i,
                      " : Status: ", self.Chargers[i].getStatus(), " : ",
                      self.Chargers[i].readVoltage(), "V @ ",
                      self.Chargers[i].readCurrent(), "A")