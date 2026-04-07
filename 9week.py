import json

with open('preset.json', 'r', encoding='utf-8') as f:
    preset = json.load(f)

x_name = preset.get('x')
y_name = preset.get('y')

with open('plot_data.csv', 'r', encoding='utf-8') as f:
    header_line = f.readline().strip() 
    header_cols = header_line.split(',')


if x_name in header_cols and y_name in header_cols:
    print(f"columns '{x_name}' and '{y_name}' have found.")
else:
    print("Error")
    print(f"only: {header_cols}")