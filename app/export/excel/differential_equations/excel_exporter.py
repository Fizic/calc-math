from os import path

import pandas as pd


class DifferentialEquationsExcelExporter:
    def __init__(self):
        self._file_name = "differential_equations.xlsx"

        if path.exists(self._file_name):
            xlsx = pd.ExcelFile(self._file_name, engine='openpyxl')
            self.sheet_name = "Result" + str(len(xlsx.sheet_names) + 1)
        else:
            self.sheet_name = "Result1"

        self.data = {}

    def create_columns(self, count=2, **kwargs):
        for key, value in kwargs.items():
            if key not in self.data:
                self.data[key] = []

            self.data[key].append(value)
        self.data["x"] = [None]
        self.data["y"] = [None]
        if count == 3:
            self.data["z"] = [None]

    def add_line(self, x, y, z=None):
        self.data["x"].append(x)
        self.data["y"].append(y)
        if z is not None:
            self.data["z"].append(z)

        for key in self.data.keys():
            if key in ["x", "y", "z"]:
                continue
            self.data[key].append(None)

    def save(self):
        df = pd.DataFrame(self.data)
        if path.exists(self._file_name):
            with pd.ExcelWriter(self._file_name, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, sheet_name=self.sheet_name)
                writer._save()
        else:
            with pd.ExcelWriter(self._file_name, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name=self.sheet_name)
                writer._save()
