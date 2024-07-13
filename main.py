import pandas as pd

csv_file = 'test.csv'

try:
    data = pd.read_csv(csv_file)
    filtered_data = data[data['Favorite Bird'] == 'Hawk']
    print(filtered_data)
except:
    print(f'error reading CSV')