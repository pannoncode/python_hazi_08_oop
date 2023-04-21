class ReadDirectory:
    def __init__(self, folder_path, file_type):
        self.folder_path = folder_path
        self.file_type = file_type
        self.read = self.read_directory()

    def read_directory(self):
        import os
        files = []
        if not os.path.exists(self.folder_path):
            print(f"Nem létezik ez a könyvtár: {self.folder_path}")
            exit()

        for item in os.listdir(self.folder_path):
            if item.endswith(f".{self.file_type}"):
                files.append(item)
        return files


class WriteFile:
    def __init__(self, folder_path, file_name, file_data):
        self.folder_path = folder_path
        self.file_name = file_name
        self.file_data = file_data
        self.write = self.write_file()

    def write_file(self):
        import json
        try:
            with open(f"{self.folder_path}/{self.file_name}.json", "w", encoding="utf-8") as f_obj:
                json.dump(self.file_data, f_obj, ensure_ascii=False, indent=4)
            print(f"{self.file_name} létrehozás és írása SIKERES volt")
        except:
            print(f"{self.file_name} fájl létrehozása és írása SIKERTELEN volt!")
