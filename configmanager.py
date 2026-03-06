import os
import shutil as sh
import subprocess as sub
import json

class ConfigManager:
    def __init__(self):
        self.config = {}
        self.printer_profiles = {}

    def check_config(self,dir):
        if os.path.exists(dir):
            return True
        else:
            return False
    def save_config(self,dir):
        if self.check_config(dir):
            sh.copy(dir, dir + ".bak")
        with open(dir, "w") as f:
            json.dump(self.config, f, indent=4)
    def load_config(self,dir):
        if self.check_config(dir):
            with open(dir, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {"printers": []}
            self.save_config(dir)
    
    def load_printer_profiles(self, profiles_dir):
        if self.check_config(profiles_dir):
            with open(profiles_dir, "r") as f:
                data = json.load(f)
                self.printer_profiles = data.get("profiles", [])
        else:
            self.printer_profiles = []
    
    def get_printer_profiles(self):
        return self.printer_profiles
    
    def save_printer_to_config(self, printer_data):
        if "printers" not in self.config:
            self.config["printers"] = []
        self.config["printers"].append({"data": printer_data})
    
    def get_saved_printers(self):
        return self.config.get("printers", [])