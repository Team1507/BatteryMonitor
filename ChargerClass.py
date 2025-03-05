class Charger:
    def __init__(self, location, IO):
        self.location = location
        self.IO = IO
        #status for charging battery
        # 0 => Charger not active
        # 1 => Charger has battery, but not charging
        # 2 => Charger has battery, is charging
        # 3 => Charger has battery, completed charging
        self.status = 0
        self.battery = False
        self.batteryID = None

    def setBatteryID(self, ID):
        self.batteryID = ID

    def getBatteryID(self):
        return self.batteryID