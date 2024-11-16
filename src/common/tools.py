import os
import json
from pathlib import Path

file_dir = os.getenv('APPDATA') + '\\' + 'ddmy\\'

def save_json(data, json_file_name):
    Path(file_dir).mkdir(parents=True, exist_ok=True)
    with open(file_dir + json_file_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, default=str, ensure_ascii=False, indent=4)

def load_json(json_file_name):
    try:
        with open(file_dir + json_file_name, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None