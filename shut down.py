import os
import sys
import tkinter as tk
from tkinter import messagebox

class ShutdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Shutdown Application")

        self.label = tk.Label(master, text="Click the button to shut down your system")
        self.label.pack(padx=20, pady=10)

        self.shutdown_button = tk.Button(master, text="Shutdown", command=self.confirm_and_shutdown)
        self.shutdown_button.pack(pady=10)

    def confirm_and_shutdown(self):
        answer = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shut down?")
        if not answer:
            return

        try:
            if sys.platform.startswith('win'):
                os.system("shutdown /s /t 1")
            else:
                os.system("sudo shutdown -h now")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shutdown:\n{e}")

def main():
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
