import pandas as pd

csv_file = 'test_file.csv'

try:
    data = pd.read_csv(csv_file)
    filtered_data = data[data['Favorite Color'] == 'Cyan']
    print(filtered_data)
except:
    print(f'error reading CSV')