import os
import json


def read_file(folder_path, files):
    if not os.path.exists(folder_path):
        print(f"Nem létezik ez a könyvtár: {folder_path}")
        exit()

    data = []
    for item in files:
        try:
            with open(f"{folder_path}/{item}", "r", encoding="utf-8") as f_obj:
                data.append(f_obj.read())
        except:
            print(f"{item} megnyitása SIKERTELEN volt!")
    return data


def convert_json_to_dict(json_files):
    data = []
    for idx in range(len(json_files)):
        data.append(json.loads(json_files[idx]))
    return data
