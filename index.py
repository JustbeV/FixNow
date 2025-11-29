import ctypes 
import sys
import subprocess
import customtkinter as ctk   # type: ignore
from tkinter import messagebox

# Admin check
def is_admin():
    """Check if the script is running as admin."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    import os
    script = os.path.abspath(sys.argv[0])
    """Re-run the script with admin privileges (UAC prompt)"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}', None, 1)

# SFC scan function
def run_sfc_scan():
    """Run the sfc /scannow command."""
    messagebox.showinfo("FixNow", "SFC scan is starting. This may take several minutes...")
    try:
        subprocess.run("sfc /scannow", shell=True)
        messagebox.showinfo("FixNow", "Scan complete!")
    except Exception as e:
        messagebox.showerror("FixNow", f"An error occurred:\n{e}")

# Main GUI
def main():
    if not is_admin():
        run_as_admin()
        sys.exit()  # exit non-admin

    # Setup GUI
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("400x200")
    app.title("FixNow: One Click PC Repair")

    # Title Label
    label = ctk.CTkLabel(app, text="FixNow", font=("Arial", 24, "bold"))
    label.pack(pady=(20, 10))

    # Subtitle
    sub_label = ctk.CTkLabel(app, text="Click the button to repair your PC (SFC Scan)")
    sub_label.pack(pady=(0, 20))

    # Run Scan Button
    button = ctk.CTkButton(app, text="Run SFC Scan", command=run_sfc_scan, width=200, height=40)
    button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main()
