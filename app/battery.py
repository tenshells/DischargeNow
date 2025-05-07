import psutil

class BatteryMonitor:
    def __init__(self):
        self.battery = psutil.sensors_battery()
    
    def get_battery_status(self):
        """Returns battery percentage and charging status"""
        battery = psutil.sensors_battery()
        return battery.percent, battery.power_plugged
    
    def check_battery_thresholds(self, charging_threshold, discharging_threshold):
        """Check if battery levels cross the defined thresholds"""
        percent, is_charging = self.get_battery_status()
        percent = int(percent)
        
        if percent <= charging_threshold and not is_charging:
            return "below_charging"
        elif percent >= discharging_threshold and is_charging:
            return "above_discharging"
        return None
