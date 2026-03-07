import json
def get_fluidd_ui():
    with open("fluidd_ui.json", "r") as f:
        return json.load(f)["ip"]
    
