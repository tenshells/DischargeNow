import tkinter as tk
from tkinter import messagebox
import psutil

# Global variables for thresholds

root = tk.Tk()
root.title("Battery Monitor")

frame = tk.Frame(root, width=300, height=300, bg="lightblue")
frame.pack(padx=10, pady=10)
frame.pack_propagate(False)

charging_threshold = tk.DoubleVar(value=30)
discharging_threshold = tk.DoubleVar(value=100)


def update_battery_label():
    battery_percent = int(psutil.sensors_battery().percent)
    isCharging = psutil.sensors_battery()[2]
    if isCharging:
        status.config(text=f"Battery: {battery_percent}%, Charging", fg="green")
    else:
        status.config(text=f"Battery: {battery_percent}%, Discharging", fg="red")
        
    # Check if battery is below discharging threshold
    if battery_percent <= int(charging_threshold.get()) and not(isCharging):
        show_popup("Charge Now", "Your battery is below the discharging threshold. Plug in your charger.")
    
    if battery_percent >= int(discharging_threshold.get()) and isCharging:
        show_popup("Charge Now", "Your battery is above the charging threshold. Remove your charger.")
    
    root.after(2000, update_battery_label)  # Update every 2000 milliseconds (2 seconds)

def show_popup(title, message):
    messagebox.showinfo(title, message)

def plug_label(value):
    report_plug.config(text=f"Report to Plug Charger at {value}%", fg="blue")
    global charging_threshold
    charging_threshold=tk.DoubleVar(value=value)

def unplug_label(value):
    report_unplug.config(text=f"Report to Unplug Charger at {value}%", fg="orange")
    global discharging_threshold
    discharging_threshold=tk.DoubleVar(value=value)

status = tk.Label(frame, text="", font=("Arial", 14), bg="lightblue")
status.pack()

charge_slider = tk.Scale(frame, from_=0, to=100, variable=charging_threshold, orient=tk.HORIZONTAL, length=300, command=plug_label)
charge_slider.pack(pady=20)
report_plug = tk.Label(frame, text="Report Charging Threshold", font=("Arial", 12))
report_plug.pack()

discharge_slider = tk.Scale(frame, from_=0, to=100, variable=discharging_threshold,orient=tk.HORIZONTAL, length=300, command=unplug_label)
discharge_slider.pack(pady=20)
report_unplug = tk.Label(frame, text="Report Discharging Threshold", font=("Arial", 12))
report_unplug.pack()

# Initial updates
update_battery_label()
root.mainloop()