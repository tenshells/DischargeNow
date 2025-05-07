
from tkinter import ttk, DoubleVar, Frame, Label, HORIZONTAL, X as tk_X
from .battery import BatteryMonitor
from .alerts import AlertManager
from config import config

class BatteryMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Battery Monitor")
        
        self.battery = BatteryMonitor()
        self.alerts = AlertManager()
        
        # Initialize thresholds
        self.charging_threshold = DoubleVar(value=config.charging_threshold)
        self.discharging_threshold = DoubleVar(value=config.discharging_threshold)
        
        self.setup_ui()
        self.update_battery_label()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Main frame
        self.frame = Frame(self.root, width=300, height=300, bg="lightblue")
        self.frame.pack(padx=10, pady=10)
        self.frame.pack_propagate(False)
        
        # Battery status label
        self.status = Label(self.frame, text="", font=("Arial", 14), bg="lightblue")
        self.status.pack()
        
        # Charging threshold slider
        ttk.Label(self.frame, text="Set Charging Threshold:", background="lightblue").pack()
        self.charge_slider = ttk.Scale(
            self.frame, 
            from_=0, 
            to=100, 
            variable=self.charging_threshold,
            orient=HORIZONTAL, 
            command=lambda v: self.update_plug_label(float(v))
        )
        self.charge_slider.pack(pady=10, padx=20, fill=tk_X)
        
        self.report_plug = Label(self.frame, text="Report Charging Threshold", font=("Arial", 12))
        self.report_plug.pack()
        
        # Discharging threshold slider
        ttk.Label(self.frame, text="Set Discharging Threshold:", background="lightblue").pack()
        self.discharge_slider = ttk.Scale(
            self.frame, 
            from_=0, 
            to=100, 
            variable=self.discharging_threshold,
            orient=HORIZONTAL, 
            command=lambda v: self.update_unplug_label(float(v))
        )
        self.discharge_slider.pack(pady=10, padx=20, fill=tk_X)
        
        self.report_unplug = Label(self.frame, text="Report Discharging Threshold", font=("Arial", 12))
        self.report_unplug.pack()
    
    def update_plug_label(self, value):
        """Update the charging threshold label"""
        self.report_plug.config(text=f"Report to Plug Charger at {int(value)}%", fg="blue")
    
    def update_unplug_label(self, value):
        """Update the discharging threshold label"""
        self.report_unplug.config(text=f"Report to Unplug Charger at {int(value)}%", fg="orange")
    
    def update_battery_label(self):
        """Update the battery status and check thresholds"""
        percent, is_charging = self.battery.get_battery_status()
        percent = int(percent)
        
        # Update status label
        status_text = f"Battery: {percent}%, {'Charging' if is_charging else 'Discharging'}"
        self.status.config(
            text=status_text,
            fg="green" if is_charging else "red"
        )
        
        # Check thresholds
        alert_type = self.battery.check_battery_thresholds(
            self.charging_threshold.get(),
            self.discharging_threshold.get()
        )
        
        if alert_type:
            self.alerts.show_popup(
                "Battery Alert",
                self.alerts.get_alert_message(alert_type)
            )
        
        # Schedule next update
        self.root.after(config.refresh_interval, self.update_battery_label)
