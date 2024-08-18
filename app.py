import tkinter as tk
from tkinter import messagebox
import psutil

# Global variables for thresholds

root = tk.Tk()
root.title("Battery Monitor")

frame = tk.Frame(root, width=300, height=300, bg="lightblue")
frame.pack(padx=10, pady=10)
frame.pack_propagate(False)

charging_threshold = 10
discharging_threshold = 100


def update_battery_label():
    battery_percent = int(psutil.sensors_battery().percent)
    isCharging = psutil.sensors_battery()[2]
    if isCharging:
        label1.config(text=f"Battery: {battery_percent}%, Charging", fg="green")
    else:
        label1.config(text=f"Battery: {battery_percent}%, Discharging", fg="red")
        
    # Check if battery is below discharging threshold
    if battery_percent <= charging_threshold and not(isCharging):
        show_popup("Charge Now", "Your battery is below the discharging threshold. Plug in your charger.")
    
    if battery_percent >= discharging_threshold and isCharging:
        show_popup("Charge Now", "Your battery is above the charging threshold. Remove your charger.")
    
    root.after(2000, update_battery_label)  # Update every 1000 milliseconds (1 second)

def show_popup(title, message):
    messagebox.showinfo(title, message)

def update_label2(value):
    label2.config(text=f"Report to Plug Charger at {value}%", fg="blue")
    global charging_threshold
    charging_threshold=int(value)

def update_label3(value):
    label3.config(text=f"Report to Unplug Charger at {value}%", fg="orange")
    global discharging_threshold
    discharging_threshold=int(value)

label1 = tk.Label(frame, text="", font=("Arial", 14), bg="lightblue")
label1.pack()

slider1 = tk.Scale(frame, from_=0, to=100, variable=0, orient=tk.HORIZONTAL, length=300, command=update_label2)
slider1.pack(pady=20)
label2 = tk.Label(frame, text="Report Charging Threshold", font=("Arial", 12))
label2.pack()

default_value = tk.DoubleVar(value=100)
slider2 = tk.Scale(frame, from_=0, to=100, variable=default_value,orient=tk.HORIZONTAL, length=300, command=update_label3)
slider2.pack(pady=20)
label3 = tk.Label(frame, text="Report Discharging Threshold", font=("Arial", 12))
label3.pack()

# Initial updates
update_battery_label()
root.mainloop()