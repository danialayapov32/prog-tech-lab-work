import json

class ConfigValidator:
    def __init__(self, json_path, csv_path):
        self.json_path = json_path
        self.csv_path = csv_path
        self.preset = {}
        self.header_cols = []

    def load_config(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            self.preset = json.load(f)
        return self.preset

    def validate_headers(self):
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            header_line = f.readline().strip()
            self.header_cols = header_line.split(',')

        x_name = self.preset.get('x')
        y_name = self.preset.get('y')

        if x_name in self.header_cols and y_name in self.header_cols:
            print(f"Columns '{x_name}' and '{y_name}' have been found.")
            return True
        else:
            print(f"Error! Expected: {x_name}, {y_name}. Found only: {self.header_cols}")
            return False

