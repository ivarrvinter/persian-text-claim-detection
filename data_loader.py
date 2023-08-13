import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_dataset(self):
        df = pd.read_csv(self.file_path)
        return df