import pandas as pd

csv_file = 'csv_file_name.csv'
df = pd.read_csv(csv_file, low_memory=False)
excel_file = 'exported_excel_file_name.xlsx'
df.to_excel(excel_file, index=False)
print("Convert Completed")
