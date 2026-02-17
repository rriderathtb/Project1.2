import tkinter as tk
from tkinter import messagebox
import threading
import os
from detector import Detector

class PreventXGUI:
    def __init__(self):
        self.detector = Detector()
        self.window = tk.Tk()
        self.window.title("PreventX - Defense System")
        self.window.geometry("400x250")

        tk.Label(self.window, text="PreventX Security", font=("Arial", 14)).pack(pady=20)
        
        self.start_btn = tk.Button(self.window, text="Start Monitoring", command=self.run_detector)
        self.start_btn.pack(pady=10)

        tk.Button(self.window, text="Exit", command=self.stop).pack(pady=10)
        self.window.mainloop()

    def run_detector(self):
        # Running detector in a thread prevents the UI from freezing
        self.start_btn.config(state="disabled", text="Monitoring...")
        thread = threading.Thread(target=self.detector.start, daemon=True)
        thread.start()
        messagebox.showinfo("Status", "Packet Sniffing Started.")

    def stop(self):
        os._exit(0) # Force close all threads
        