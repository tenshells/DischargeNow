from tkinter import messagebox

class AlertManager:
    @staticmethod
    def show_popup(title, message):
        """Show an information popup with the given title and message"""
        messagebox.showinfo(title, message)
    
    @staticmethod
    def get_alert_message(alert_type):
        """Return appropriate alert message based on alert type"""
        messages = {
            "below_charging": "Your battery is below the charging threshold. Plug in your charger.",
            "above_discharging": "Your battery is above the charging threshold. Remove your charger."
        }
        return messages.get(alert_type, "Battery status alert")
