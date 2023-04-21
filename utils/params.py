class FolderPath:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.folder = self.folder_path()

    def folder_path(self):
        import os
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), self.folder_name)
