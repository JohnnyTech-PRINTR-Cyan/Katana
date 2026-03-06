import flask
from flask import *
from version import *
from configmanager import *
app = Flask(__name__)
config = ConfigManager()

@app.route('/')
def load():
    if config.check_config("config.json"):
        config.load_config("config.json")
        return render_template('index.html', version=v, page_title="Katana")
    else:
        return render_template('welcomeflow.html', version=v, page_title="Katana")

@app.route('/welcome')
def welcome():
    return render_template('welcomeflow.html', version=v, page_title="Katana")

@app.route('/printer_setup')
def printer_setup():
    # Load prebuilt profiles
    config.load_printer_profiles("printers/printer-settings.json")
    prebuilt_profiles = config.get_printer_profiles()
    
    # Load saved config
    config.load_config("config.json")
    saved_printers = config.get_saved_printers()
    
    return render_template('printer-setup.html', 
                         version=v, 
                         page_title="Katana - Printer Setup",
                         profiles=prebuilt_profiles,
                         saved_printers=saved_printers)

@app.route('/save_custom_printer', methods=['POST'])
def save_custom_printer():
    try:
        printer_data = request.get_json()
        
        # Load current config
        config.load_config("config.json")
        
        # Save the custom printer
        config.save_printer_to_config(printer_data)
        config.save_config("config.json")
        
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/save_printer_selection', methods=['POST'])
def save_printer_selection():
    try:
        data = request.get_json()
        
        # Load current config and printer profiles
        config.load_config("config.json")
        config.load_printer_profiles("printers/printer-settings.json")
        
        # Get the actual profile data
        if data['type'] == 'prebuilt':
            # Get prebuilt profile by index
            profiles = config.get_printer_profiles()
            if 0 <= data['index'] < len(profiles):
                profile_data = profiles[data['index']]
            else:
                return jsonify({"success": False, "error": "Invalid profile index"})
        elif data['type'] == 'saved':
            # Get saved profile by index
            saved_printers = config.get_saved_printers()
            if 0 <= data['index'] < len(saved_printers):
                profile_data = saved_printers[data['index']]['data']
            else:
                return jsonify({"success": False, "error": "Invalid saved profile index"})
        else:
            return jsonify({"success": False, "error": "Invalid profile type"})
        
        # Save the full profile data
        if "selected_printer" not in config.config:
            config.config["selected_printer"] = {}
        
        config.config["selected_printer"] = profile_data
        config.save_config("config.json")
        
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
    
print("DO NOT RUN THIS SCRIPT DIRECTLY! USE main.py TO RUN KATANA!")
