#Checker cart has 6 slots to charge 6 batteries at a time

import ChargerClass

class BatteryCart:
    def __init__(self):
        self.Chargers = [ChargerClass(1,1), ChargerClass(2,2), ChargerClass(3,3), ChargerClass(4,4), ChargerClass(5,5), ChargerClass(6,6)]

    def setChargerBatteryID(self, location, batID):
        #Call this when a battery is loaded into a specific slot to set the battery ID to the charger
        self.Chargers[location].setBatteryID(batID)

