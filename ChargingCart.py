#Checker cart has 6 slots to charge 6 batteries at a time

from ChargerClass import Charger

class BatteryCart:
    def __init__(self):
        self.Chargers = [Charger(1,1), Charger(2,2), Charger(3,3), Charger(4,4), Charger(5,5), Charger(6,6)]

    def setChargerBatteryID(self, location):
        #Call this when a battery is loaded into a specific slot to set the battery ID to the charger
        self.Chargers[location].addBattery()

    def getActiveChargers(self):
        return [charger.location for charger in self.Chargers if charger.status > 0]

    def getAllBatteryData(self):
        return [charger.getBatteryID() for charger in self.Chargers if charger.battery]