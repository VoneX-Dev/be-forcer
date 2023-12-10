import os
import subprocess

class Forcer:
    @staticmethod
    def kill_eac():
        if Forcer.is_process_running("EasyAntiCheat.exe") or Forcer.is_process_running("FortniteClient-Win64-Shipping_EAC.exe"):
            # If EAC is found, terminate it
            print("Found EAC")
            os.system("TASKKILL /F /IM EasyAntiCheat.exe >nul")
            os.system("TASKKILL /F /IM FortniteClient-Win64-Shipping_EAC.exe >nul")
            subprocess.run(["sc", "stop", "EasyAntiCheat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("EAC killed")

    @staticmethod
    def force_battleye():
        if not Forcer.is_process_running("EasyAntiCheat.exe") and Forcer.is_process_running("FortniteClient-Win64-Shipping_EAC.exe"):
            subprocess.Popen([
                "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping_BE.exe"
            ])
            print("BE Successfully Executed")

    @staticmethod
    def is_process_running(process_name):
        try:
            subprocess.check_output(["tasklist", "/FI", f"IMAGENAME eq {process_name}", "/FO", "CSV"]).decode("utf-8")
            return True
        except subprocess.CalledProcessError:
            return False

# Example usage:
# Forcer.kill_eac()
# Forcer.force_battleye()
