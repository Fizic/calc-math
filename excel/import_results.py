from os import path

import pandas as pd


class ExcelImporter:
    def __init__(self, file_name: str = None, sheet_name: str = None):
        self.file_name = file_name
        self.sheet_name = sheet_name
        if path.exists(file_name):
            # save the current information
            xlsx = pd.ExcelFile(self.file_name, engine='openpyxl')

            if self.sheet_name in xlsx.sheet_names:
                df = pd.read_excel(self.file_name, self.sheet_name, index_col=0, engine='openpyxl')
                self.data: dict[str:list] = df.to_dict('list')
            else:
                self.data = {}

            self.writer = pd.ExcelWriter(self.file_name)
            for sheet_name in xlsx.sheet_names:
                raw_data = pd.read_excel(xlsx, sheet_name, index_col=0, engine='openpyxl')
                raw_data.to_excel(self.writer, sheet_name=sheet_name)
        else:
            self.writer = pd.ExcelWriter(self.file_name)
            self.data = {}

    def add_data(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.data:
                self.data[key] = []

            self.data[key].append(value)

    def save_data(self):
        df = pd.DataFrame(self.data)
        df.to_excel(self.writer, sheet_name=self.sheet_name)
        self.writer._save()


def update_data(type_of_calculations: str = None, method: str = None, **kwargs):
    ei = ExcelImporter(f'./{type_of_calculations}.xlsx', "Sheet1")
    ei.add_data(**kwargs, method=method)
    ei.save_data()
