import tkinter as tk
from app.gui import BatteryMonitorApp

def main():
    root = tk.Tk()
    app = BatteryMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
